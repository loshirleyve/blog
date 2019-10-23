# -*- coding: utf-8 -*-
import codecs
from win32com import client as wc
import re
import chardet
from bs4 import BeautifulSoup, Comment
import os


def init():
    path = os.getcwd()  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    html_dir = os.path.join(path, 'html')
    try:
        os.mkdir(html_dir)
    except FileExistsError as e:
        print(e)
    for file in files:  # 遍历文件夹
        if os.path.isfile(file) and file.split('.')[1] == 'docx':
            main(path, html_dir, file)


def main(word_dir, html_dir, word_name):
    html_name = word_name.split('.')[0] + '.html'
    # html_name1 = word_name.split('.')[0] + '1.html'
    html = word_to_html(os.path.join(word_dir, word_name), os.path.join(html_dir, html_name))
    res = format_html(html)
    html = my_beautiful_soup(res)

    html = re.sub(r'<strong>\s{0,}</strong>', r'', html)  # 空的strong标签
    html = re.sub(r'&nbsp;{2,}', r'&nbsp;', html)  # 去空格
    html = re.sub(r'\s+', r' ', html)  # 多个空格合并成一个

    save_file(html, os.path.join(html_dir, html_name))


# doc_path - word 文档地址 export_path - 导出的 html 地址
def word_to_html(doc_path, export_path):
    try:
        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(doc_path)
        doc.SaveAs(export_path, 10)
    finally:
        if('doc' in dir()) and doc.Close:
            doc.Close()
        if('word' in dir()) and word.Quit:
            word.Quit()
    f = open(export_path, 'r')
    str = f.read()
    f.close()
    return str


# 格式化html
# res - 导出的 html
def format_html(res):
    res = re.sub(r'<html.*?>', r'<!DOCTYPE html>', res)
    res = re.sub(r'\s+', r' ', res)  # 多个空格合并成一个
    res = re.sub(r'\s+>', r'>', res)  # 标签结尾的空格
    res = re.sub(r'>\s+<', r'><', res)  # 去除标签之间的空格
    res = re.sub(r'<font.*?>(.*?)<\/font>', r'\1', res)  # 去除<font></font>
    res = re.sub(r'<ins.*?<\/ins>', r'', res)  # 去除<ins></ins>
    res = re.sub(r'<u>(.*?)<\/u>', r'\1', res)  # 去除<u></u>
    res = re.sub(r'<o(.*?)<\/o.*?>', r'', res)  # 去除<o:p></o:p>
    res = re.sub(r'<b>(.*?)<\/b>', r'<strong>\1</strong>', res)
    return res

def my_beautiful_soup(html):
    soup = BeautifulSoup(html, "html5lib")

    head_tag = soup.new_tag('head')
    meta1 = soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no'})
    meta2 = soup.new_tag('meta', attrs={'content': 'text/html', 'charset': 'utf-8', 'http-equiv': 'Content-Type'})
    title = soup.new_tag('title')
    head_tag.append(meta1)
    head_tag.append(meta2)
    head_tag.append(title)
    soup.head.replace_with(head_tag)


    # 遍历节点
    for tag in soup.find_all(True):
        # 删除 class
        del tag['class']

        if not tag.get('style') is None:
            tag_style = tag['style']
            del tag['style']  # 删除元素的 style
            # 增加加粗样式
            # if ('font-weight:bold' in tag_style) and (not tag.string is None):
            #     strong_tag = soup.new_tag("strong")
            #     if 'text-decoration:underline' in tag_style:
            #         strong_tag['style'] = 'text-decoration:underline;'
            #     strong_tag.string = tag.string
            #     tag.replace_with(strong_tag)
            # 增加下划线样式
            if 'text-decoration:underline' in tag_style and (not tag.string is None):
                u_tag = soup.new_tag("u")
                u_tag['style'] = 'text-decoration:underline;'
                u_tag.string = tag.string
                tag.replace_with(u_tag)
            # 增加居中样式
            if 'text-align:center' in tag_style:
                tag['style'] = 'text-align:center;'
            # 增加右对齐样式
            elif 'text-align:right' in tag_style:
                tag['style'] = 'text-align:right;'

        # 合并相同的标签
        # if (not tag.previous_sibling is None) and (not tag.previous_sibling.string is None) and (tag.previous_sibling.name == tag.name) and (tag.previous_sibling.get('style') == tag.get('style')) and (not tag.string is None):
        #     tag.string.insert_before(tag.previous_sibling.string)
        #     if not tag.previous_sibling.name is None:
        #         tag.previous_sibling.decompose()

    # 删除span标签
    spans = soup.find_all('span')
    for span in spans:
        span.unwrap()

    # 删除i标签
    i_tags = soup.find_all('i')
    for i_tag in i_tags:
        i_tag.unwrap()

    for tag in soup.find_all(True):
        # 合并相同的标签
        if (not tag.previous_sibling is None) and (not tag.previous_sibling.string is None) and (
                tag.previous_sibling.name == tag.name) and (tag.previous_sibling.get('style') == tag.get('style')) and (
        not tag.string is None):
            tag.string.insert_before(tag.previous_sibling.string)
            if not tag.previous_sibling.name is None:
                tag.previous_sibling.decompose()

    # 删除注释
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    return str(soup).encode().decode('utf-8')

# 保存格式化好的文件
def save_file(res, html_path):
    with codecs.open(html_path, 'w+', 'utf-8') as out:
        out.write(res)
        out.close()

init()
# -*- coding: utf-8 -*-
import codecs
from win32com import client as wc
import re
import chardet
from bs4 import BeautifulSoup
import os
from html.parser import HTMLParser
globalClsList = []

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
    html_name1 = word_name.split('.')[0] + '1.html'
    html = word_to_html(os.path.join(word_dir, word_name), os.path.join(html_dir, html_name))
    res = format_html(html)
    parser = MyHTMLParser()
    parser.feed(res)
    res = str(my_beautiful_soup(res))
    # print(len(globalClsList))
    cls_list_text = ''
    for cls in globalClsList:
        # print(cls)
        cls_text = '.cls%s{%s}'%(globalClsList.index(cls), cls)
        cls_list_text = cls_list_text + cls_text
    # print(cls_list_text)
    cls_list_text = '<style>' + cls_list_text + '</style></head>'
    res = re.sub(r'(</head>)', cls_list_text, res)
    save_file(res, os.path.join(html_dir, html_name1))

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

def format_html(res):
    return res

# 格式化html
# res - 导出的 html
def format_html1(res):
    res = re.sub(r'charset=[\w\d\-]+', 'charset=utf-8', res)

    code_type = chardet.detect(res.encode('utf-8'))['encoding']
    try:
        res = res.encode('utf-8').decode(code_type)
    except UnicodeDecodeError:
        res = res.decode('gbk')

    head = r'''<head>
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no">
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    </head>
    '''
    # 去除默认生成的 style 标签
    res = re.sub(r'<style>[\s\S]*<\/style>', r'', res)
    # 去除默认生成的 xml 标签
    res = re.sub(r'<xml>[\s\S]*<\/xml>', r'', res)
    res = re.sub(code_type, r'utf-8', res) # 改编码
    # 添加meta标签
    res = re.sub(r'<head>.*?<\/head>', head, res)
    # 去掉行间样式 style
    # res = re.sub(u'style=[\w\d;\-_.\.\s;,:#\"\'%\u4e00-\u9fa5]+>', '>', res)

    # 去空 - 格式化
    # res = re.sub(r'&nbsp;', r'', res)  # 去空格
    res = re.sub(r'\s+', r' ', res)  # 多个空格合并成一个
    res = re.sub(r'\s+>', r'>', res)  # 标签结尾的空格
    res = re.sub(r'<span>\s{0,}<\/span>', r'', res)  # 空的span标签
    res = re.sub(r'>\s+<', r'><', res)  # 去除标签之间的空格
    res = re.sub(r'<font.*?>(.*?)<\/font>', r'\1', res)  # 去除<font></font>
    res = re.sub(r'<b>(.*?)<\/b>', r'\1', res)  # 去除<b></b>
    res = re.sub(r'<u>(.*?)<\/u>', r'\1', res)  # 去除<u></u>
    res = re.sub(r'<o(.*?)<\/o.*?>', r'', res)  # 去除<o:p></o:p>
    res = re.sub(r'<html.*?>(.*?)<\/html>', r'<!DOCTYPE html>\1</html>', res)
    res = re.sub(r'mso-.*?;', r'', res)  # 去除mso- 开头的属性
    res = re.sub(r'class=".*?"', r'', res)  # 去除默认添加的class
    res = re.sub('font-family:([\u4e00-\u9fa5]*?);', r'', res)  # 去除font-family: 等线;
    res = re.sub(r'(:\d*?\.\d).*?(pt;)', r'\1\2', res)  # 属性值只保留一位小数
    return res

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'style':
                if attr[1] not in globalClsList:
                    globalClsList.append(attr[1])
        # print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        pass
        # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        pass
        # print("Encountered some data  :", data)

# 合并内容相同的标签
def my_beautiful_soup(html):
    soup = BeautifulSoup(html, "html.parser")
    mso_tag = soup.find_all(style=True)
    for tag in mso_tag:
        tag_style = tag['style']
        idx = globalClsList.index(tag_style)
        tag['class'] = 'cls' + str(idx)
        del tag['style']
        if not tag.previous_sibling is None:
            if tag.previous_sibling.name == tag.name and (not tag.previous_sibling['class'] is None) and tag.previous_sibling['class'] == tag['class']:
                if (not tag.string is None) and (not tag.previous_sibling.string is None):
                    tag.string = tag.previous_sibling.string + tag.string
                    tag.previous_sibling.decompose()

    return soup

# 保存格式化好的文件
def save_file(res, html_path):
    with codecs.open(html_path, 'w+', 'utf-8') as out:
        out.write(res)
        out.close()

init()
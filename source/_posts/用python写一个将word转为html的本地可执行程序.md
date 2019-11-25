---
title: 用python写一个将word转为html的本地可执行程序
date: 2019-10-21 14:15:27
urlname: word2html
tags:
    - python
    - word2html
    - exe
---
目标：一键批量把 word 转为 html
优势：可嵌入到项目里，通过命令执行；可本地直接双击执行；可定制化；
 <!-- more -->
#### 实现思路：
1. 通过 pywin32 调用本地的 word 程序把 .docx 格式的文档转存为筛选过的网页（*.htm,*.html）
2. 用 html.parser 模块解析读取的html, 通过 re 模块的正则替换删除冗余内容，通过 bs4 模块对 html 进行其他优化处理
3. 用 codecs 模块保存优化后的 html
4. 用 pyinstaller(或cxfreeze, pyinstaller打包出的可执行程序更稳定) 将 优化后的 html 打包成 word2html.exe 可执行内容
5. 将打包后的内容放在项目目录下，并在项目目录下的 package.json 的 scripts 里配置 `start word2html.exe`，使程序可在项目中运行

#### 准备工作：
**0. python 学习**
[python文档](https://docs.python.org/zh-cn/3/)
[廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

**1. 搭建 python 环境**
window 环境下去 [官网](https://www.python.org/downloads/windows/) 下载与电脑位数匹配的 python 版本，如下，我下载的是64位的 python 3.7.5
{% asset_img 1.png This is an example image %}

命令行输入 `where python` 查询 python 安装目录并配置环境变量
{% asset_img 2.jpg This is an example image %}  
{% asset_img 3.png This is an example image %}

**2. 下载 PyCharm 方便编写 python 程序**

**3. 下载安装第三方模块 [Python Packaging User Guide](https://packaging.python.org/tutorials/)**
[pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/)
注意点：要下载python对应，与电脑位数64位相同的版本，如我下载的是：64位的，对应python3.7版本的
{% asset_img 4.png This is an example image %}

[Python 正则表达式](https://www.runoob.com/python/python-reg-expressions.html)，安装 [re](https://docs.python.org/zh-cn/3/library/re.html#re.compile)：`pip install re` 
[Beautiful Soup](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id12)
[cchardet](https://pypi.org/project/cchardet/)

**4. 安装打包插件 [cx-Freeze](https://pypi.org/project/cx-Freeze/5.0.1/)**
`pip install cx-Freeze[==版本号]`
[cx_freeze安装参考](https://blog.csdn.net/kun_dl/article/details/81223732)

**5. 代码实现**
{% link word2html https://colab.research.google.com/drive/1AwRVupBJjtXNmg519nxcIrmPjjaZdgQU [external] [title] %}
{% include_code word转html lang:python word2html.py %}
另一个版本的:
{% include_code word转html lang:python word2html2.py %}

**6. 其他**
[用python创建 docx 文件](https://www.cnblogs.com/deepwaterplan/articles/6664796.html)
[别人用js实现的word2html](https://github.com/wibetter/word2html)
[python-docx](https://python-docx.readthedocs.io/en/latest/index.html)
[mammoth.js](https://www.cnblogs.com/fhkankan/p/11136238.html)
{% include_code 使用BeautifulSoup删除html中的script lang:python removeScript.py %}
{% include_code 使用BeautifulSoup删除html中的注释 lang:python removeComment.py %}
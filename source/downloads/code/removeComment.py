#! /usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup, Comment
data = """<div class="foo">
cat dog sheep goat
<!--
<p>test</p>
-->
</div>"""

soup = BeautifulSoup(data)

for element in soup(text=lambda text: isinstance(text, Comment)):
    element.extract()

print soup.prettify()

# 输出结果：
# <div class="foo">
#  cat dog sheep goat
# </div>
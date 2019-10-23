#! /usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
html = '''
<script>a</script>
baba
<script>b</script>
<h1>hi, world</h1>
'''
soup = BeautifulSoup('<script>a</script>baba<script>b</script><h1>')
[s.extract() for s in soup('script')]
# 或者： [s.extract() for s in soup.findAll('script')]
print soup

# 输出
# baba<h1></h1>
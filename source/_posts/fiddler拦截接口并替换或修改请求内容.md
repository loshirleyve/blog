---
title: fiddler拦截接口并替换或修改请求内容
date: 2019-09-20 15:43:20
urlname: fiddler拦截接口
categories:
    - 日常问题解决分享
tags:
    - 开发调试
    - fiddler
    - 抓包
---
## 问题背景
项目上线，界面显示异常，通过定位发现是接口返回不符合预期。
 <!-- more -->

问题一：修改接口返回，界面能正常显示了吗？

问题二：接口返回不合预期，是不是因为请求参数不对？

## 解决问题
对问题一，拦截接口返回，并修改接口返回，看界面是否能正常显示；

对问题二，拦截接口请求，修改接口请求参数，看接口返回能否正常。

## 方法步骤
对问题一，在 fiddler 下的控制台输入 `bpafter 接口请求地址` + `Enter` 拦截到请求返回后，修改返回内容。执行步骤如下：
<iframe height=498 width=1080 src='http://player.youku.com/embed/XNDM2ODk5MTMxMg==' frameborder=0 'allowfullscreen'></iframe>

[拦截请求返回并修改](https://pan.baidu.com/s/1Ls86DVls4lAjKL5c-Zgnmg)

对问题二，在 fiddler 下的控制台输入 `bpu 接口请求地址` + `Enter` 拦截到请求发出后，修改请求的内容。执行步骤同上

<iframe style="margin-left: 2px; margin-bottom:-5px;" frameborder="0" scrolling="0" width="100px" height="20px" src="https://ghbtns.com/github-btn.html?user=loshirleyve&repo=loshirleyve.github.io&type=star&count=true">
</iframe>
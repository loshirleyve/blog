---
title: day4
date: 2018-06-05 08:59:33
tags:
    - 每日清单
---
| 条目  | 备注 |
| :--: | :--: |
| 技术学习 | ✔ |
| 运动 | ✔ |
| 看书 | ✘ |
| 生活学习 | ✔ |
| 英语 | ✔ |

<!-- more -->

| 条目  | 时间 | 时长   | 备注 |
| :--: | :--: | :--: | :--: |
| 看连岳公号 |08:56-09:05  | 9 min  |     |
| 看前端早读课及剖析vue.js |09:06-11:11  | 125 min  |     |


>### ask about vue.js
>+ Vue.js 究竟是如何在我们对数据进行操作的时候影响视图的呢？
>+ 修改的数据如何批量高效地映射到视图上呢？
>+ 传统的 DOM 操作又在何时进行的呢？

<br/>

>### 资源
>+ https://source.unsplash.com/  | https://unsplash.com/ 高质量图片网
>+ https://fonts.google.com 字体资源网

<br/>

### 代码片段

    // Animate Smooth Scroll
    $('#view-work').on('click', function() {
        const images = $('#images').position().top;

        $('html, body').animate(
            {
                scrollTop: images
            },
            900
        );
    });

<br/>

### 一个简单的，响应式的图片网站

用到的资源：
+ 高质量图片网: https://source.unsplash.com/  | https://unsplash.com/
+ 字体资源网: https://fonts.google.com
+ jQuery3: http://code.jquery.com/

达到效果：
+ 每次刷新页面会加载不同的图片，但是首屏图片不变
+ 在 pc 和 mobile 端能实现响应式布局
<iframe width="100%" height="500" src="//jsfiddle.net/liewshirley/6ay5rcjv/8/embedded/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

<br/>

### Build a Responsive Grid CSS Website Layout From Scratch
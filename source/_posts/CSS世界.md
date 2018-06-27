---
title: CSS世界
date: 2018-06-15 10:58:36
tags:
categories:
    - css
    - book
---

### CSS 世界的“世界观”

CSS 特性之间的相互联系和具象关系。
在 CSS 这个世界中，CSS 并不是一个机械枯燥的语言，所有属性都是有血有肉、有着不同个性和身世的个体。不同的个体可以碰撞出不同的火花，激荡出异彩纷呈的故事。
<!-- more -->
<img src="./image.png" width=640 height=1300>
从上面的描述可以看出，在 CSS 世界中，HTML 是魔法石，选择器就是选择法器，CSS 属性就是魔法师，CSS 各种属性值就是魔法师的魔法技能，浏览器就是他们所在的“王国”，“王国”会不断更新法律法规（版本升级），决定是否允许使用新的魔法石（HTML5 新标签新属性），是否允许新的魔法师入“国籍”（CSS3 新属性），或者允许魔法师使用某些新技能（CSS 新的属性值），以及是否舍弃某些魔法技能（如 display:run-in）；操作系统就是他们所在的世界，不同的操作系统代表不同的平行世界，所以，CSS 世界有这么几个比较大的平行世界，即 Windows 世界、OS X 世界以及移动端的 iOS 世界和 Android 世界。不同世界的浏览器王国的命运不一样，例如，在 OS X 世界中，IE王国是不存在的，而 Safari 王国却异常强大，但在 Windows 世界中，Safari 王国却异常落寞。
以上这一切就构成了完整的 CSS 世界的“世界观”。
>CSS 世界的诞生就是为图文信息展示服务的。

### CSS 变量 currentColor 可用来改变图标颜色

### CSS 实现凹凸形状 -- 利用 CSS "首选最小宽度" 特点
```
.ao {
    display: inline-block;
    width: 0;
}
.ao:before {
    content: 'love你love';
    outline: 2px solid #cd0000;
    color: #fff;
}
```
<iframe width="100%" height="300" src="//jsfiddle.net/liewshirley/w8b07fzL/1/embedded/html,css,result/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

### box-sizing 被发明出来的最大的初衷是解决替换元素宽度自适应的问题。
```
input, textarea, img, video, object {
    box-sizing: border-box;
}
```

### CSS 实现动态正在加载中...
<iframe width="100%" height="300" src="//jsfiddle.net/liewshirley/brumtp6k/5/embedded/html,css,result/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

### margin 属性的 auto 计算是为块级元素左中右对齐而设计的
如果想要某个块状元素右对齐，脑子里不要就一个 float: right， 很多时候， margin-left: auto 才是最佳的实践

### vertical-align
vertical-align 支持数值，且支持负数
vertical-align 起作用是有前提条件的，这个前提条件就是：只能应用于内联元素以及 display 值为 table-cell 的元素。

### 一套基于 20px 图标对齐的处理技巧
该技巧有下面 3 个要点：
（1）图标高度和当前行高都是 20px。很多小图标背景合并工具都是图标宽高多大生成的CSS 宽高就是多大，这其实并不利于形成可以整站通用的 CSS 策略，我的建议是图标原图先扩展成统一规格，比方说这里的 20px×20px，然后再进行合并，可以节约大量 CSS 以及对每个图标对齐进行不同处理的开发成本。
（2）图标标签里面永远有字符。这个可以借助:before 或:after 伪元素生成一个空格字符轻松搞定。
（3）图标 CSS 不使用 overflow:hidden 保证基线为里面字符的基线，但是要让里面潜在的字符不可见。
<iframe width="100%" height="300" src="//jsfiddle.net/liewshirley/brumtp6k/5/embedded/html,css,result/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

### 基于 vertical-align 属性的水平垂直居中弹框
<iframe width="100%" height="300" src="//jsfiddle.net/liewshirley/54rL9q3j/10/embedded/html,css,result/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>


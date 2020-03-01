"#blog" 
#线上访问地址https://loshirleyve.github.io/
生成的文件地址：https://github.com/loshirleyve/loshirleyve.github.io

#初始化git上的blog步骤

###1，下载 blog 资源 
（项目地址：https://github.com/loshirleyve/blog）

    git clone git@github.com:loshirleyve/blog.git

###2，安装 Hexo 并更新依赖
    npm install hexo-cli -g
    cd blog
    npm install

###3，下载定制主题，即 blog 配置文件 
（项目地址：https://github.com/loshirleyve/hexo-theme-yilia）

    hexo clean
    git clone git@github.com:loshirleyve/hexo-theme-yilia.git themes/yilia
    cd themes/yilia
    git pull
    
###4，本地启动
    hexo g (generate) # 生成
    hexo s (server) # 启动本地web服务器
    
#写 blog 步骤
    $ hexo new "postName" #新建文章
    $ hexo new page "pageName" #新建页面

#blog 发布步骤
    $ hexo d -g #生成部署
    $ hexo s -g #生成预览
    
#常用简写
    $ hexo n == hexo new
    $ hexo g == hexo generate
    $ hexo s == hexo server
    $ hexo d == hexo deploy
    
#Hexo博客中插入音乐/视频
[两个好用的hexo插件](https://www.jianshu.com/p/26a7fc7cc185)：

* hexo-tag-aplayer：https://github.com/grzhan/hexo-tag-aplayer)
* hexo-tag-dplayer： https://github.com/NextMoe/hexo-tag-dplayer
```
// npm install hexo-tag-aplayer
{% aplayer "她的睫毛" "周杰伦" "http://home.ustc.edu.cn/~mmmwhy/%d6%dc%bd%dc%c2%d7%20-%20%cb%fd%b5%c4%bd%de%c3%ab.mp3"  "http://home.ustc.edu.cn/~mmmwhy/jay.jpg" "autoplay=false" %}

// npm install hexo-tag-dplayer
{% dplayer "url=http://home.ustc.edu.cn/~mmmwhy/GEM.mp4"  "pic=http://home.ustc.edu.cn/~mmmwhy/GEM.jpg" "loop=yes" "theme=#FADFA3" "autoplay=false" "token=tokendemo" %}
```

#hexo文档
https://hexo.io/zh-cn/docs

# 七牛云地址
https://portal.qiniu.com/kodo/bucket/resource?bucketName=liewshirley

# 在线音频压缩：https://www.compresss.com/cn/compress-audio.html
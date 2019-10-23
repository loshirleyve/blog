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
#hexo文档
https://hexo.io/zh-cn/docs
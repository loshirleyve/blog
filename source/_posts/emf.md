---
emf 记日记：
desc: 查看文件路径 {% asset_path final_audio.mp3 %} 得到 "/2019/11/11/emf20191111/final_audio.mp3"
1，hexo new "emf20191111" 新建 post 文章，复制前一篇内容
2，复制 emf20191111 的文件夹路径
3，windows 版微信打开 EMF，保存图片到 emf20191111 的文件夹路径
4，手机打开 emf，fiddler 抓包
5，fiddler 上全选请求列表 - 右键 - copy - just url
6，在chrome 浏览器控制台输入 aaa = [...(new Set(`url`.split('\n')))].filter(item => item.indexOf('.mp3')>-1); 
7，把得到的 url 列表复制到 downloadfile.py 里
8，执行 npm run downloadfile.py，生成合成的 final_audio.mp3
---
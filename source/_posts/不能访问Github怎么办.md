---
title: 不能访问Github怎么办?
date: 2021-10-18 21:53:36
urlname:
tags:
---

前提：不能开VPN，比如 chrome的vpn插件，公司的vpn登录

## 一、确定ip  https://websites.ipaddress.com/github.com
查看GitHub的ip地址。
[](https://raw.githubusercontent.com/loshirleyve/images/main/github.png?token=ADCW5YXXVETSWLGAHBZC3WDBNV7HO)

## 二、确定域名ip https://websites.ipaddress.com/github.global.ssl.fastly.net
[](https://github.com/loshirleyve/images/blob/main/fastlynet.png?raw=true)

## 三、确定静态资源ip https://github.com.ipaddress.com/assets-cdn.github.com
[](https://github.com/loshirleyve/images/blob/main/assetscdn.png?raw=true)

## 四、修改hosts文件

### mac系统：
1. 打开终端
2. 输入sudo vi /etc/hosts
3. 输入密码
4. 进入文件hosts，然后按“i”，进入编辑模式
5. 把你的host添加到最后
   [](https://raw.githubusercontent.com/loshirleyve/images/main/mac1.png?token=ADCW5YVAADI3AFK6KC2B2RDBNWB2E)

    ```
    ##
    # Github
    ##
    151.101.44.240 github.global.ssl.fastly.net
    192.30.255.112 github.com
    199.232.28.133 assets-cdn.github.com
    185.199.109.153 documentcloud.github.com
    192.30.253.119 gist.github.com
    185.199.110.154 help.github.com
    140.82.114.10 nodeload.github.com
    151.101.0.133 raw.github.com
    185.199.108.153 githubstatus.com
    140.82.114.17 training.github.com
    199.232.28.133 raw.githubusercontent.com
    199.232.28.133 gist.githubusercontent.com
    199.232.28.133 cloud.githubusercontent.com
    199.232.28.133 camo.githubusercontent.com
    199.232.28.133 avatars0.githubusercontent.com
    199.232.28.133 avatars1.githubusercontent.com
    199.232.28.133 avatars2.githubusercontent.com
    199.232.28.133 avatars3.githubusercontent.com
    199.232.28.133 avatars4.githubusercontent.com
    199.232.28.133 avatars5.githubusercontent.com
    199.232.28.133 avatars6.githubusercontent.com
    199.232.28.133 avatars7.githubusercontent.com
    199.232.28.133 avatars8.githubusercontent.com
    192.30.253.120 codeload.github.com

    140.82.114.3 github.com
    199.232.69.194 github.global.ssl.fastly.net
    185.199.108.153 assets-cdn.github.com
    185.199.109.153 assets-cdn.github.com
    185.199.110.153 assets-cdn.github.com
    185.199.111.153 assets-cdn.github.com
    ```
6. control+c退出出编辑模式
7. 输入:wq，保存退出
8. 刷新网络 DNS 缓存：
   sudo killall -HUP mDNSResponder
   sudo dscacheutil -flushcache

### Windows 系统：
1. 打开C:\Windows\System32\drivers\etc
2. windows下刷新DNS的方法： ``` ipconfig /flushdns ```
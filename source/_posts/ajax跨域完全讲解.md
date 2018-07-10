---
title: ajax跨域完全讲解
date: 2018-07-10 15:00:21
tags:
---

### ajax 跨域原因：
1. 浏览器限制 （chrome --disable-web-security --user-data-dir=e:\temp3）
2. 跨域
3. XHR [XMLHttpRequest] (JSONP 解决)

<!-- more -->

#### JSONP 有什么弊端
+ 服务器需要改动代码支持
+ 只支持 GET 请求
+ 发送的不是 XHR 请求 （不支持异步及各种事件）

#### 跨域解决方向
+ 被调用方解决 （设置 header，允许跨域）
    + 服务器端实现
    + NGINX 配置
    + APACHE 配置
    ```
        header("Access-Control-Allow-Origin: *")
        header("Access-Control-Allow-Methods: *")
        header("Access-Control-Allow-Headers: Content-Type") // 针对预检命令
        header("Access-Control-Max-Age: 3600") // 针对预检命令缓存，单位是秒
    ```
+ 调用方解决 （设置代理访问，隐藏跨域）


#### 简单请求和非简单请求
+ 定义
+ OPTIONS 预检命令
+ OPTIONS 预检命令缓存

##### 工作中比较常见的【简单请求】：
方法为：
+ GET
+ HEAD
+ POST
<br/>

请求 header 里面
+ 无自定义头
+ Content-Type 为以下几种：
    + text/plain
    + multipart/form-data
    + application/x-www-form-urlencoded

***

##### 工作中常见的【非简单请求】有：
+ put, delete 方法的 ajax 请求
+ 发送 json 格式的 ajax 请求
+ 带自定义头的 ajax 请求

### 带 cookie 的跨域
+ 带 cookie 的时候， origin 必须是全匹配，不能用 *
    ```
    header("Access-Control-Allow-Origin: http://localhost:8081")
    ```
+ 要新加一个头
    ```
    header("Access-Control-Allow-Credentials: true")
    ```
```
    // 带 cookie 的 $.ajax 请求需要配置
    xhrFields: {
        withCredentials: true
    }
```

注： 可以通过 document.cookie 来设置和获取 cookie | cookie 要加在被调用方，因为网络请求里面你要读的 cookie 只能读到本域的

### 带自定义头的跨域
```
    // 带自定义头的 $.ajax 请求需要配置
    headers: {
        "x-header1": "AAA"
    }
    // 或者
    beforeSend: function(xhr) {
        xhr.setRequestHeader("x-header2", "BBB")
    }
```

后台需要配置：
```
header("Access-Control-Allow-Headers: Content-Type, x-header1, x-header2")
```

后台代码逻辑可以为：取到 Access-Control-Allow-Headers 不为空的话，就设置
```
String headers = req.getHeader("Access-Control-Allow-Headers");
if(!isEmpty(headers)){
    header("Access-Control-Allow-Headers: " + headers)
}
```


## 被调用方 - nginx 解决跨域
```
server{
    listen 80;
    server_name b.com;

    location /{
        proxy_pass http://localhost:8080/;

        add_header Access-Control-Allow-Methods *;
        add_header Access-Control-Max-Age 3600;
        add_header Access-Control-Allow-Credentials true;

        add_header Access-Control-Allow-Origin $http_origin;
        add_header Access-Control-Allow-Headers $http_access_control_allow_headers;

        if ($request_method = OPTIONS){
            return 200;
        }
    }
}
```

## 被调用方 - APACHE 解决方案
```
// 需要打开虚拟主机的相关配置
LoadModule vhost_alias_module modules/mod_vhost_alias.so

Include conf/extra/httpd-vhosts.conf

LoadModule proxy_module modules/mod_proxy.so

LoadModule proxy_http_module modules/mod_proxy_http.so

LoadModule headers_module modules/mod_headers.so

LoadModule rewrite_module modules/mod_rewrite.so
```

```
// httpd-vhosts.conf

<VirtualHost*:80>
    ServerName b.com
    ErrorLog "logs/b.com-error.log"
    CustomLog "logs/b.com-access.log" common
    ProxyPass/ http://localhost:8080/

    # 把请求头的 origin 值返回到 Access-Control-Allow-Origin 字段
    Header always set Access-Control-Allow-Origin "expr=%{req:origin}"

    # 把请求头的 Access-Control-Request-Headers 值返回到 Access-Control-Request-Headers 字段
    Header always set Access-Control-Allow-Headers "expr=%{req:Access-Control-Allow-Headers}"

    Header always set Access-Control-Allow-Methods "*"
    Header always set Access-Control-Allow-Credentials "true"
    Header always set Access-Control-Max-Age "3600"

    # 处理预检命令 OPTIONS， 直接返回 204
    RewriteEngine On
    RewriteCond %{REQUEST_METHOD} OPTIONS
    RewriteRule ^(.*)$ "/" [R=204,L]
</VirtualHost>
```

## 被调用方 - SPRING 框架解决方案
增加 @CrossOrigin 注解（可以加在类上面，也可以加在具体的方法上面）

## 调用方解决 - 隐藏跨域
通过调用方的 http 服务器的反向代理转发到被调用方的服务器，在浏览器上看不到任何跨域请求

反向代理（简单来说就是：同一个域名的两个不同的 URL，它最后会去到两个不同的服务器）

隐藏跨域与通过被调用方解决方案相比，调用方解决方案时，调用的接口都是本域的，所以调用接口的 URL 都是相对地址

```
// NGINX 的配置
server{
    listen 80;
    server_name a.com;

    location /{
        proxy_pass http://localhost:8081/;
    }

    location /ajaxserver{
        proxy_pass http://localhost:8080/test/;
    }
}
```
```
// APACHE 的配置
<VirtualHost*:80>
    ServerName a.com
    ErrorLog "logs/a.com-error.log"
    CustomLog "logs/a.com-access.log" common

    ProxyPass /ajaxserverapache http://localhost:8080/test
    ProxyPass / http://localhost:8081/
</VirtualHost>
```
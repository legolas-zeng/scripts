##### 下载主题
> git clone https://github.com/alehaa/nginx-fancyindex-flat-theme.git

##### 安装插件
 > npm install -g uglify-js
 
 > npm install less@1.6.2 -g
 
 > npm install clean-css
 
 ##### 开始编译
  > cd nginx-fancyindex-flat-theme
  
  > make
  
 ##### 安装fancyindex
 
 > ./configure --prefix=/usr/local/nginx --add-module=/data/ngx-fancyindex-master
 
 > cd /data
 
 > git clone https://github.com/TheInsomniac/Nginx-Fancyindex-Theme.git
 
 ##### 配置nginx
 
```
 server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location /download {
            root  /ftpfile;
            autoindex on;
            charset utf-8,gbk;
            autoindex_exact_size off;         #关闭详细文件大小统计，让文件大小显示MB，GB单位，默认为b；
            autoindex_localtime on;           #开启以服务器本地时区显示文件修改日期！
            include  /data/Nginx-Fancyindex-Theme/fancyindex.conf;
            #index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
```

再把相应的静态文件拷贝到`/usr/local/nginx/html/theme` 即可。
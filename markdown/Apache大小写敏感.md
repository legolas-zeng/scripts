今天部署了一个静态网页index.html，用的Apache，不为啥，就因为静态网站的文件中有中文路径，nginx对中文支持不是很好。所以改用Apache

#### 安装Apache
> yum install httpd -y

### 修改配置
> vim /etc/httpd/conf/httpd.conf

> `LoadModule speling_module     modules/mod_speling.so`

> 在`Directory`中加入`CheckSpelling On`

`mod_speling.so`模块在`/etc/httpd/modules`目录下，如果有报错的话，现在看下这个模块在不在。

### 设置路径
就用httpd的默认路径吧`DocumentRoot "/var/www/html"`，把静态文件全部放到html目录下。
重启Apache.....
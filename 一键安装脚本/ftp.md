http://www.louisvv.com/archives/1635.html

##### 1.使用yum安装vsftpd
```shell script
[root@localhost ~]# yum install vsftpd
Installed:
  vsftpd.x86_64 0:3.0.2-22.el7                                                                                                                                                                                    
Complete!
```
##### 2.修改vsftpd配置文件
```shell script
[root@localhost ~]# vim /etc/vsftpd/vsftpd.conf 
```
```shell script
[root@localhost ~]# cat /etc/vsftpd/vsftpd.conf |grep ^[^#]
anonymous_enable=NO    #不允许匿名登录
local_enable=YES    #vsftpd所在系统的用户可以登录vsftpd 
write_enable=YES        #允许使用任何可以修改文件系统的FTP的指令 
local_umask=022        #匿名用户新增文件的umask数值
dirmessage_enable=YES    
xferlog_enable=YES        #启用一个日志文件，用于详细记录上传和下载
connect_from_port_20=YES        #开启20端口    
xferlog_std_format=YES        #记录日志使用标准格式 
listen=NO         #关闭监听
listen_ipv6=YES    #监听IPV6地址
pam_service_name=vsftpd     #验证文件的名字
userlist_enable=YES    #允许由userlist_file指定文件中的用户登录FTP服务器
tcp_wrappers=YES    #支持tcp_wrappers,限制访问(/etc/hosts.allow,/etc/hosts.deny)
```

##### 3.添加ftp用户，设置主目录，不允许使用shell
```shell script
[root@localhost mail]# useradd -d /data/ftp/huoyan -s /sbin/nologin ftpuser
```
##### 5.配置chroot

```shell script
[root@localhost mail]# vim /etc/vsftpd/vsftpd.conf 
chroot_local_user=NO
chroot_list_enable=YES
# (default follows)
chroot_list_file=/etc/vsftpd/chroot_list
```
##### 6.创建chroot_list
```shell script
[root@localhost ftp]# vim /etc/vsftpd/chroot_list
ftpuser
```
##### 7.重启服务，并将服务设置为开机自启
```shell script
[root@localhost ~]# systemctl start  vsftpd.service
[root@localhost ~]# systemctl enable vsftpd.service
```

#! /bin/bash
hostname=`hostname`
zabbix_file=zabbix-3.4.4.tar.gz

########### 同步zabbix ##############
#yum install -y wget pcre-devel
#if [ ! -f $zabbix_file ]; then
#	echo "-------------开始下载zabbix安装包-------------"
#	wget http://downloads.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/3.4.4/zabbix-3.4.4.tar.gz
#fi


mkdir -p /data/zabbix
echo "-------------- 同步zabbix软件------------------" > /etc/rsync_manager_passwd.txt
chmod 600 /etc/rsync_manager_passwd.txt
rsync -avz --delete --password-file=/etc/rsync_manager_passwd.txt --port=873 tongbu@192.168.3.10::zabbix /data/zabbix

echo "-------------- 开始创建zabbix用户------------------"
echo "创建zabbix用户"
groupadd zabbix
useradd -g zabbix zabbix

echo "------------- 开始安装必需软件 ----------------"
yum -y install curlcurl-devel net-snmp snmp net-snmp-devel libssh2-devel

echo "-------------- 开始安装mysql ------------------"
# wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-x86_64.tar.gz
rsync -avz --delete --password-file=/etc/rsync_manager_passwd.txt --port=873 tongbu@192.168.3.10::mysql /data/zabbix

echo "-------------- 开始安装php ------------------"
yum install epel-release
rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
#rpm -Uvh http://mirrors.isu.net.sa/pub/fedora/fedora-epel/7/x86_64/e/epel-release-7-6.noarch.rpm
yum -y install gcc gcc++ gcc-c++ wget make libxml2 libxml2-devel openssl  openssl-devel curl-devel libjpeg-devel libpng-devel freetype-devel bison autoconf
yum -y install patch php-xml unixODBC unixODBC-devel  php-xmlrpc php-mbstring php-mhash patch java-devel wget unzip libxml2 libxml2-devel httpd mariadb mariadb-devel mariadb-server php php-mysql php-common php-mbstring php-gd php-odbc php-pear curl curl-devel net-snmp net-snmp-devel perl-DBI php-xml ntpdate  php-bcmath zlib-devel glibc-devel curl-devel gcc automake libidn-devel openssl-devel net-snmp-devel rpm-devel OpenIPMI-devel
echo "-------------- 设置php.ini相关参数 ------------------"
cp /etc/php.ini /etc/php.ini.zabbixbak
sed -i 's/max_execution_time = 30/max_execution_time = 300/g' /etc/php.ini
sed -i '/max_input_time =/s/60/300/' /etc/php.ini
sed -i '/mbstring.func_overload = 0/a\mbstring.func_overload = 1' /etc/php.ini
sed -i '/post_max_size =/s/8M/32M/' /etc/php.ini
sed -i '/;always_populate_raw_post_data = -1/a\always_populate_raw_post_data = -1' /etc/php.ini
sed -i '/;date.timezone =/a\date.timezone = Asia/Shanghai' /etc/php.ini

#yum -y install nginx php php-fpm php-cli php-common php-gd php-mbstring php-mcrypt php-mysql php-pdo php-devel php-imagick php-xmlrpc php-xml php-bcmath php-dba php-enchant php-yaf
echo "---------开始解压安装包-----------"
cd /data/zabbix
tar -zxvf zabbix-3.4.4.tar.gz
cd zabbix-3.4.4
./configure --prefix=/usr/local/zabbix --enable-server --enable-agent --with-mysql --enable-ipv6 --with-net-snmp --with-libcurl --with-libxml2
make && make install
echo "---------开始拷贝php静态文件----------"
cd frontends/php
mkdir /home/zabbix -p
cp * -rf /home/zabbix

echo "------------修改zabbix配置文件---------------"


echo "------------导入zabbix数据库-----------------"

create database zabbix default charset utf8 COLLATE utf8_general_ci;
mysql -uzabbix -pzabbix zabbix < schema.sql




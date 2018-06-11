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
echo "rsync" > /etc/rsync_manager_passwd.txt
chmod 600 /etc/rsync_manager_passwd.txt
rsync -avz --delete --password-file=/etc/rsync_manager_passwd.txt --port=873 tongbu@192.168.3.10::zabbix /data/zabbix

#  echo "------------- 开始安装必需软件 ----------------"
yum -y install curlcurl-devel net-snmp snmp net-snmp-devel libssh2-devel

# echo "-------------- 开始安装mysql------------------"
rsync -avz --delete --password-file=/etc/rsync_manager_passwd.txt --port=873 tongbu@192.168.3.10::mysql /data/zabbix

# echo "-------------- 开始安装php--------------------"
yum install epel-release
rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
yum -y install gcc gcc++ gcc-c++ wget make libxml2 libxml2-devel openssl  openssl-devel curl-devel libjpeg-devel libpng-devel freetype-devel bison autoconf

yum -y install nginx php php-fpm php-cli php-common php-gd php-mbstring php-mcrypt php-mysql php-pdo php-devel php-imagick php-xmlrpc php-xml php-bcmath php-dba php-enchant php-yaf
echo "---------开始解压安装包-----------"
cd /data/zabbix
tar -zxvf zabbix-3.4.4.tar.gz
cd zabbix-3.4.4


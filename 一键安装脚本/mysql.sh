#!/bin/bash

yum install libaio -y
yum install numactl.x86_64 -y

name_tar='mysql-5.7.19-linux-glibc2.12-x86_64.tar.gz'
cd /usr/local/src

if [ ! -f $name_tar ]; then
    wget https://dev.mysql.com/get/Downloads/MySQL-5.7/$name_tar
fi
rm -rf ../mysql
mkdir ../mysql
tar -zxvf $name_tar -C ../mysql --strip-components 1

groupadd mysql
useradd -r -g mysql -s /bin/false mysql

cd /usr/local/mysql
chown -R mysql:mysql ./*
rm -rf /etc/my.cnf

#bin/mysqld \
#--initialize \
#--user=mysql \
#--explicit_defaults_for_timestamp \
#--basedir=/usr/local/mysql \
#--datadir=/usr/local/mysql/data/ \
#--socket=/usr/local/mysql/data/mysql.sock \
#--pid-file=/usr/local/mysql/data/mysql.pid \
#--plugin-dir=/usr/local/mysql/lib/plugin \
#--log-error=/usr/local/mysql/data/mysql.err

#bin/mysqld \
#--user=mysql \
#--explicit_defaults_for_timestamp \
#--basedir=/usr/local/mysql \
#--datadir=/usr/local/mysql/data/ \
#--socket=/usr/local/mysql/data/mysql.sock \
#--pid-file=/usr/local/mysql/data/mysql.pid \
#--plugin-dir=/usr/local/mysql/lib/plugin \
#--log-error=/usr/local/mysql/data/mysql.err

bin/mysqld --user=mysql --initialize --explicit_defaults_for_timestamp
support-files/mysql.server start

ln -s /usr/local/mysql/support-files/mysql.server  /etc/init.d/mysql
ln -s /usr/local/mysql/bin/mysql /usr/local/bin/mysql

#用mysql初始化给的密码登录，并修改密码
#set  password = password('xxx');

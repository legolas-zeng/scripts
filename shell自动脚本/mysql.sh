#!/bin/bash

yum install libaio -y
yum install numactl.x86_64 -y

name_tar='mysql-5.7.19-linux-glibc2.12-x86_64.tar.gz'
cd /usr/local/src

if [ ! -f $name_tar ]; then
    wget https://dev.mysql.com/get/Downloads/MySQL-5.7/$name_tar
fi

tar -zxvf mysql-5.7.19-linux-glibc2.12-x86_64.tar.gz
mv mysql-5.7.19-linux-glibc2.12-x86_64 /usr/local/mysql
useradd mysql
groupadd mysql

cd /usr/local/mysql
chown -R mysql:mysql /usr/local/mysql
rm -rf /etc/my.cnf

./bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql
support-files/mysql.server start

ln -s /usr/local/mysql/support-files/mysql.server  /etc/init.d/mysql
ln -s /usr/local/mysql/bin/mysql /usr/local/bin/mysql

#用mysql初始化给的密码登录，并修改密码
#set  password = password('xxx');

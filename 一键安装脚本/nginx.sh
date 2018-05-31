#!/bin/bash

if [ -z $1 ]; then
    version=1.10.2
else
    version=$1
fi

name=nginx-${version}
name_tar=${name}.tar.gz
target_dir=/usr/local/nginx
target_dir_bak=/usr/local/nginx_bak


if [ -d $target_dir ]; then
    echo "${target_dir}存在, 备份${target_dir}"
    rm -rf $target_dir_bak
    mv $target_dir $target_dir_bak
fi

cd /data/yunwei/software

if [ ! -f $name_tar ]; then
    echo "下载nginx文件"
    wget http://nginx.org/download/${name_tar}
fi

if [ ! -f $name_tar ]; then
    echo "${name_tar} not exists and upload error"
    exit 1
fi

echo "nginx ${version} 开始安装"
#yum -y update 不更新

yum install -y gcc automake autoconf libtool gcc-c++

yum install -y gd zlib zlib-devel openssl openssl-devel libxml2 libxml2-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libmcrypt libmcrypt-devel bzip2 bzip2-devel curl curl-devel pcre pcre-devel

if [ -d $name ]; then
    cd $name
    make clean
else
    tar -zxvf $name_tar
    cd $name
fi

# useradd wwwroot
./configure --prefix=$target_dir --user=wwwroot --group=wwwroot --with-stream
make && make install

rm -rf /usr/local/sbin/nginx
rm -rf /usr/sbin/nginx
rm -rf /etc/nginx

ln -s ${target_dir}/sbin/nginx /usr/local/sbin/nginx
ln -s ${target_dir}/sbin/nginx /usr/sbin/nginx
ln -s ${target_dir}/conf /etc/nginx

cd /etc/init.d
rm -rf nginx
wget http://doc.ranlau.com/nginx -O nginx
# http://nginx.org/download/1.10.2.tar.gz
chmod a+x nginx
chkconfig --add /etc/init.d/nginx
chkconfig nginx on

cd ${target_dir}/conf
mkdir vhosts
cd vhosts


echo "------------nginx安装完成---------------"

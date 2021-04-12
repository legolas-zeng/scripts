#!/bin/bash

read -p "请输入要安装的php版本号（默认5.6版本请回车）：" phpversion
if  [ ! -n "$phpversion" ] ;then
    echo "默认版本是5.6.0"
    phpversion=5.6.0
fi

read -p "您要安装的版本号是:$phpversion，确定？（y/n）" input

case $input in
    [yY][eE][sS]|[yY])
		echo "Yes"
		;;
    [nN][oO]|[nN])
		echo "No"
       		;;
    *)
	echo "取消安装......"
	exit 1
	;;
esac

# 变量
name=php-${version}
name_tar=${name}.tar.gz
target_dir=/usr/local/php
target_dir_bak=/usr/local/php_bak

if [ -d $target_dir ]; then
    echo "${target_dir}存在"
    rm -rf $target_dir_bak
    mv $target_dir $target_dir_bak
fi

cd /usr/local/src

if [ ! -f $name_tar ]; then
    echo "下载php文件"
    #wget http://am1.php.net/get/${name_tar}/from/this/mirror -O $name_tar
    #wget http://cn2.php.net/distributions/php-7.2.2.tar.gz
    # 国内搜狐镜像源
    wget http://mirrors.sohu.com/php/${name_tar} -O $name_tar
    #a=$?
    #echo $a
    if [ $? -ne 0 ];then
       echo "版本号$phpversion 没有找到"
       exit 1
    fi
fi

if [ ! -f $name_tar ]; then
    echo "${name_tar} not exists and upload error"
    exit 1
fi

echo "php ${version} begin install"

yum update -y
yum install -y gcc automake autoconf libtool gcc-c++
yum install -y epel-release
yum install -y gd zlib zlib-devel openssl openssl-devel libxml2 libxml2-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libmcrypt libmcrypt-devel bzip2 bzip2-devel curl curl-devel



if [ -d $name ]; then
    cd $name
    make clean
else
    tar -zxvf $name_tar
    cd $name
fi

# centos6.8不支持--with-fpm-systemd，可以尝试在7以上的系统添加
# --enable-intl 需要安装ICU yum install -y libicu libicu-devel

./configure --prefix=$target_dir \
--enable-fpm \
--with-fpm-user=wwwroot \
--with-fpm-group=wwwroot \
--with-gd \
--with-freetype-dir \
--with-jpeg-dir \
--enable-gd-native-ttf \
--enable-gd-jis-conv \
--enable-mysqlnd \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--enable-opcache \
--with-openssl \
--with-mcrypt \
--with-curl \
--enable-mbstring \
--enable-zip \
--with-zlib \
--enable-sockets \
--with-gettext


make && make install

cp /usr/local/src/${name}/php.ini-production ${target_dir}/lib/php.ini
cp ${target_dir}/etc/php-fpm.conf.default ${target_dir}/etc/php-fpm.conf
cp ${target_dir}/etc/php-fpm.d/www.conf.default ${target_dir}/etc/php-fpm.d/www.conf

ln -s ${target_dir}/bin/php /usr/local/sbin/php
ln -s ${target_dir}/bin/phpize /usr/local/sbin/phpize
ln -s ${target_dir}/bin/php-config  /usr/local/sbin/php-config

#vim php.ini 将date.timezone设置为PRC
echo "安装成功,请自行配置时区(PRC)，并选择安装redis\swoole\opcache等扩展，客户端升级项目需要配置post_max_size和upload_max_filesize参数，开启opcache需要配置相关参数"


# 重启php-fpm
# ps aux|grep php-fpm|grep -v grep|awk '{print $2}' | xargs kill -SIGUSR2


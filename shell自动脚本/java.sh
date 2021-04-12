#!/bin/bash


# 变量
version=jdk1.8.0_121
name=jdk-8u121-linux-x64
name_tar=${name}.tar.gz
target_dir=/usr/local/jdk
target_dir_bak=/usr/local/jdk_bak

#download_url=http://download.oracle.com/otn-pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/jdk-8u152-linux-x64.tar.gz?AuthParam=1510286646_ef26a138c86bb5cfc80891604fc78f70

download_url=http://qcloud.ikouqin.cn/download/${name_tar}
echo $download_url
# http://qcloud.ikouqin.cn/download/jdk-8u121-linux-x64.tar.gz


# 文件已经存在，则备份
if [ -d $target_dir ]; then
    echo "${target_dir}已经存在，开始备份"
    rm -rf $target_dir_bak
    mv $target_dir $target_dir_bak
fi


#if [ ! -d $target_dir ]; then
#    echo "jdk目录不存在"
#    mkdir $target_dir
#    echo "jdk目录创建完成"
#fi

# 下载
cd /usr/local/src
echo "开始下载"

if [ ! -f $name_tar ]; then
    wget $download_url -O $name_tar
fi

tar -zxvf $name_tar
mv $version ../jdk

# 添加环境变量
echo "export JAVA_HOME=/usr/local/jdk" >> /etc/profile
echo "PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH" >> /etc/profile

source /etc/profile

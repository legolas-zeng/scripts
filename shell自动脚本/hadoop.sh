#!/usr/bin/env bash
DOWNLOAD_DIR="/opt/download"
SOURCE_DIR="/opt/source"
CONF_DIR="/opt/conf"
SHELL_DIR=$(cd `dirname $0`; pwd)

download_url="https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz" # 更换清华站点源

if [ ! -d "$DOWNLOAD_DIR" ]; then
 mkdir $DOWNLOAD_DIR;
fi
if [ ! -d "$SOURCE_DIR" ]; then
 mkdir $SOURCE_DIR;
fi
if [ ! -d "$CONF_DIR" ]; then
 mkdir $CONF_DIR;
fi

NAME="hadoop"
VERSION="3.0.0"
OS="linux"
BIT="x64"
FULL_NAME="${NAME}-${VERSION}"
APP_SOURCE_PATH="/opt/${FULL_NAME}"
APP_DOWNLOAD_FILE="${DOWNLOAD_DIR}/${FULL_NAME}.tar.gz"
DOWLOAD_URL="http://qcloud.ikouqin.cn/download/${FULL_NAME}.tar.gz"
if [ ! -d ${APP_SOURCE_PATH}  ]; then
 wget -O ${APP_DOWNLOAD_FILE} -c ${DOWLOAD_URL}
 tar -xvf ${APP_DOWNLOAD_FILE}  -C "/opt"
 mkdir -p ${APP_SOURCE_PATH}/data
 cp -rf ${SHELL_DIR}/conf/hadoop ${APP_SOURCE_PATH}/etc/
 echo "-------------hadoop3.0安装完毕-------------"
 else
 echo "-------------hadoop3.0已经安装-------------"
fi
if  [ ! -n "$HADOOP_HOME" ] ;then
    echo "HADOOP_HOME has not set"
    echo "add blow text into /etc/profile"
    echo "export HADOOP_HOME=${APP_SOURCE_PATH}"
    echo "export HADOOP_CONF_DIR=${APP_SOURCE_PATH}/etc/hadoop"
    echo "export PATH=\$HADOOP_HOME/sbin:\$HADOOP_HOME/bin:\$PATH"
    echo "run source /etc/profile"
else
    echo "HADOOP_HOME has set"
fi

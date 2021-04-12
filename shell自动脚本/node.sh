#!/bin/bash

node_dir = /usr/local/node
download_dir = /usr/local/

if [ -d node_dir ]; then
    echo "error,node目录已经存在！"
    exit 1
fi

cd $download_dir
echo "开始下载node....."
wget https://nodejs.org/dist/v8.11.1/node-v8.11.1-sunos-x64.tar.xz

echo "开始解压...."
tar -zxf node-v8.11.1-sunos-x64.tar.xz
echo "解压完成...."

echo "
export PATH=$PATH:/usr/local/node-v8.11.1-sunos-x64/bin
" >/root/.bashrc

soure /root/.bashrc

#!/bin/bash
echo '######################开始执行脚本####################'
file_path=./root/jenkins
tomcat_path=/data/tomcatapp_web
echo '检查tomcat环境'
check_pro='ps aux | grep tomcat | grep -v grep'
if [ -n "check_pro" ]
then
   echo "tomcat已经停止"
else
    echo "tomcat还在运行中....."
fi
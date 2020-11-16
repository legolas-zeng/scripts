#!/usr/bin/env sh

if [ ! -d "/root" ]; then
  /home/rrjctomcat/dingding_msg.py
  exit 0
fi

su - rrjctomcat

. /etc/profile > /dev/null
find /usr/local/tomcat7/logs/ -mtime +10 -exec rm -f {} \;
rm /usr/local/tomcat7/work/Catalina -rf
rm /usr/local/tomcat7/temp/* -rf
sleep 2
/usr/local/tomcat7/bin/startup.sh


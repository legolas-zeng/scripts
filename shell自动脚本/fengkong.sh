#!/bin/bash

# 切换用户

function start() {
    echo -e "\033[36m----------启动 eureka 服务-----------\033[0m"
    /home/risk/discover/eurekaserice/app.sh restart
    sleep 2
    echo -e "\033[36m----------启动 blacklist 服务-----------\033[0m"
    /home/risk/blacklist/app.sh restart
    sleep 2
    echo -e "\033[36m----------启动 system 服务-----------\033[0m"
    /home/risk/system/app.sh restart
    sleep 2
    echo -e "\033[36m----------启动 feign 服务-----------\033[0m"
    /home/risk/discover/feign/app.sh restart
}

# eureka xxxx
# blacklist xxxx
# system xxxx
# feign xxxx
function check() {
    count=`netstat -lanp|grep xxxx|grep -v "grep" | wc -l `
    if [ $count -ge 1 ];then
      echo -e "\033[32m eureka已经启动√√√ \033[0m"
    else
      echo -e "\033[31m eureka未启动×××\033[0m"
    fi
    sleep 2
    count=`netstat -lanp|grep xxxx|grep -v "grep" | wc -l `
    if [ $count -ge 1 ];then
      echo -e "\033[32m blacklist已经启动√√√ \033[0m"
    else
      echo -e "\033[31m blacklist未启动×××\033[0m"
    fi
    sleep 2
    count=`netstat -lanp|grep xxxx|grep -v "grep" | wc -l `
    if [ $count -ge 1 ];then
      echo -e "\033[32m system已经启动√√√ \033[0m"
    else
      echo -e "\033[31m system未启动×××\033[0m"
    fi
    sleep 2
    count=`netstat -lanp|grep xxxx|grep -v "grep" | wc -l `
    if [ $count -ge 1 ];then
      echo -e "\033[32m feign已经启动√√√ \033[0m"
    else
      echo -e "\033[31m feign未启动×××\033[0m"
    fi

}

start
check
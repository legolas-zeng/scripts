#!/usr/bin/expect
spawn ssh root@192.168.28.130  # 启动新的进程
expect "*password:" # 从进程接收字符串，判断师傅是password
send "qq1005521\r"   # 向进程发送字符串
expect "*#" # 等上一条命令执行完
send "cd /data\r"
expect "*#"
send "touch test\r"
expect "*#"
interact  # 允许用户交互


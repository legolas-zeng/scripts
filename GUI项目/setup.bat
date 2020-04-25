@echo off
set url=http://127.0.0.1:9999/win10%2064.zip

bitsadmin /rawreturn /transfer getfile https://mirrors.tuna.tsinghua.edu.cn/zabbix/zabbix/4.5/rhel/7/x86_64/zabbix-release-4.5-2.el7.noarch.rpm c:\p.rpm


bitsadmin /transfer down /download /priority normal https://mirrors.tuna.tsinghua.edu.cn/zabbix/zabbix/4.5/rhel/7/x86_64/zabbix-release-4.5-2.el7.noarch.rpm c:\p.rpm

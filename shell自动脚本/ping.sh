#!/bin/bash
. /etc/init.d/functions
for var in {1..254};
do
  ip=172.16.50.$var
  ping -c2 $ip >/dev/null 2>&1
  if [ $? = 0 ];then
    action "$ip" /bin/true
  else
    action "$ip" /bin/false
  fi
done
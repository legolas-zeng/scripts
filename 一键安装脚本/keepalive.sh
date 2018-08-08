#!/bin/bash

KEEPALIVED_USER="keepalived"
KEEPALIVED_VERSION="2.0.4"
KEEPALIVED_INSTALL_DIR="/usr/local"

yum install -y kernel-devel openssl openssl-devel &> /dev/null
ln -s /usr/src/kernels/`uname -r`/ /usr/src/linux


id -u ${KEEPALIVED_USER=} &> /dev/null
[ $? -ne 0 ] && useradd -M -s /bin/bash ${KEEPALIVED_USER}


if [ ! -f keepalived-${KEEPALIVED_VERSION}.tar.gz ];then
 echo "下载软件包....."
 wget http://www.keepalived.org/software/keepalived-2.0.4.tar.gz
 tar -zxf keepalived-${KEEPALIVED_VERSION}.tar.gz
fi

cd keepalived-${KEEPALIVED_VERSION}
./configure --sysconf=/etc &> /dev/null
make &> /dev/null
make install &> /dev/null

/bin/cp /usr/local/sbin/keepalived /usr/bin/


sed -i 's@^KEEPALIVED_OPTIONS=.*@KEEPALIVED_OPTIONS="-D -d -S 0"@' /etc/sysconfig/keepalived
#cat >> "local0.* /var/log/keepalived/keepalived.log" /etc/rsyslog.conf
cat > /etc/rsyslog.d/keepalived.conf << EOF
local0.* /var/log/keepalived.log
&~
EOF
/etc/init.d/rsyslog restart &> /dev/null

# man config

# 
/etc/init.d/keepalived start
chmod +x /etc/init.d/keepalived
chkconfig keepalived on
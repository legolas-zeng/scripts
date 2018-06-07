#!/bin/bash
hostname=`hostname`
########### 安装zabbix ##############
yum install -y wget
wget http://downloads.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/3.4.4/zabbix-3.4.4.tar.gz
tar -zxvf zabbix-3.4.4.tar.gz
cd zabbix-3.4.4
./configure --enable-agent --prefix=/usr/local/zabbix_agentd
make && make install
############ 配置zabbix ###############

mv /usr/local/zabbix_agentd/etc/zabbix_agentd.conf /usr/local/zabbix_agentd/etc/zabbix_agentd.conf.back
cat > /usr/local/zabbix_agentd/etc/zabbix_agentd.conf << EOF
Server= 192.168.3.111,127.0.0.1
ServerActive= 192.168.3.111
Hostname = $hostname
LogFile=/var/log/zabbix/zabbix_agentd.log
PidFile=/var/run/zabbix/zabbix_agentd.pid
EOF

############## 添加防火墙 #############
firewall-cmd --permanent --add-port=10050/tcp
firewall-cmd --reload
############# 设置开机自启动 #########
sed -i '/usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/etc/zabbix_agentd.conf' /etc/rc.local

############# 启动zabbix服务 #########
/usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/etc/zabbix_agentd.conf

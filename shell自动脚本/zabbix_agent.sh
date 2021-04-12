#!/bin/bash
hostname=`hostname`
zabbix_file=zabbix-3.4.4.tar.gz

########### 同步zabbix ##############
#yum install -y wget pcre-devel
#if [ ! -f $zabbix_file ]; then
#	echo "-------------开始下载zabbix安装包-------------"
#	wget http://downloads.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/3.4.4/zabbix-3.4.4.tar.gz
#fi
mkdir -p /data/zabbix
echo "rsync" > /etc/rsync_manager_passwd.txt
chmod 600 /etc/rsync_manager_passwd.txt
rsync -avz --delete --password-file=/etc/rsync_manager_passwd.txt --port=873 tongbu@192.168.3.10::zabbix /data/zabbix

echo "---------开始解压安装包-----------"
cd /data/zabbix
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
User=root
AllowRoot=1
EOF

mkdir /var/log/zabbix/
mkdir /var/run/zabbix


############## 添加防火墙 #############
firewall-cmd --permanent --add-port=10050/tcp
firewall-cmd --reload
############# 设置开机自启动 #########
sed -i '$a /usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/etc/zabbix_agent.conf' /etc/rc.local

############# 启动zabbix服务 #########
/usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/etc/zabbix_agentd.conf

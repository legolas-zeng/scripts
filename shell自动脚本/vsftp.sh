#!/bin/bash
# sed -i "s/\r//" vsftp.sh
echo "******************************"
echo "欢迎使用一键配置vsftpd服务脚本！"


echo "******************************"
echo "执行：yum install vsftpd"
sudo yum -y install vsftpd
echo "完成：yum install vsftpd"

echo "******************************"
echo "执行：启动vsftp并设置开机启动"
sudo systemctl start vsftpd
sudo systemctl enable vsftpd
echo "完成：启动vsftp并设置开机启动"

echo "******************************"
echo "执行：添加FTP用户"
read -p "请输入FTP的用户名：" myuser
sudo adduser $myuser
echo "完成：添加FTP用户"

echo "******************************"
echo "执行：创建FTP文件夹"
read -p "请输入FTP的文件夹名：" mydir
sudo mkdir /home/$myuser/ftp
sudo chown nobody:nogroup /home/$myuser/ftp
sudo chmod a-w /home/$myuser/ftp
sudo mkdir /home/$myuser/ftp/$mydir
sudo chown $myuser:$myuser /home/$myuser/ftp/$mydir
echo "完成：创建FTP文件夹"

echo "******************************"
echo "执行：配置FTP文件"
sudo mv /etc/vsftpd/vsftpd.conf /etc/vsftpd/vsftpd.conf.bak
sudo bash -c "cat > /etc/vsftpd/vsftpd.conf" <<EOF
listen=NO
listen_ipv6=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
chroot_local_user=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
pasv_enable=Yes
pasv_min_port=10000
pasv_max_port=11000
user_sub_token=$myuser
local_root=/home/$myuser/ftp
userlist_enable=YES
userlist_file=/etc/vsftpd/vsftpd.userlist
userlist_deny=NO
EOF
sudo bash -c "cat > /etc/vsftpd/vsftpd.userlist" <<EOF
$myuser
EOF
echo "完成：配置FTP文件"

echo "******************************"
echo "执行：重启FTP服务"
sudo systemctl restart vsftpd
echo "完成：重启FTP服务。你现在可以正常使用FTP服务了!"
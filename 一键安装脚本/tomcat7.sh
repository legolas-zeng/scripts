download_dir=/usr/local/download
target_dir=/usr/local/tomcat

if [ ! -d "download_dir" ]; then
 mkdir download_dir;
fi
if [ ! -d "target_dir" ]; then
 mkdir target_dir;
fi

app_version="apache-tomcat-7.0.77"
app_file="${app_version}.tar.gz"
DOWLOAD_URL="http://qcloud.ikouqin.cn/download/centos/${app_version}.tar.gz"

# http://qcloud.ikouqin.cn/download/centos/apache-tomcat-7.0.77.tar.gz

# tar -xvf apache-tomcat-7.0.77.tar.gz -C /usr/local/

cd $download_dir
wget ${DOWLOAD_URL}
tar -xvf ${app_file} -C /usr/local/
mv $app_version tomcat



rm /usr/local/tomcat/conf/tomcat-server.xml
ln -s /usr/local/tomcat/conf/conf/server.xml /usr/local/tomcat/conf/tomcat-server.xml
echo '--------tomcat安装完成------------'

DOWNLOAD_DIR="/opt/download"
SOURCE_DIR="/opt/source"

if [ ! -d "$DOWNLOAD_DIR" ]; then
 mkdir $DOWNLOAD_DIR;
fi
if [ ! -d "$SOURCE_DIR" ]; then
 mkdir $SOURCE_DIR;
fi

NAME="zookeeper"
VERSION="3.4.11"
FULL_NAME="${NAME}-${VERSION}"
APP_SOURCE_PATH="/opt/zookeeper"
APP_DOWNLOAD_FILE="${DOWNLOAD_DIR}/${FULL_NAME}.tar.gz"
DOWLOAD_URL="http://mirrors.hust.edu.cn/apache/zookeeper/zookeeper-${VERSION}/zookeeper-${VERSION}.tar.gz"
if [ ! -d ${APP_SOURCE_PATH}  ]; then
 wget -O ${APP_DOWNLOAD_FILE} -c ${DOWLOAD_URL}
 tar -xvf ${APP_DOWNLOAD_FILE}  -C "/opt"
 mv "/opt/${FULL_NAME}" ${APP_SOURCE_PATH}
 echo "${NAME} finish installed"
else
 echo "${NAME} has installed" 
fi
# cp conf/zoo.cfg ${APP_SOURCE_PATH}/conf
#zoo_sample.cfg  这个文件是官方给我们的zookeeper的样板文件，给他复制一份命名为zoo.cfg，zoo.cfg是官方指定的文件命名规则。

cp ${APP_SOURCE_PATH}/conf/zoo_sample.cfg ${APP_SOURCE_PATH}/conf/zoo.cfg

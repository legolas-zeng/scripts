WNLOAD_DIR="/opt/download"
SOURCE_DIR="/opt/source"
CONF_DIR="/opt/conf"
SOURCE_DIR="/opt/source"
CONF_DIR="/opt/conf"
if [ ! -d "$DOWNLOAD_DIR" ]; then
 mkdir $DOWNLOAD_DIR;
fi
if [ ! -d "$SOURCE_DIR" ]; then
 mkdir $SOURCE_DIR;
fi
if [ ! -d "$CONF_DIR" ]; then
 mkdir $CONF_DIR;
fi

NAME="redis"
VERSION="4.0.2"
APP_NAME_VERSION="${NAME}-${VERSION}"
APP_SOURCE_PATH="${SOURCE_DIR}/${APP_NAME_VERSION}"
APP_DOWNLOAD_FILE="${DOWNLOAD_DIR}/${APP_NAME_VERSION}.tar.gz"
DOWLOAD_URL="http://download.redis.io/releases/${APP_NAME_VERSION}.tar.gz"
#wget http://download.redis.io/releases/redis-4.0.2.tar.gz
if [ ! -d ${APP_SOURCE_PATH} ]; then
 wget -O ${APP_DOWNLOAD_FILE} -c ${DOWLOAD_URL}
 tar -xvf ${APP_DOWNLOAD_FILE}  -C ${SOURCE_DIR}
fi
yum install -y gcc g++ gcc-c++ make
cd ${SOURCE_DIR}
cd ${APP_SOURCE_PATH}
ls
make
# make MALLOC=libc
make install
pwd
cp redis.conf /opt/conf/redis.conf


#!/usr/bin/env bash
cat >> /etc/profile <<EOF
export JAVA_HOME=/usr/local/jdk8
export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin

export HADOOP_HOME=/opt/hadoop3
export HDFS_DATANODE_SECURE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export HDFS_NAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export HDFS_DATANODE_SECURE_USER=yarn
export YARN_NODEMANAGER_USER=root
export  PATH=.:${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:$PATH
EOF

source /etc/profile
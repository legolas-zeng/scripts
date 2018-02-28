FROM ansible/centos7-ansible

COPY /usr/local/jdk1.8.0_152 /opt/jdk8
COPY hadoop3 /opt/

RUN yum install -y openssh-server
RUN yum install -y openssh-clients
RUN rm -rf /etc/localtime
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN yum install -y ntp
RUN	chkconfig ntpd on
RUN	ntpdate -u pool.ntp.org


#RUN echo "root:root" | chpasswd
#RUN echo "root<span style="white-space:pre;">   </span>All=(All)<span style="white-space:pre;"> </span>All" >> /etc/sudoers

RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key

RUN mkdir -p /opt/hadoop3/hdfs/name
RUN mkdir -p /opt/hadoop3/hdfs/data
RUN mkdir -p /opt/hadoop3/tmp

ENV JAVA_HOME /opt/jdk8
ENV PATH $JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
ENV CLASSPATH .:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

ENV HADOOP_HOME /opt/hadoop3
ENV PATH .:${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:$PATH

#!/bin/sh

name=supervisor-3.3.3
name_tar=${name}.tar.gz
supervisor_dir="/etc/supervisord"
if [ ! -d "supervisor_dir" ]; then
 mkdir $supervisor_dir;
fi
cd /etc/supervisord

pip install python-setuptools
easy_install supervisor

echo_supervisord_conf > /etc/supervisord/supervisord.conf



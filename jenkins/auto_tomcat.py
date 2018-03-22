# -*-coding:utf-8 -*-
import os,re,time,shutil
from commands import getstatusoutput as gso
import subprocess
import sys

file_path = '/data/file'
tomcat_pah = '/usr/local/tomcat'
version_path = '/data/version'
ln_name = 'project.war'

def check_pro():
    cmd = 'ps aux|grep tomcat|grep -v grep'
    status, result = gso(cmd)
    if result:
        print '<<<<<<<<<<<<<<<<<<<< tomcat running >>>>>>>>>>>>>>>>>>>>'
        return 0
    else:
        print '<<<<<<<<<<<<<<<<<<<< tomcat stopped >>>>>>>>>>>>>>>>>>>>'
        return 1
def kill_pro():
    cmd = "ps aux|grep tomcat|grep -v grep|awk '{print $2}'"
    status, result = gso(cmd)
    if result:
        cmd_kill = "kill -9 %s"%result
        status, result = gso(cmd_kill)
        if status:
            print '<<<<<<<<<<<<<<<<<<<< tomcat process is dead! >>>>>>>>>>>>>>>>>>>>'
            return 0
        else:
            print '<<<<<<<<<<<<<<<<<<<< killed abort! >>>>>>>>>>>>>>>>>>>>'
            return 1
def start_pro():
    path = tomcat_pah + '/bin'
    print path
    os.chdir(path)
    cmd = "sh startup.sh"
    status, result = gso(cmd)
    print result
    if not result:
        print "<<<<<<<<<<<<<<<<<<<< tomcat startuo failed >>>>>>>>>>>>>>>>>>>>"
        return 1
    else:
        print "<<<<<<<<<<<<<<<<<<<< tomcat startup success >>>>>>>>>>>>>>>>>>>>"
        return 0


def update_job():
    #TODO 把版本文件拷到指定目录下
    version = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
    cmd_mkdir = "mkdir /data/version/%s"%version
    status,result = gso(cmd_mkdir)
    if not result:
        print 'Create Version of the directory success!'
        file_paths = os.path.isdir(file_path)
        if not file_path:
            mkdir_req = os.mkdir(file_path)
        else:
            file = os.listdir(file_path)
            filename = file[0]
            cmd_cp = 'mv /data/file/%s /data/version/%s'%(filename,version)
            status,result = gso(cmd_cp)
            if result:
                print 'copy file success!'
                return filename,version
            else:
                print 'copy file filed!'
                exit(1)
    else:
        print 'Create Version of the directory failed!'
        exit(1)
def update_tomcat(filename,version):
    now_project_path = '/usr/local/tomcat/webapps/%s'%ln_name
    # TODO 先删除上一个版本解压之后的文件再更新软连接.
    shutil.rmtree(now_project_path)
    os.remove('/usr/local/tomcat/webapps/publish.war')
    cmd_ln = 'ln -s /usr/local/tomcat/webapps/publish.war /data/version/%s/%s'%(version,filename)
    status,result = gso(cmd_ln)
    if result:
        print 'SoftConnect create success!'
        return 0
    else:
        print 'SoftConnect create failed!'
        exit(1)
def main():
    status = check_pro()
    if status == 0:
        kill = kill_pro()
        if kill == 0:
            filename,version = update_job()
            code = update_tomcat(filename,version)
            if code == 0:
                print '<<<<<<<<<<<<<<<<<<<< Remote release success! >>>>>>>>>>>>>>>>>>>>'
                start_pro()
            else:
                print '<<<<<<<<<<<<<<<<<<<< Remote release failed! >>>>>>>>>>>>>>>>>>>>'
                exit(1)
        else:
            exit(1)
    else:
        filename, version = update_job()
        code = update_tomcat(filename, version)
        if code == 0:
            print '<<<<<<<<<<<<<<<<<<<< Remote release success! >>>>>>>>>>>>>>>>>>>>'
            start_pro()
        else:
            print '<<<<<<<<<<<<<<<<<<<< Remote release failed! >>>>>>>>>>>>>>>>>>>>'
            exit(1)

if __name__ == '__main__':
    main()





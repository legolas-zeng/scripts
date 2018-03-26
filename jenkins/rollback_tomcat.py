# -*-coding:utf-8 -*-
import sys,os,re,shutil
from commands import getstatusoutput as gso
from auto_tomcat import *

version_path = '/data/version'
ver = sys.argv[1]
def main():
    if ver.isdigit() and len(ver) == 1:
        # 比如输入python rollback_tomcat.py 2 就是回滚到2个版本前
        print u'你要回滚到前%s个版本....'%ver
        roll_code(ver)
    elif len(ver) == 13 and re.search(r"\d{4}(\-|\/|.)\d{1,2}\1\d{1,2}\1\d{1,2}",ver,re.I):
        roll_full(ver)
    else:
        print u'你输入的参数有误....'
        exit(1)

def roll_code(ver):
    version = int(ver) + 2
    # TODO 按时间排序，然后重建软连接
    cmd_sort = "ls -lt /data/version|sed -n %sp|awk '{print $9}'"%version
    print cmd_sort
    status,result = gso(cmd_sort)
    filename = os.listdir('/data/version/%s'%result)
    if not status:
        print u'准备回滚到版本号为%s的版本'%result
        status = check_pro()
        if status == 0:
            kill = kill_pro()
            if kill == 0:
                code = update_tomcat(filename, result)
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
    else:
        print u'获取版本号失败...'
        exit(1)


def roll_full(ver):
    print ver
    # TODO 精确查找到某个版本


if __name__ == '__main__':
    main()

# -*-coding:utf-8 -*-
import os,re,zipfile


file_path = 'D:/cqAdmin/versions'

def showPath():
    game_path = 'D:\games\\552play'
    path = os.listdir(game_path)
    filePath, name = showFile()
    print u"你要热更的文件是%s,是否确认？" %name
    input = raw_input()
    if input not in ['y', 'Y']:
        print u"退出操作"
        exit(1)
    else:
        for p in path:
            games_path = os.path.join(game_path,p)
            print games_path
            unzipFile(filePath,games_path)

def showFile():
    file_path = 'D:\cqAdmin\\versions\\hotupdate'
    if not os.path.isdir(file_path):
        print u"请检查热更文件夹（D:/cqAdmin/versions/hotupdate）是否存在!!"
        exit(1)
    else:
        file = os.listdir(file_path)
        print file
        if file == []:
            print u"请放入你要热更的文件，程序退出！！！"
            exit(1)
        elif len(file) != 1:
            print u"只允许放入一个热更文件，程序退出！！！"
            exit(1)

        filename = file[0]
        if not filename.endswith('.zip'):
            print u"文件不是zip包，程序退出！！！"
            exit(1)
        file_path = os.path.join(file_path, filename)
        return file_path,filename

#解压缩Zip到指定文件夹
class ZFile(object):
    def __init__(self, filename, mode='r', basedir=''):
        self.filename = filename
        self.mode = mode
        if self.mode in ('w', 'a'):
            self.zfile = zipfile.ZipFile(filename, self.mode, compression=zipfile.ZIP_DEFLATED)
        else:
            self.zfile = zipfile.ZipFile(filename, self.mode)
        self.basedir = basedir
        if not self.basedir:
            self.basedir = os.path.dirname(filename)

    def addfile(self, path, arcname=None):
        path = path.replace('//', '/')
        if not arcname:
            if path.startswith(self.basedir):
                arcname = path[len(self.basedir):]
            else:
                arcname = ''
        self.zfile.write(path, arcname)

    def addfiles(self, paths):
        for path in paths:
            if isinstance(path, tuple):
                self.addfile(*path)
            else:
                self.addfile(path)

    def close(self):
        self.zfile.close()

    def extract_to(self, path):
        for p in self.zfile.namelist():
            self.extract(p, path)

    def extract(self, filename, path):
        if not filename.endswith('/'):
            f = os.path.join(path, filename)
            dir = os.path.dirname(f)
            if not os.path.exists(dir):
                os.makedirs(dir)
            file(f, 'wb').write(self.zfile.read(filename))

def unzipFile(zfile,path):
    z = ZFile(zfile)
    z.extract_to(path)
    z.close()
    print u'%s解压完成'%path


showPath()

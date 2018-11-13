# coding=utf-8
import zipfile
import os

def zip_ya(startdir,file_news):
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('压缩成功')
    z.close()

if __name__ == "__main__":
    startdir = "C:\Users\Administrator\Desktop\\xiaohong\\test"
    file_news = 'xiaohong' + '.zip'
    zip_ya(startdir,file_news)
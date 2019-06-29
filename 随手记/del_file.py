# -*- coding: utf-8 -*-
import os,sys,time

def removefiles(beftime, defalutpath='.'):
    for i in os.listdir(path):
        filename = path + os.sep + i
        if os.path.getmtime(filename) < beftime:
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
                elif os.path.isdir(filename):
                    os.removedirs(filename)
                else:
                    os.remove(filename)
                print("%s remove success." % filename)
            except Exception as error:
                print(error)
                print("%s remove faild." % filename)


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        breday = int(sys.argv[2])
        bretime = time.time() - 3600 * 24 * breday
        removefiles(bretime, path)
    except Exception as e:
        print(e)
        sys.exit(-1)

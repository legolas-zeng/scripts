#### 库的安装
###### 1、[pip](https://pypi.org/)
>安装:  pip install PackageName==Version
>
>查看:  pip freeze
>
>卸载:  pip uninstall PackageName
##### 2、whell
>安装:  pip install PackageName.whl
##### 3、conda
>安装:  conda install PackageName==Version
>
>查看:  conda list
>
>卸载:  conda remove PackageName
##### 4、easy_install
>安装:  easy_install PackageName

### 库的引用
##### 1、绝对引用

```
from numpy import array
```
##### 2、相对引用
```
from ..one import point
```
##### 3、全量引用
```
from numpy import *
```
`尽量不要用全量引用`
### package
##### 1、package路径

-[X] C:\Python37\Lib\site-packages
-[X] /usr/lib/python2.7/site-packages

##### 2、exe文件打包
```
pip install pyinstaller

pyinstaller -F helloworld.py
```

-[X] -F参数可将代码打包成单个exe程序
-[X] 脚本路径不能含有中文
-[X] 运行之后exe文件在`dist`目录









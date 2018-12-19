#### 库的安装
##### 1、[pip](https://pypi.org/)
>安装:  pip install PackageName==Version
>
>查看:  pip freeze
>
>卸载:  pip uninstall PackageName
#### 2、whell
>安装:  pip install PackageName.whl
#### 3、conda
>安装:  conda install PackageName==Version
>
>查看:  conda list
>
>卸载:  conda remove PackageName
#### 4、easy_install
>安装:  easy_install PackageName

### 库的引用
#### 1、绝对引用

```
from numpy import array
```
#### 2、相对引用
```
from ..one import point
```
#### 3、全量引用
```
from numpy import *
```

#### 





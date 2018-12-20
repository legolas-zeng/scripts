##### 1、空函数
```
def NullFunction():
    pass
```
##### 2、`__name__`函数
```
if __name__ == "__main__":
    main()
``` 
-[X] `__main__`一般作为函数的入口
-[X] `__main__`当前模块的名称，用于区分是否运行在当前模块

`__xx__`前后各双下划线的函数都是用于Python调用的，不要随意调用

`_`单下划线的函数表明不是API，不要去调用

##### 3、多值返回
```
def MultReturn():
    a = 'A'
    b = 'B'
    return a,b
```
##### 4、自省函数
###### dir()
> 删除所有可以调用的方法
###### type()
>返回对象的类型。
###### len()
>返回长度
###### id()
>返回内存地址id
##### 5、参数
###### 默认参数

```
def DefaultArg(x,y='Y'):
    pass
```
###### 不定参数
```
def VaryArg(*args):
    pass
```
###### 关键字参数
```
def KeyArg(**kwargs)
    pass
```
###### 传参的本质

-[X] 指针传递
-[X] 值拷贝传递
```
a = 1
def ChangeValue(a):
    a = a + 1
ChangeValue(a)
print a
```
#### 6、类
#####类的初始化
```
class A (object):
    def __init__(self):
        self.one = '1'
        self.two = '2'
    def output(self,*args):
        print args
        print self.one
        print self.two
``` 

##### 类的继承
```
B = A()  # 实例化
B.output("123") # 调用output方法
```

##### 子类调用父类
```
class C (A):
    def __init__(self):
        self.three = '3'
        A.__init__(self) # 子类中初始化父类
    def shuchu(self):
        data = A.fanhui(self)
        print data
```







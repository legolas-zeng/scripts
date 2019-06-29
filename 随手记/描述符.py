# coding=utf-8
# @Time    : 2019/6/13 11:02
# @Author  : zwa

'''
描述符一般用于实现对象系统的底层功能， 包括绑定和非绑定方法、类方法、静态方法特特性等。
'''

'''
descr.__get__(self, obj, type=None) -> value
descr.__set__(self, obj, value) -> None
descr.__delete__(self, obj) -> None

定义任何上面三个方法的任意一个,这个对象就会被认为是一个描述符,并且可以在被作为对象属性时重载默认的行为,
如果一个对象定义了__get__() 和 __set__(),它被认为是一个数据描述符.只定义 __get__()被认为是非数据描述符,
数据和非数据描述符的区别在于:如果一个实例的字典有和数据描述符同名的属性,那么数据描述符会被优先使用,
如果一个实例的字典实现了无数据描述符的定义,那么这个字典中的属性会被优先使用,实现只读数据描述符,
同时定义__get__()和__set__(),在__set__()中抛出AttributeError.
'''

class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
m.x = 20    # 对描述符进行赋值，会触发它的__set__方法，因为有self.val = val，所以在__set__方法中还会触发__setattr__方法
m.x         # 触发__get__方法

'''
以上定义了两个类。其中RevealAccess类的实例是作为MyClass类属性x的值存在的。而且RevealAccess类定义了__get__、__set__方法，
它是一个描述符对象。注意，描述符对象的__get__、__set__方法中使用了诸如self.val和self.val = val等语句，
这些语句会调用__getattribute__、__setattr__等方法，这也说明了__getattribute__、__setattr__等方法在控制访问对象属性上的一般性
（一般性是指对于所有属性它们的控制行为一致），以及__get__、__set__等方法在控制访问对象属性上的特殊性（特殊性是指它针对某个特定属性可以定义不同的行为）。
'''

'''
注意，描述符对象的__get__、__set__方法中使用了诸如self.val和self.val = val等语句，这些语句会调用__getattribute__、__setattr__等方法
'''

'''
描述符有数据描述符和非数据描述符之分:
1、只要至少实现__get__、__set__、__delete__方法中的一个就可以认为是描述符； 
2、只实现__get__方法的对象是非数据描述符，意味着在初始化之后它们只能被读取； 
3、同时实现__get__和__set__的对象是数据描述符，意味着这种属性是可读写的。
'''
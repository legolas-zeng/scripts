# coding=utf-8
# @Time    : 2019/4/22 10:46
# @Author  : zwa

'''
该方法主要思路就是在覆盖实例化函数__new__()，在其中添加判断，检查对象是否存在。
hasattr是python的特殊方法，用来查看对象是否具有某个属性。
'''
# class Singleton(object):
#     def __new__(self):
#         if not hasattr(self, 'instance'):
#             self.instance = super(Singleton, self).__new__(self)
#         return self.instance
#
#
# a = Singleton()
# b = Singleton()
#
# print(id(a), id(a))


'''
如果想要继承这个Singleton，子类中一定不要忘了重写__new__方法，否则会覆盖掉父类中已经修改的方法。
'''
# class Singleton(object):
#     def __new__(self):
#         if not hasattr(self, 'instance'):
#             self.instance = super(Singleton, self).__new__(self)
#         return self.instance
#
#
# class test(Singleton):
#     def __new__(self):
#         super(Singleton, self).__new__(self)
#
#
# ab = test()
# bc = test()
#
# print(id(ab), id(bc))

'''
元类是一个类的类，可以通过创建元类，重新定义类的行为。当我们用类A创建一个类的时候，
python通过A = type( name , bases , dict )创建它，其中name是类的名称，base是基类，dict是属性变量。
这个过程是，首先__new__创建类的实例，作为__init__的输入，完成构造函数的作用。当然这个过程的结果是获得了一个实例并且是叫做：
Student的类，ClassStudent是对这个类的引用。当采用（）调用，即实现Meta的实例的可调用的实例化过程。
'''
# class Meta(type):
#     def __init__(self, name, bases, attrs):
#         print("init")
#         super(Meta, self).__init__(name, bases, attrs)
#
#     def __new__(meta, name, bases, attrs):
#         print("new")
#         return super(Meta, meta).__new__(meta, name, bases, attrs)
#
#     def __call__(self):
#         print("call")
#         return super(Meta, self).__call__()
#
#
# s = ["Student", (object,), {"name": "Joe", "age": 25}]
# ClassStudent = Meta(*s)
# instance = ClassStudent()


def counter_af(l):
    result = {}
    for key in l:
        try:
            result[key] += 1
        except KeyError:
            result[key] = 1
    print(result)

counter_af([1,2,1,2,3])


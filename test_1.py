# -*-coding:utf-8 -*-
# -*- coding:utf-8 -*-
# 摇3次骰子，当总数total，3<=total<=10时为小，11<=total<=18为大
import random
import time

# def enter_stake(current_money):
#     '''输入小于结余的赌资及翻倍率,未考虑输入type错误的情况'''
#     stake = int(input('How much you wanna bet?(such as 1000):'))
#     rate = int(input("What multiplier do you want?你想翻几倍？(such as 2):"))
#     small_compare = current_money < stake * rate
#     while small_compare == True:
#         stake = int(input('You has not so much money ${}!How much you wanna bet?(such as 1000):'.format(stake * rate)))
#         rate = int(input("What multiplier do you want?你想翻几倍？(such as 2):"))
#         small_compare = current_money < stake * rate
#     return stake,rate
#
# def roll_dice(times = 3):
#     '''摇骰子'''
#     print('<<<<<<<<<< Roll The Dice! >>>>>>>>>>')
#     points_list = []
#     while times > 0:
#         number = random.randrange(1,7)
#         points_list.append(number)
#         times -= 1
#     return points_list
#
# def roll_result(total):
#     '''判断是大是小'''
#     is_big = 11 <= total <= 18
#     is_small = 3 <= total <= 10
#     if is_small:
#         return 'Small'
#     elif is_big:
#         return 'Big'
#
# def settlement(boo,points_list,current_money,stake = 1000,rate = 1):
#     '''结余'''
#     increase = stake * rate
#     if boo:
#         current_money += increase
#         print('The points are ' + str(points_list) + ' .You win!')
#         print('You gained $' + str(increase) + '.You have $' + str(current_money) + ' now.' )
#     else:
#         current_money -= increase
#         print('The points are ' + str(points_list) + ' .You lose!')
#         print('You lost $' + str(increase) + '.You have $' + str(current_money) + ' now.' )
#     return current_money
#
# def sleep_second(seconds=1):
#     '''休眠'''
#     time.sleep(seconds)
#
#
# # 开始游戏
# def start_game():
#     '''开始猜大小的游戏'''
#     current_money = 1000
#     print('You have ${} now.'.format(current_money))
#     sleep_second()
#     while current_money > 0:
#         print('<<<<<<<<<<<<<<<<<<<< Game Starts! >>>>>>>>>>>>>>>>>>>>')
#         your_choice = input('Big or Small: ')
#         choices = ['Big','Small']
#         if your_choice in choices:
#             stake,rate = enter_stake(current_money)
#             points_list = roll_dice()
#             total = sum(points_list)
#             actual_result = roll_result(total)
#             boo = your_choice == actual_result
#             current_money = settlement(boo,points_list,current_money,stake,rate)
#         else:
#            print('Invalid input!')
#     else:
#         sleep_second()
#         print('Game Over!')
#         sleep_second(2)
#
# if __name__ == '__main__':
#     start_game()

# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
#
# g = foo()
# print(next(g))
# print(g.send(7))
# # g.close()

# s = 'ABC'
# l = list(s)
# print(l)
# print(dir(l))

# class A:
#     def x(self):
#         print("A")
#
# class B(A):
#     pass
#
# class C(A):
#     def x(self):
#         print("C")
#
# class D(B,C):
#     pass
#
# s=D()
# s.x()

# def func(a: int = ...):
#     print(a)   # Ellipsis
#
# func(111)

# s1="abc123abc"
# res=s1.upper()
# print(res)

# class A(object):
#     def __init__(self,*args,**kwargs):
#         print("init &&&& %s" % self.__class__)
#         super(A, self).__init__()
#         print(*args,**kwargs)
#
#     def __new__(cls,*args,**kwargs):
#         print("new &&&& %s" % cls)
#         return super(A,cls).__new__(cls)
#
# a=A()
#
# class PositiveInterger(int):
#     def __new__(cls,value):
#         return super(PositiveInterger, cls).__init__(abs(value))
#
# i = PositiveInterger(-3)
# print(i)

# class Singleton(object):
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"): # 反射
#             Singleton._instance = object.__new__(cls)
#         return Singleton._instance
#
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1, obj2)
#
#
# class Singletons(object):
#     # _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls, *args, **kwargs)
#         return cls._instance


# def singlem(fn):
#     __instans = {}
#     def function(*args, **kwargs):
#         if fn not in __instans:
#             __instans[fn] = fn(*args, **kwargs)
#         return __instans[fn]
#     return function
#
# @singlem
# def person(a=0, b=1):
#     return (a, b)
#
#
# print(person())
#
# import threading
# class Singleton(object):
#     _instance_lock = threading.Lock()
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = object.__new__(cls)
#         return Singleton._instance
#
# ab = Singleton()
#
# class Person:
#     def __init__(self,height,weight):
#         self.height = height
#         self.weight = weight
#
#     def get_height(self):
#         return self.height
#
#     def get_weight(self):
#         return self.weight
#
#
# class Male(Person):
#     def __init__(self, name):
#         print("Hello Mr." + name)
#
#
# class Female(Person):
#     def __init__(self, name):
#         print("Hello Miss." + name)
#
#
# class Factory:
#     def getPerson(self, name, gender):
#         if gender == 'M':
#             return Male(name)
#         if gender == 'F':
#             return Female(name)
#
#
# if __name__ == '__main__':
#     factory = Factory()
#     person = factory.getPerson("ll", "F")


class CashSuper(object):
    def accept_cash(self,money):
        pass

class CashNormal(CashSuper):
    def accept_cash(self,money):
        return money

class CashRebate(CashSuper):
    def __init__(self,discount=1):
        self.discount = discount

    def accept_cash(self,money):
        return int(money) * self.discount

class CashReturn(CashSuper):
    def __init__(self,money_condition=0,money_return=0):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self,money):
        if int(money)>=self.money_condition:
            return int(money) - (int(money) / self.money_condition) * self.money_return
        return int(money)

class Context(object):
    def __init__(self,csuper):
        self.csuper = csuper

    def GetResult(self,money):
        return self.csuper.accept_cash(money)


if __name__ == '__main__':
    money = input("原价: ")
    strategy = {}
    strategy[1] = Context(CashNormal())
    strategy[2] = Context(CashRebate(0.8))
    strategy[3] = Context(CashReturn(100,10))
    mode = input("选择折扣方式: 1) 原价 2) 8折 3) 满100减10: ")
    if int(mode) in [1,2,3]:
        csuper = strategy.get(int(mode))
    else:
        print("不存在的折扣方式")
        csuper = strategy[1]
    print("需要支付: ",csuper.GetResult(money))
# coding=utf-8
# @Time    : 2019/4/23 11:15
# @Author  : zwa
from typing import TypeVar, Iterable, Tuple, Dict, List,MutableMapping,Text

'''
对于较复杂的内置类型、泛型、生成器、自定义类型等，需要引入标准库typing
typing常用的类型：
int,long,float: 整型,长整形,浮点型;
bool,str: 布尔型，字符串类型；
List, Tuple, Dict, Set:列表，元组，字典, 集合;
Iterable,Iterator:可迭代类型，迭代器类型；
Generator：生成器类型；
'''

t : Tuple[int, float] = (0,1.2)
d : Dict[str, int] = {"a": 1, "b": 2}
m : MutableMapping[str, int] = {"a": 1, "b": 2}
l : List[int] = [1, 2, 3]
i : Iterable[Text] = [ u'1', u'2', u'3']
print(t,d,m,l,i)

Vector = List[float]
Matrix = List[Vector]

def addTwo(x : int) -> int:
   return x + 2


def addMatrix(a : Matrix, b : Matrix) -> Matrix:
    result = []
    for i,row in enumerate(a):
        result_row =[]
        for j, col in enumerate(row):
            result_row += [a[i][j] + b[i][j]]
        result += [result_row]
    return result
x = [[1.0, 0.0], [0.0, 1.0]]
y = [[2.0, 1.0], [0.0, -2.0]]
z = addMatrix(x, y)
print(z)

'''
->:标记返回函数注释,信息作为.__annotations__属性提供,__annotations__属性是字典。
键return是用于在箭头后检索值的键。
->用于指示函数返回的类型。
'''
def test() -> [1, 2, 3, 4, 5]:
    pass

print(test.__annotations__)

# coding=utf-8
import read_excel
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


excel_path = "C:\\Users\Administrator\Desktop\movie_info.xlsx"
grad_list = read_excel.read_xls(excel_path,2)

res = {}
for i in grad_list:
    res[i] = res.get(i, 0) + 1
print(res)

# print([k for k in res.keys()])
# print([v for v in res.values()])

def sortedDictValues(adict):
    keys = adict.keys()
    keys.sort()
    return keys
    # return map(adict.get(), keys)


# sort_res = sortedDictValues(res)
sort_res = sorted(res)
print(sort_res)

sort_res_value = []
for i in range(0,len(res)):
    sort_res_value.append(res[sort_res[i]])
print(sort_res_value)
#设置汉字格式
# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
x = sort_res  # X轴
y = sort_res_value

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

plt.plot(x,y,label=u'趋势图',linewidth=1,color='g',marker='o',)
plt.xlabel(u'影片评分')
plt.ylabel(u'得分的影片数量')
plt.title(u'豆瓣电影TOP250\n评分分布图')
plt.legend()
plt.savefig("C:\\Users\Administrator\Desktop\movie_info.svg")
plt.show()


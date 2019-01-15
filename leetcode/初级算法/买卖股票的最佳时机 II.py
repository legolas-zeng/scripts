# coding=utf-8

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
prices = [7,1,5,3,6,4]
data_len = len(prices)
i = 1
data = []
for x in prices:
    print('被减数',x)
    print('减数',prices[i])
    result = x - prices[i]
    print(result)
    data.append(result)
    i+=1
print(data)
for z in range(10):
    pass

def max_number(list):
    pass
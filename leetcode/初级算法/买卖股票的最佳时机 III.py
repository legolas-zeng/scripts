# coding=utf-8
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
prices = [3,3,5,0,0,3,1,4]
maxprofit = 0
# oneprofit = []
# for i in range(1,len(prices)):
#     d = prices[i] - prices[i-1]
#     if d > 0:
#         oneprofit.append(d)
# print(oneprofit)
# if len(oneprofit) == 0:
#     maxprofit = 0
# if len(oneprofit) == 1:
#     maxprofit = oneprofit[0]
# if len(oneprofit) == 2:
#     maxprofit = oneprofit[0] + oneprofit[1]
# else:
#     pass

# result[k,i]=max(result[k,i−1],prices[i]−prices[j]+result[k−1,j−1])

result = 0
if not prices:
    result = 0
len_prices = len(prices)
buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0
for i in range(1, len_prices):
    buy1 = max(buy1, -prices[i])
    sell1 = max(sell1, buy1 + prices[i])
    buy2 = max(buy2, sell1 - prices[i])
    sell2 = max(sell2, buy2 + prices[i])

print(max(0, sell1, sell2))








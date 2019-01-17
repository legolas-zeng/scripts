# coding=utf-8
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
prices = [3,3,5,0,0,3,1,4]

if not prices:
    result = 0
len_prices = len(prices)
'''
分为两部分，第一次收益，和第二次收益。
'''
buy1 = -prices[0]   # -3
buy2 = -prices[0]   # -3
sell1 = 0
sell2 = 0

for i in range(1, len_prices):              # 从prices[1]开始
    print(i)
    buy1 = max(buy1, -prices[i])            # 第一次买入手上的钱
    sell1 = max(sell1, buy1 + prices[i])    # 第一次卖出手上的钱
    print('11111111',buy1,sell1)
    buy2 = max(buy2, sell1 - prices[i])     # 第二次买入手上的钱
    sell2 = max(sell2, buy2 + prices[i])    # 第二次卖出手上的钱
    print('22222222', buy2, sell2)

print(max(0, sell1, sell2))








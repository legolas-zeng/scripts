# coding=utf-8
prices = [3,3,5,0,0,3,1,4]

result = 0
for i in range(len(prices)-1):
    for j in range(i + 1, len(prices)):
        result = max(result, prices[j] - prices[i])
print(result)

Begin_value = prices[0]
result = 0                # 初始化结果为0
for p in prices:
    result = max(result, p-Begin_value)
    Begin_value = min(Begin_value, p)
print(result)
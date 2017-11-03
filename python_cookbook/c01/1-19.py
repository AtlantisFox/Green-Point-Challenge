# encoding=utf-8
# 生成器表达式
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

portfolio = [ {'name':'GOOG', 'shares': 50}, 
{'name':'YHOO', 'shares': 75}, 
{'name':'AOL', 'shares': 20}, 
{'name':'SCOX', 'shares': 65} ] 

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# note this 
# generator only can be use one time

data = (x**x for x in range(3))
next(data)
next(data)
next(data)

for i in data:
	print(i)

# reduce function now in functools(python3)

from functools import reduce

reduce(lambda x, y:x + y, list(range(100)))
from collections import defaultdict
from collections import OrderedDict
import json

def defaultdict_test():
	pairs = [('shazhao', 'nj'), ('shahua', 'sh'), ('shali', 'sz'), ('shazhao', 'sz')]
	d = defaultdict(list)
	for key, value in pairs:
		d[key].append(value)
	print(d)

def ordereddict_test():
	d = OrderedDict()
	d['shazhao'] = 1
	d['shahua'] = 2
	d['shali'] = 3
	for key in d:
		print(key, d[key])
	json.dumps(d)

def dic_compute():
	prices = {'apple': 6985, 'mix': 3999, 'note': 5999}
	min_price = min(zip(prices.values(), prices.keys()))
	max_price = max(zip(prices.values(), prices.keys()))

def dic_set_op():
	a = {'x': 1, 'y': 2, 'z': 3}
	b = {'w': 10, 'x': 11, 'y': 2}
	print(a.keys() & b.keys())
	print(a.keys() - b.keys())
	print(a.items() & b.items())

if __name__ == '__main__':
	defaultdict_test()
	ordereddict_test()
	dic_compute()
	dic_set_op()
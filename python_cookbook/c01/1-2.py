# coding=utf-8

from functools import reduce

def drop_first_last(grades):
	first, *middle, last = grades
	return reduce(lambda x,y:x+y,middle)/len(middle)

def get_datahead(data):
	head, *tail = data
	return head

if __name__ == '__main__':
	grades = [80, 78, 32, 44, 100]
	print(drop_first_last(sorted(grades)))
	print(get_datahead(grades))
	# neat in python3
	print([*map(lambda x:x**2,list(range(100)))])
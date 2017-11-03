# encoding=utf-8

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my',
'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'you are',
'under']

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why','are','you','not','looking','in','my','eyes']

a = Counter(words)
b = Counter(morewords)
print(a, b)
# Counter实例可以使用数学运算操作相结合
c = a + b
d = a - b
print(c, d)
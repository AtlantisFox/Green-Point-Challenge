from collections import deque
from itertools import dropwhile, permutations, chain
import itertools



# 4.3
def frange(start, stop,  increment):
    x = start
    while x < stop:
        yield x
        x += increment


# 4.5
class Countdown(object):
    def __init__(self, start):
        self.start = start

    # forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # reverse iterator
    def __reversed__(self):
        n = 1
        while n < self.start:
            yield n
            n += 1

# 4.6
class linehistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def count(n):
    while True:
        yield n
        n += 1


# 4.7
def iterator_slice():
    c = count(0)
    for i in itertools.islice(c,10, 20):
        print(i)


# 4.8 跳过可迭代对象开始的部分
def drop_ele_iter():
    print('before:')
    with open('08.input') as f:
        for line in f:
            print(line, end='')

    print('\n\nafter:')
    with open('08.input') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')


# 4.9 排列组合
class Perm(object):
    items = ['a', 'b', 'c']

    @classmethod
    def arrange(cls):
        for p in permutations(cls.items):
            print(p)


# 4.10 序列上索引值迭代
class Index(object):
    list = ['a', 'b', 'c']

    @classmethod
    def meth1(cls):
        for idx, val in enumerate(cls.list):
            print(idx, val)


class Iter(object):
    al = [1, 2, 3, 4, 5]
    bl = ['a', 'b', 'c', 'd', 'e']

    # 4.11 同时迭代多个序列
    @classmethod
    def meth(cls):
        for x, y in zip(cls.al, cls.bl):
            print(x, y)

    # 4.12 在不同结合上元素的迭代
    @classmethod
    def meth0(cls):
        for x in chain(cls.al, cls.bl):
            print(x)



def call_frange():
    for i in frange(0, 4, 0.5):
        print(i)

    print(list(frange(0, 1, 0.25)))


def call_countdown():
    for i in reversed(Countdown(10)):
        print(i)


def call_linehistory():
    with open('06.input') as f:
        lines = linehistory(f)
        for line in lines:
            if 'flag' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

if __name__ == '__main__':

    pass

    # call_frange()

    # call_countdown()

    # call_linehistory()

    # iterator_slice()

    # drop_ele_iter()

    # Perm.arrange()

    # Index.meth1()

    # Iter.meth()

    Iter.meth0()
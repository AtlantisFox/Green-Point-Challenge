import heapq, random
from collections import deque

def deque_test():
    range_deque = deque(maxlen=10)
    for i in range(20):
        range_deque.append(i)
    print(range_deque)

def heapq_test():
    nums = []
    for i in range(100):
        nums.append(random.randint(0, 100))
    print(heapq.nlargest(10, nums))
    print(heapq.nsmallest(10, nums))
    heapq.heapify(nums)
    for i in range(10):
        print(heapq.heappop(nums))

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        print(heapq.heappop(self._queue)[-1])

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

def priority_queue_test():
    q = PriorityQueue()
    q.push(Item('shahua'), 1)
    q.push(Item('shazhao'), 5)
    q.push(Item('fuli'), 6)
    q.push(Item('3 ldiots'), 6)
    q.pop()
    q.pop()
    q.pop()
    q.pop()

if __name__ == "__main__":
    deque_test()
    heapq_test()
    priority_queue_test()

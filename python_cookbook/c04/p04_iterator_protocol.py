"""
topc: 实现迭代器协议
desc: 构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

"""
python的迭代协议要求一个__iter__()方法发挥一个特殊的迭代器对象,
这个迭代器对象实现了__next__()方法, 并通过StopIteration异常标识迭代的完成.
但是实现比较繁琐. 

下面我们演示这种方式, 如何使用一个关联迭代器类重新实现depth_first()方法

"""
class Node2:
    def __init(self, value):
        self._value = value
        self._children = []

    def __repr(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstInterator(self)


class DepthFirstInterator(object):
    """
    深度优先遍历
    """

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # 如果是开始节点就返回自身; 为子节点生成一个迭代器
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # 如果执行到子节点, 就返回它的下一个节点
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)

        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

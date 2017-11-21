class Node():
	"""docstring for Node"""
	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		return 'Node ({!r})'.format(self._value)

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

	def depth_first(self):
		yield self
		for c in self:
			yield from c.depth_first()

def countdown(n):
	print('Starting to count from', n)
	while n > 0:
		yield n
		n -= 1
	print('Done!')

class Countdown():
	"""docstring for Countdown"""
	def __init__(self, start):
		self.start = start

	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -= 1

	def __reversed__(self):
		n = 1
		while n <= self.start:
			yield n 
			n += 1

if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)
	child1.add_child(Node(3))
	child1.add_child(Node(4))
	child2.add_child(Node(5))
	for ch in root:
		print(ch)
	for ch in root.depth_first():
		print(ch)
	for i in countdown(10):
		print(i)
	count = Countdown(10)
	for i in reversed(count):
		print(i)
		
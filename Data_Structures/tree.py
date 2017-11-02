# coding=utf-8


class Node(object):
	"""docstring for Node"""
	def __init__(self, elem=-1, left=None, right=None):
		super(Node, self).__init__()
		self.elem = elem
		self.left = left
		self.right = right


class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		super(Tree, self).__init__()
		self.root = Node()
		self.myQueue = []

	def add(self, elem):
		node = Node(elem)
		if self.root.elem == -1:
			self.root = node
			self.myQueue.append(self.root)
		else:
			treeNode = self.myQueue[0]
			if treeNode.left == None:
				treeNode.left = node
				self.myQueue.append(treeNode.left)
			else:
				treeNode.right = node
				self.myQueue.append(treeNode.right)
				self.myQueue.pop(0)


if __name__ == '__main__':
	elems = list(range(10))
	tree = Tree()
	for elem in elems:
		tree.add(elem)
	for node in tree.myQueue:
		print(node.elem)
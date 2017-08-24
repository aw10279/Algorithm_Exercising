# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
    	self.elem = elem
    	self.lchild = lchild
    	self.rchild = rchild

class Tree(object):
	def __init__(self):
		self.root = Node()
		self.queue = []

	def add(self, elem):
		node = Node(elem)
		if node.root.elem == -1:
			self.root = node
			self.queue.append(self.root)
        else:
        	t_node = self.queue(0)
            if t_node.lchild == None:
            	t_node.lchild = node
            	self.queue.append(t_node)
            else:
            	t_node.rchild = node
            	self.queue.append(t_node.rchild)
                self.queue.pop(0)
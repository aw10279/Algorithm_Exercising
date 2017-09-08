# coding: utf-8

class Node(object):  #创建节点类,有内容、左右子树3个属性
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object): #创建树类，有根节点属性；queue用来记录所有子树不全的节点；且所有函数均在此类下定义
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:  #若根节点为空，赋值给根节点
            self.root = node
            self.queue.append(self.root)
        else:
            t_node = self.queue[0]  
            if t_node.lchild == None:  #若左子树为空，赋值给左子树
                t_node.lchild = node
                self.queue.append(t_node.lchild)
            else:
                t_node.rchild = node  #左不为空，赋值给右
                self.queue.append(t_node.rchild)
                self.queue.pop(0)  #左右都已赋值的节点，从queue中删除

    def front_recursion(self, root): #递归-先序遍历
        if root == None:
            return
        print(root.elem)
        self.front_recursion(root.lchild)
        self.front_recursion(root.rchild)

    def middle_recursion(self, root): #递归-中序遍历
        if root == None:
            return
        self.middle_recursion(root.lchild)
        print(root.elem)
        self.middle_recursion(root.rchild)

    def behind_recursion(self, root): #递归-后序遍历
        if root == None:
            return
        self.behind_recursion(root.lchild)
        self.behind_recursion(root.rchild)
        print(root.elem)

    def front_stack(self, root):      #堆栈-先序遍历
        if root == None:
            return
        stack = []  #记录所有待遍历节点
        node = root
        while node or stack:
            while node:  #此循环一直遍历左子树，退出则遍历到尽头
                print(node.elem)
                stack.append(node)
                node = node.lchild
            node = stack.pop()  #node指向堆栈中最后一个元素，同时删除该元素（要指向右子树的节点需从堆栈删除，下次才能指向上层）
            node = node.rchild  #指向右子树

    def middle_stack(self, root):      #堆栈-中序遍历
        if root == None:
            return
        stack = []  
        node = root
        while node or stack:
            while node:  #此循环一直遍历左子树，退出则遍历到尽头，但不输出任何内容
                stack.append(node)
                node = node.lchild
            node = stack.pop()
            print(node.elem)    #node指向上层并删除后，再输出内容，然后指向右子树
            node = node.rchild

    def behind_stack(self, root):     #堆栈-后序遍历
        if root == None:
            return
        stack1 = []  #stack1负责记录待遍历节点，stack2负责逆序储存节点，最后依序输出即可
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.lchild:
                stack1.append(node.lchild)
            if node.rchild:
                stack1.append(node.rchild)
            stack2.append(node)  #将遍历过左右的节点加入stack2，此顺序即为后序遍历的逆序
        while stack2:
            print(stack2.pop().elem)

    def layer(self, root):           #层次遍历
        if root == None:
            return
        queue = []
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)  #每次循环都指向queue的第一个元素，并删除之
            print(node.elem)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)



if __name__ == '__main__':
    L = range(1,11)
    tree = Tree()

    for i in L:                 #新建树并赋值
        tree.add(i)

    print('layer:')
    tree.layer(tree.root)

    print('front_recursion:')
    tree.front_recursion(tree.root)

    print('middle_recursion:') 
    tree.middle_recursion(tree.root)

    print('behind_recursion:')
    tree.behind_recursion(tree.root)

    print('front_stack:')
    tree.front_stack(tree.root)

    print('middle_stack:')
    tree.middle_stack(tree.root)

    print('behind_stack:')
    tree.behind_stack(tree.root)
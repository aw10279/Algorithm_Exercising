# coding: utf-8

class Node(object):  #�����ڵ���,�����ݡ���������3������
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object): #�������࣬�и��ڵ����ԣ�queue������¼����������ȫ�Ľڵ㣻�����к������ڴ����¶���
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:  #�����ڵ�Ϊ�գ���ֵ�����ڵ�
            self.root = node
            self.queue.append(self.root)
        else:
            t_node = self.queue[0]  
            if t_node.lchild == None:  #��������Ϊ�գ���ֵ��������
                t_node.lchild = node
                self.queue.append(t_node.lchild)
            else:
                t_node.rchild = node  #��Ϊ�գ���ֵ����
                self.queue.append(t_node.rchild)
                self.queue.pop(0)  #���Ҷ��Ѹ�ֵ�Ľڵ㣬��queue��ɾ��

    def front_recursion(self, root): #�ݹ�-�������
        if root == None:
            return
        print(root.elem)
        self.front_recursion(root.lchild)
        self.front_recursion(root.rchild)

    def middle_recursion(self, root): #�ݹ�-�������
        if root == None:
            return
        self.middle_recursion(root.lchild)
        print(root.elem)
        self.middle_recursion(root.rchild)

    def behind_recursion(self, root): #�ݹ�-�������
        if root == None:
            return
        self.behind_recursion(root.lchild)
        self.behind_recursion(root.rchild)
        print(root.elem)

    def front_stack(self, root):      #��ջ-�������
        if root == None:
            return
        stack = []  #��¼���д������ڵ�
        node = root
        while node or stack:
            while node:  #��ѭ��һֱ�������������˳����������ͷ
                print(node.elem)
                stack.append(node)
                node = node.lchild
            node = stack.pop()  #nodeָ���ջ�����һ��Ԫ�أ�ͬʱɾ����Ԫ�أ�Ҫָ���������Ľڵ���Ӷ�ջɾ�����´β���ָ���ϲ㣩
            node = node.rchild  #ָ��������

    def middle_stack(self, root):      #��ջ-�������
        if root == None:
            return
        stack = []  
        node = root
        while node or stack:
            while node:  #��ѭ��һֱ�������������˳����������ͷ����������κ�����
                stack.append(node)
                node = node.lchild
            node = stack.pop()
            print(node.elem)    #nodeָ���ϲ㲢ɾ������������ݣ�Ȼ��ָ��������
            node = node.rchild

    def behind_stack(self, root):     #��ջ-�������
        if root == None:
            return
        stack1 = []  #stack1�����¼�������ڵ㣬stack2�������򴢴�ڵ㣬��������������
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.lchild:
                stack1.append(node.lchild)
            if node.rchild:
                stack1.append(node.rchild)
            stack2.append(node)  #�����������ҵĽڵ����stack2����˳��Ϊ�������������
        while stack2:
            print(stack2.pop().elem)

    def layer(self, root):           #��α���
        if root == None:
            return
        queue = []
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)  #ÿ��ѭ����ָ��queue�ĵ�һ��Ԫ�أ���ɾ��֮
            print(node.elem)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)



if __name__ == '__main__':
    L = range(1,11)
    tree = Tree()

    for i in L:                 #�½�������ֵ
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
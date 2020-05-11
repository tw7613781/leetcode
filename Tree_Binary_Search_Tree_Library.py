# https://www.laurentluce.com/posts/binary-search-tree-library-in-python/comment-page-1/
# 学习上面的blog之后写个binary search tree的library

class Node:
    # 在class中self就等于调用class方法的class对象
    def __init__(self,data):
        '''
        node constructor
        @param data: any data type
        '''
        self.val = data
        self.left = None
        self.right = None

    def insert(self, data):
        '''
        插入data到BST中,根据BST的定义,data不能等于tree的node
        @param data: any data type
        '''
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data
            self.left = None
            self.right = None

    def lookup(self, data, parent=None):
        '''
        查找BST中是否有data,有的话返回这个node和它的父节点,没有的话返回None, None
        @param data: BST的Node中包含的val的数据类型
        @param parent: Node类型，递归的时候要用到
        '''
        if data < self.val:
            if self.left is None:
                return None, None
            else:
                self.left.lookup(data,self)
        elif data > self.val:
            if self.right is None:
                return None, None
            else:
                self.right.lookup(data,self)
        # 不大也不小,找到了,返回自己和父节点
        else:
            return self, parent

    def delete(self, data):
        '''
        删除值为data的节点,难点在于删除之后,要重建BST,分为被删除节点有0个子节点,1个子节点,2个子节点三个情况,没有返回
        @param data: 要被删除的数
        '''
        node, parent = self.lookup(data)
        if node:
            children_count = node.children_count()
            # 直接删除此节点,把父节点对应的位置设了None
            if children_count == 0:
                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.val = None
            # 如果有一个子节点,把这个节点代替自己
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if node == parent.left:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self = n
            # 如果有二个子节点,我们要找这个节点的后继节点,把后继节点代替被删节点,同时要修改后继节点的父节点的指向
            # 当找到后继节点后,把后继节点的值给被删节点,如果获得后继节点的父节点来操作,被删节点的父节点没有关系
            else:
                # 找后继节点
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 找到了交换
                node.val = successor.val
                # 修改后继节点的父节点的指向
                if parent.left == successor:
                    parent.left = None
                else:
                    parent.right = None

    def print_tree(self):
        '''
        没有参数,按照深度优先打印,也是BST排序的位置
        :return: 没有
        '''
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()

    def children_count(self):
        # 没有参数,返回调用函数的节点有几个子节点
        res = 0
        if self.left:
            res+=1
        if self.right:
            res+=1
        return res

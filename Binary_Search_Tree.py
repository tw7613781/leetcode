class node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


root=node(4)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(7)

root.data= 3
root.left.right.data = 4

def checkBST(root):
    min = 0
    max = 10000
    return isBST(root, min, max)

# traverse each node 1 time. make a value limitations that make sure
# maximun of left side nodes value is less that the node value
# and the minimum value of right side nodes is greater than the node value
def isBST(root, min, max):
    if root is None:
        return True

    if root.data < min or root.data > max:
        return False

    return isBST(root.left, min, root.data-1) and isBST(root.right, root.data+1, max)


print checkBST(root)














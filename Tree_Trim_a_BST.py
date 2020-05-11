# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # good code
    def trimBST(self,root,L,R):
        if root == None:
            return None

        if L > root.val:
            return self.trimBST(root.right, L, R)

        elif R < root.val:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root
    # my code
    def trimBST(self, root, L, R):
        if root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            if root.left:
                if root.left.val < L:
                    root.left = root.left.right
                    root.left = self.trimBST(root.left,L,R)
                else:
                    root.left = self.trimBST(root.left, L, R)
            if root.right:
                if root.right.val > R:
                    root.right = root.right.left
                    root.right = self.trimBST(root.right, L, R)
                else:
                    root.right = self.trimBST(root.right, L, R)
            return root



    # def trimBST(self, root, L, R):
    #     """
    #     :type root: TreeNode
    #     :type L: int
    #     :type R: int
    #     :rtype: TreeNode
    #     """
    #     if not root:
    #         return None
    #     if root.val < L:
    #         return self.trimBST(root.right, L, R)
    #     elif root.val > R:
    #         return self.trimBST(root.left, L, R)
    #     else:
    #         while root.left and root.left.val < L:
    #             self.left_delete(root, root.left)
    #         while root.right and root.right.val > R:
    #             self.right_delete(root, root.right)
    #         return root
    #
    # def left_delete(self, father, node):
    #     # the deleting node has no right subtree, delete the node and left subtree (father's left child assign None)
    #     if not node.right:
    #         father.left = None
    #     # the deleting node has right subtree
    #     else:
    #         # find successor of the node be deleted, the parent is the successor's parent
    #         parent = node
    #         successor = node.right
    #         while successor.left:
    #             parent = successor
    #             successor = successor.left
    #         # replace successor's value with the node be deleted
    #         node.val = successor.val
    #         # delete successor
    #         if successor == parent.left:
    #             parent.left = None
    #         else:
    #             parent.right = None
    #         # delete the left child tree of the node be deleted
    #         node.left = None
    #
    # def right_delete(self, father, node):
    #     if not node.left:
    #         father.right = None
    #     else:
    #         parent = node
    #         successor = node.left
    #         while successor.right:
    #             parent = successor
    #             successor = successor.right
    #         node.val = successor.val
    #         if successor == parent.left:
    #             parent.left = None
    #         else:
    #             parent.right = None
    #         node.right = None

    # '''
    # New idea, whoch is convert tree to list, then filter list by scope provided by question, finally make BST again
    # but prove wrong, as we don't know the sequence when make BST
    # '''
    # def trimBST(self, root, L, R):
    #     # if root is None, return Noe
    #     if not root:
    #         return None
    #     # convert all node value to list ascendingly.
    #     nodeList = []
    #     nodeList = self.printBST(root, nodeList)
    #     # remove all nodes that not in the scope and make a new
    #     newList = []
    #     for i, v in enumerate(nodeList):
    #         if v <= L and v >= R:
    #             newList.append(v)
    #     # find new root
    #     if root.val in newList:
    #         rootNode = root.val
    #     elif root.val < L:
    #         rootNode = newList[0]
    #     elif root.val > R:
    #         rootNode = newList[-1]
    #     newhead = None
    #     self.insertBST(newhead, rootNode)
    #     for i, v in enumerate(newList):
    #         self.insertBST(v)
    #     return newhead
    #
    # def printBST(self, head, res):
    #     if head.left:
    #         res = self.printBST(head.left, res)
    #     res.append(head.val)
    #     if head.right:
    #         res = self.printBST(head.right, res)
    #     return res
    #
    # def insertBST(self, head, value):
    #     if head:
    #         if value < head.val:
    #             if head.left:
    #                 self.insertBST(head.left)
    #             else:
    #                 head.left = TreeNode(value)
    #         if value > head.val:
    #             if head.right:
    #                 self.insertBST(head.right)
    #             else:
    #                 head.right = TreeNode(value)
    #     else:
    #         head.val = value
    #         head.left = None
    #         head.right = None

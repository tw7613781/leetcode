# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
# use a DSF to convert the target tree to list, then use set to remove duplicate then use sorted to sort the list, then the second element is the answer


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.list = []

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.convertToList(root)
        res = sorted(list(set(self.list)))
        if len(res)>1:
            return res[1]
        else:
            return -1

    def convertToList(self, root):
        '''
        convert BT to list
        :param root: root node of a BT
        :return: return a list to global var list
        '''
        if root:
            self.convertToList(root.left)
            self.list.append(root.val)
            self.convertToList(root.right)

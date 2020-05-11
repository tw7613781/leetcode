# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# brute-force algorithm, but in BST, finding a element is O(log(n)),that is the advantage

class treeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def findTarget(self, root, k):
        return self.traverse(root, root, k)


    def traverse(self, root, run, k):
        '''
        traverse the BST, and for each node try to find if there is another node which add up to be the target
        :param root: BST root, pass to findAonther()
        :param run: current node
        :param k: target value
        :return: boolean
        '''
        if run:
            if self.traverse(root, run.left, k):
                return True
            if self.findAnother(root, run, k):
                return True
            if self.traverse(root, run.right, k):
                return True
            return False

    def findAnother(self, root, run, k):
        '''
        find a value at BST, if found, return True, not found, return False
        :param root: BST root
        :param run: the node that need find another
        :param k: target value
        :return: boolean
        '''
        target = k - run.val
        if target == run.val:
            return False
        if root:
            if target == root.val:
                return True
            elif target < root.val:
                return self.findAnother(root.left, run, k)
            else:
                return self.findAnother(root.right, run, k)
        else:
            return False

head = treeNode(2)
head.left = treeNode(1)
head.right = treeNode(3)
solution = Solution()
print(solution.findTarget(head,4))
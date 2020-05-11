# https://leetcode.com/problems/construct-string-from-binary-tree/description/
# the first submission result was Time Limit Exceeded as I use list.append() to make self.res that was list before
# the second submission result is accept as I use str to make self.res. It reveal that list append operation is time consuming than str + operation

class Solution:
    def __init__(self):
        self.res = ''

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.function(t)
        return self.res

    def function(self, t):
        if t:
            self.res += str(t.val)
            if t.left or t.right:
                self.res += '('
                self.tree2str(t.left)
                self.res += ')'
            if t.right:
                self.res += '('
                self.tree2str(t.right)
                self.res += ')'

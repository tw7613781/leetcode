# https://leetcode.com/problems/merge-two-binary-trees/description/

# binary tree node
class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        # type t1: TreeNode
        # type t2: TreeNode
        # rtype: TreeNode
        # 如果两个点都有值,返回他们的和
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            # 左子树也是相同的策略
            root.left = self.mergeTrees(t1.left, t2.left)
            # 右子树也是相同的策略
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        # 不然返回左子树或者右子树
        else:
            return t1 or t2

    def makeTreeFromList(self, s):
        # s: list []
        # rtype: TreeNode

        # if s is none, just return with None
        if not s:
            return None

        # convert all elements in list into TreeNodes
        sTree = [TreeNode(x) if x else None for x in s]

        length = len(sTree)

        for i, sNode in enumerate(sTree):

            if sNode:

                # calculate left node index
                left_index = i * 2 + 1
                if  left_index < length:
                    sNode.left = sTree[left_index]

                # calculate right node index
                right_index = i * 2 + 2
                if right_index < length:
                    sNode.right = sTree[right_index]

        # 如果是None直接打印None了，不然看看左右子节点是不是空，不是的话输出保存的值
        for sNode in sTree:
            if sNode:
                print(sNode.val, sNode.left.val if sNode.left else None, sNode.right.val if sNode.right else None )
            else:
                print(None)

        return sTree[0]

    def makeTreeFromListFindFather(self, s):
        # s: list []
        # rtype: TreeNode

        # if s is none, just return with None
        if not s:
            return None

        # convert all elements in list into TreeNodes, if the elements is None, convert it to None
        sTree = [TreeNode(x) if x else None for x in s]

        length = len(sTree)
        

        for x in range(length-1, -1, -1):

            parentNode = int((x-1)/2)

    def traverseBread_thFirst(self, root):
        # root: TreeNode
        # rtype: None
        res = []
        if not root:
            return res
        queue = []
        queue.insert(0, root)
        while queue:
            run = queue.pop()
            if run:
                res.append(run.val)
            else:
                res.append(None)
                continue
            if run.left:
                queue.insert(0, run.left)
            if root.right:
                queue.insert(0, run.right)
        return res


s = [0,1,2,3,4,5,6,7,8,9,10]
s = []
s1 = [2,1,3,None,4,None,7]
s2 = [1,3,2,5]
s1 = [1,2,None,3]
s2 = [1,None,2,None,3]
s1 = [1,2,3,4,5]
s2 = [1,2,3]

solution = Solution()
# solution.mergeTrees(s1,s2)
s1 = solution.makeTreeFromList(s1)
# print(solution.traverseBreadthFirst(s1))
s2 = solution.makeTreeFromList(s2)

s3 = solution.mergeTrees(s1,s2)
print(solution.traverseBread_thFirst(s3))
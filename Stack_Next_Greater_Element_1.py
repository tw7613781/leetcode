# https://leetcode.com/problems/next-greater-element-i/description/
# 跟stack_Daily来第二个找_Temperatures一样，核心都是找数组中下一个比自己大得数字，因为有两个数组，第一个用了一个hash到第二个找

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        res = []

        for i, v in enumerate(nums2):
            dict[v] = i

        nextGreater = self.findNextGreater(nums2)

        for i, v in enumerate(nums1):
            pos = dict[v]
            res.append(nextGreater[pos])
        return res

    def findNextGreater(self, s):
        # s: int array
        # r: int array
        stack = []
        nextGreater = [-1] * len(s)
        for i, v in enumerate(s):
            while stack and v > s[stack[-1]]:
                index = stack.pop()
                nextGreater[index] = v
            stack.append(i)
        return nextGreater


solution = Solution()
s = [1,3,4,2]
print(solution.findNextGreater(s))
num1=[4,1,2]
num2=[1,3,4,2]
print(solution.nextGreaterElement(num1,num2))
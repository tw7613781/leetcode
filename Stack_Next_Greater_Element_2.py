# https://leetcode.com/problems/next-greater-element-ii/description/
# 在1的基础上，只是把输入数组翻倍就行了，其他的保持不变
class Solution:
    def nextGreaterElement(self, nums):

        length = len(nums)
        stack = []
        res = [-1]*length*2
        nums = nums + nums
        for i, v in enumerate(nums):
            while stack and v > nums[stack[-1]]:
                index = stack.pop()
                if i >= length:
                    res[index] = i-length
                else:
                    res[index] = i
            stack.append(i)
        return res[:int(len(res)/2)]


solution = Solution()
s = [1,3,4,2]
print(solution.nextGreaterElement(s))
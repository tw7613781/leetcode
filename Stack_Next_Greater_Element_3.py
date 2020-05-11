# https://leetcode.com/problems/next-greater-element-iii/description/
# 基本思路从右往左边找到第一个小的数字，然后跟右手边最小的数字交换，然后再次把右手边的数字从小到大排序。有个陷阱是是说说有的数字要小于32bit，所以最大的signed数字是2的31次方-1.但是从test set来看超过1000000000就能返回-1了


class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n >= 1000000000: return -1
        n = [int(x) for x in str(n)]

        stack = []
        tag = 0

        for i in range(len(n)-1,-1,-1):
            while stack and n[i] < n[stack[-1]]:
                index = stack.pop()
                tag = 1
            if tag == 1: break
            stack.append(i)
        if tag == 0: return -1
        n[index], n[i] = n[i], n[index]
        newEnding = sorted(n[i+1:])
        resList = n[:i+1] + newEnding
        return int(''.join(map(str,resList)))

n=45321
# n = 36521
# n= 12
# n=21
# n=89116521
n=1000000000
solution =Solution()
print(solution.nextGreaterElement(n))

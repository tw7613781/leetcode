# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
# 很多方法，包括往右移动一位再作XOR操作等等。这个方法最直观，变成二进制之后，保证没有连续两个00或者连续两个11就行了。

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return '00' not in bin(n) and '11' not in bin(n)

solution = Solution()
res = solution.hasAlternatingBits(5)
print(res)

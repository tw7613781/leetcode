# https://leetcode.com/contest/weekly-contest-67/problems/prime-number-of-set-bits-in-binary-representation/
# 基本思路就是暴力穷举，对这一区间内的所有数字变成二进制，然后算出有多少个1，然后看这个数字是不是preme
# 时间复杂度，貌似因为求preme的算法不会走的很远，基本上是O(n*instant)


class Solution:

    def check_Preme(self, val):
        if val == 1: return False
        else:
            for x in range(2, val):
                if val % x == 0:
                    return False
            return True

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        output = 0
        for x in range(L, R + 1):
            count = 0
            for ch in bin(x):
                if ch == '1':
                    count += 1
            if self.check_Preme(count):
                output += 1
        return output

solution = Solution()
print(solution.countPrimeSetBits(10,15))
'''
https://leetcode.com/problems/climbing-stairs/
DP classical problem. keep in mind, DP is a brute force + buffer
'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = [0] * (n + 1) 
        steps[1] = 1
        steps[2] = 2
        for x in range(3, n+1):
            steps[x] = steps[x-1] + steps[x-2]
        return steps[n]

solution = Solution()
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(20))

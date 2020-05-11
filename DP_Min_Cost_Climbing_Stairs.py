# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# DP Bottom-Up, naturally memoization, O(n) Time complexity

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        sum = [0] * n
        for i in range(2, n):
            sum[i] = min(sum[i - 2] + cost[i - 2], sum[i - 1] + cost[i - 1])
        final = min(sum[-1] + cost[-1], sum[-2] + cost[-2])
        return final


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
solution = Solution()
print(solution.minCostClimbingStairs(cost))
# https://leetcode.com/problems/out-of-boundary-paths/description/
# using DP bottom-up, find the relation between i-1 step and i step, use numpy to operate 2D array, time complexity is O(m*n*M)
import numpy as np
class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N == 0: return 0
        # initialize a 2-array
        paths = np.zeros((m,n),dtype = np.int64)
        mod = 10**9 + 7
        # the paths for each coordinate after 1 move
        paths[0] += 1
        paths[-1] += 1
        paths[:,0] += 1
        paths[:,-1] += 1
        sumPaths = paths
        for _ in range(N-1):
            prevPaths = paths % mod
            paths = prevPaths - prevPaths
            paths[1:] += prevPaths[:-1]
            paths[:-1] += prevPaths[1:]
            paths[:,1:] += prevPaths[:,:-1]
            paths[:,:-1] += prevPaths[:,1:]
            sumPaths += paths
        res = sumPaths[i,j] % mod
        return int(res)

m,n,N,i,j = 2,2,2,0,0
# m = 1
# n = 3
# N = 3
# i = 0
# j = 1
solution = Solution()
print(solution.findPaths(m,n,N,i,j))


# Numpy test
# maps = np.zeros((1,2),np.int64)
# maps[0] += 1
# maps[-1] +=1
# maps[:,0] +=1
# maps[:,-1] +=1
# maps += 100
# print(maps)
# print(maps[1:])
# print(maps[:-1])
# print(maps[:,1:])

# Numpy test
# for i in range(3):
#     for j in range(4):
#         print(maps[i,j])
#     print('--------------')

# The solution is DP up-down without cache, time complexity is O(4^N), submission result is time exceeds
# class Solution:
#     def __init__(self):
#         self.count = 0
#         self.cache = {}
#
#     def findPaths(self, m, n, N, i, j):
#         """
#         :type m: int
#         :type n: int
#         :type N: int
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#
#         if N == 0: return 0
#
#         if i+1 > m-1: self.count += 1
#         else:
#             self.findPaths(m,n,N-1,i+1,j)
#         if j+1 > n-1: self.count += 1
#         else:
#             self.findPaths(m,n,N-1,i,j+1)
#         if i-1 < 0: self.count += 1
#         else:
#             self.findPaths(m,n,N-1,i-1,j)
#         if j-1 < 0: self.count += 1
#         else:
#             self.findPaths(m,n,N-1,i,j-1)
#         return self.count % (1000000007)
#
# m,n,N,i,j = 2,2,2,0,0
# m = 1
# n = 3
# N = 3
# i = 0
# j = 1
# solution = Solution()
# print(solution.findPaths(m,n,N,i,j))
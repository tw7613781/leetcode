class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix[0])
        n = len(matrix)

        for i in range(0,n):
            scope = m if i ==0 else 1
            for j in range(0, scope):
                target = matrix[i][j]
                k= 1
                while i+k < n and j+k < m:
                    if matrix[i+k][j+k] != target:
                        return False
                    k+=1
        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix =[[1,2,3],[2,3,4],[7,8,9]]
matrix = [[1,2,3,4],[5,1,2,3],[9,6,1,2]]
solution = Solution()
print(solution.isToeplitzMatrix(matrix))
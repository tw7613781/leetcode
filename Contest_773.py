class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        transfrom = [[1,2,3],[4,5,0]]
        res = self.finding(board, transfrom, 0)


    def finding(self, board, transform, step):
        if board == transform:
            return step
        i,j = self.findZero(transform)
        if i + 1 < 2:
            transform[i][j], transform[i+1][j] = transform[i+1][j], transform[i][j]

    def findZero(self, transform):
        for i in len(2):
            for j in len(3):
                if transform[i][j] == 0:
                    break
        return (i,j)
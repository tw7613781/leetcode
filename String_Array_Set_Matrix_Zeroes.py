
def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(0,n):
        i_has_0 = 0
        for j in range(0,m):
            if matrix[i][j] == 0:
                i_has_0 = 1
                for x in range(0, i+1):
                    matrix[x][j] = 0
                for x in range(i+1,n):
                    if matrix[x][j] != 0:
                        matrix[x][j] = None
            if matrix[i][j] == None:
                matrix[i][j] = 0
            print(matrix)
        if i_has_0 == 1:
            matrix[i] = [0]*m

matrix = [[1,1,1,1],[1,0,1,0],[1,1,1,1]]

matrix = [[0,1,1,1],[1,1,1,1],[1,1,1,1]]

matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,1]]

matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]

solution(matrix)
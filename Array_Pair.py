A = [8,3,3,4,4,2,6,5,5,2,6]

def solution(A):
    A.sort()
    i = 0
    while i<len(A):
        if i == len(A)-1:
            return A[i]
        if(A[i] == A[i+1]):
            i=i+2
        else:
            return A[i]

print solution(A)
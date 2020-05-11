A = [-1, -2, -3, -4, -5, -6]

def solution(A, K):
    B = [0] * len(A)
    N = len(A)
    if N == 0:
        return A
    if K > N:
        K = K % N
    if K == N or K == 0:
        return A
    else:
        i = 0
        while i < N:
            B[(i+K)%N] = A[i]
            i = i + 1
        return B



print solution(A,10)
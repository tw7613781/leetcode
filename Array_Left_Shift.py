a = [1, 2, 3, 4, 5]

a = [1]

def solution(a,n,k):
    b = [0] * n
    if k == n:
        return a
    else:
        i = 0
        while i < n:
            if (i - k) >= 0:
                b[i-k] = a[i]
            else:
                b[n-(k-i)] = a[i]
            i = i + 1

        return b



print solution(a,1,1)
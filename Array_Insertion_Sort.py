def InsertionSort(A):
    for end in range(1,len(A)):
        i = end - 1
        val = A[end]
        while i > -1 and val < A[i]:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = val
    return A

A = [6,5,4,3,2,1]
A = InsertionSort(A)
print A 
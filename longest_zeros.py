def solution(N):
    str = bin(N)
    length = len(str)
    maxLength = 0
    currentLength = 0
    for char in str[2:]:
        if char == '0':
            currentLength = currentLength+1
        else:
            maxLength = max(currentLength,maxLength)
            currentLength=0
    return maxLength


print solution(9)
print solution(529)
print solution(20)
print solution(15)

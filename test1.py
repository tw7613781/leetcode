
S = "BBBAABABBBCCBCBBCACB"

def solution(S):

    S = S.replace('B','')

    result = []
    previous = 'B'
    for chr in S:
        if chr != previous:
            result.append(chr)
        previous = chr
    return ''.join(result)


print solution(S)
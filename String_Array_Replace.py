def solution(S, L):
    replace = '%20'
    output = ''
    for i in range(0,L):
        if S[i] == ' ':
            output += replace
        else:
            output +=S[i]
    return output

S = 'Mr Jonh Smith      '
L = 13
print(solution(S,L))


def solution(s):
    hash_char = [0]*26
    for ch in s:
        hash_char[ord(ch)-ord('a')] += 1
    print(hash_char)
    pos = 0
    for ch in s:
        if hash_char[ord(ch)-ord('a')] == 1:
            return pos
        pos+=1
    return -1



print(solution('zz'))
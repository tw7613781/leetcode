def NumToCharList(num):
    return [i for i in str(num)]

def solution(s):
    target = []
    count = 1
    for i,ch in enumerate(s):
        if i==len(s)-1:
            if count!=1:
                target+=ch
                target+=NumToCharList(count)
                break
            else:
                target+=ch
                break
        if s[i]==s[i+1]:
            count+=1
        else:
            target+=ch
            if count!=1:
                target+=NumToCharList(count)
            count=1
    return target

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    count = 1
    write = 0
    for i, ch in enumerate(chars):
        if i == len(chars) - 1 or chars[i] != chars[i + 1]:
            if count != 1:
                chars[write] = ch
                write += 1
                for j in str(count):
                    chars[write] = j
                    write += 1
                count = 1
            else:
                chars[write] = ch
                write += 1
        else:
            count += 1
    # print(write)
    return chars


s = ['a','c','c','c','c','c','c','c','c','c','c','c','c']
s = ['a']
s = ['a','s','a','a','b','b','b','c','c','c','b','b']
print(compress(s))
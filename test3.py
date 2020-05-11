A = "(())))("
A = "(())"
A = "))"

def solution(A):
    co_count=0
    for ch in A:
        if ch == ')':
            co_count+=1

    op_count = 0
    i=0
    for ch in A:
        if ch == '(':
            op_count+=1
        else:
            co_count-=1
        if(op_count == co_count):
            return i+1
        i+=1

print solution(A)
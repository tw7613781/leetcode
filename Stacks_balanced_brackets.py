def is_matched(expression):
    list = []
    for ch in expression:
        if ch == '(' or ch =='[' or ch =='{':
            list.append(ch)
        else:
            if not list:
                return False
            temp = list.pop()
            if temp == '(':
                if ch != ')':
                    return False
            elif temp == '[':
                if ch != ']':
                    return False
            else:
                if ch != '}':
                    return False
    if not list:
        return True
    else:
        return False

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

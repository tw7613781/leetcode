'''
Hi, here's your problem today. This problem was recently asked by Uber:

Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
'''

class Solution:
    def isValid(self, s):
        stack = []
        char_map = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for c in s:
            if c in char_map.keys():
                stack.append(c)
            else:
                if len(stack) == 0: return False
                else:
                    value = stack.pop()
                    if c != char_map[value]:
                        return False
        if len(stack) != 0: return False
        return True
  
# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))
  
s = ""
# should return True
print(Solution().isValid(s))
  
s = "([{}])()"
# should return True
print(Solution().isValid(s))
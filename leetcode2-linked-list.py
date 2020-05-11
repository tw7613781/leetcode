# Problem description

'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

The answer can be tested at leetcode 2
'''

import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        carrier, r1, r2 = 0, l1, l2
        ret = ListNode('Temp')
        r = ret
        while r1 or r2:
            s = 0
            if r1: s += r1.val
            if r2: s += r2.val
            if carrier: s += carrier
            if s >= 10:
                value = s % 10
                carrier = 1
            else:
                value = s
                carrier = 0
            r.next = ListNode(value)
            r = r.next
            if r1: r1 = r1.next
            if r2: r2 = r2.next
        if carrier:
            r.next = ListNode(carrier)
        return ret.next
    
    def input(self, number):
        if number < 0: return None
        if number < 10: return ListNode(number)
        first = number % 10
        p = ListNode(first)
        r = p
        number = number // 10
        while number:
            remainder = number % 10
            number = number // 10
            r.next = ListNode(remainder)
            r = r.next
        return p
    
    def print(self, l1):
        ret = ''
        while l1:
            ret += str(l1.val)
            l1 = l1.next
        print(ret[::-1])

s = Solution()
arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])
number1 = s.input(arg1)
number2 = s.input(arg2)
s.print(number1)
s.print(number2)
result = s.addTwoNumbers(number1, number2)
s.print(result)

# 7 0 8
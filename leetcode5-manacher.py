'''
Hi, here's your problem today. This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"

'''

'''
key points of manacher algorithem

1. By using the symmetric of palindromic, reduce duplicate searching space
2. By constructing a new string, unify odd and even number of string's solution 
'''


class Solution: 
    def longestPalindrome(self, s):
        s = '#' + '#'.join(s) + '#'
        m = 0
        res = [0]*len(s)
        max_right = 0
        pos = 0
        for i in range(len(s)):
            if i < max_right:
                res[i] = min(res[2*pos-i], max_right-i)
            else:
                res[i] = 1
            while i-res[i] >= 0 and i+res[i] < len(s) and s[i-res[i]] == s[i+res[i]]:
                res[i] += 1
            if res[i] > m:
                m = res[i] - 1
                location = i
            if res[i]+i-1 > max_right:
                max_right = res[i]+i-1
                pos = i
        return ''.join(s[location-m:location+m+1].split('#'))    

        
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
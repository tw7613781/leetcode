'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
'''

class Solution:

    def lengthOfLongestSubstring(self, s):
        l = res = 0
        memo = {}
        for r,x in enumerate(s):         
            if x in memo:                  # when we meet repeating characters( substring does not meet requirement, update left pointer)
                l = max(l, memo[x] + 1)    # why don't we use "l = memo[x] + 1"? refer to testcase like 'abba'
            memo[x] = r                    # update new index for character x (memo[x] will always be the largest index in the characters we visited)
            res = max(res, r - l + 1)      # inclusive, l: first index of the string, r: last index of the string
        return res

ret = Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
print(ret)
# 10
ret = Solution().lengthOfLongestSubstring('')
print(ret)
# 0
ret = Solution().lengthOfLongestSubstring('a')
print(ret)
# 1
ret = Solution().lengthOfLongestSubstring('abcabcdefga')
print(ret)
# 3
ret = Solution().lengthOfLongestSubstring('pwwkew')
print(ret)
# 3


'''
The answer is from danielduochen in leetcode

General idea: For sliding window questions, we usually keep left side fixed, and increment right side step by step until we reach the substring that does not meet the requirement, then we keep right side fixed, and move left side step by step until the substring meet the requirement again.

Specifically, we use a hashtable "memo" to record the largest index of each character we visited, why is the largest index? when we encounter a substring that does not meet the requirement, we need this information to tell left side where to move.

Helpful questions before coding:
"How do we know the current substring does not meet the requirement?"
assume "x" is the current character, if "x" appears in "memo" before

"How to update left pointer when the substring does not meet the requirement?"
we use l = max(l, memo[x] + 1)
ex: s = "abba", when we reach index = 3, x = 'a', memo['a'] = 0 in this case, but l = 2 already because we move the left pointer before, thus l = max(l, memo[x] + 1) = max(2, 0 + 1) = 2
'''
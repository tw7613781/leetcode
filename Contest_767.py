# https://leetcode.com/contest/weekly-contest-68/problems/reorganize-string/

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # sort S by character occurrence, return value is a list
        S = sorted(sorted(S), key=S.count, reverse=True)
        # find the middle point
        length = len(S)
        middle = int((length-1)/2)+1
        # i start from 0, j start from middle point. append S[i] and S[j] in turn
        res = []
        i,j=0,middle
        while i<middle and j<length:
            if S[i] == S[j]:
                return ''
            else:
                res.append(S[i])
                res.append(S[j])
            i += 1
            j += 1
        # if the length is even number, append the one just before middle point
        if i == middle-1:
            res.append(S[i])
        return ''.join(i for i in res)




s='aaabb'
s='aab'
s='ksdalkjfkldsjfl'
s="abbabbaaab"
solution = Solution()
print(solution.reorganizeString(s))

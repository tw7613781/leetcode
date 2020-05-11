class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Jlist = [x for x in J]
        Slist = [x for x in S]
        ct = 0
        for stone in Slist:
            if stone in Jlist:
                ct+=1
        return ct
J = "aA"
S = ""

solution = Solution()
print(solution.numJewelsInStones(J,S))

# https://leetcode.com/contest/weekly-contest-67/problems/partition-labels/
# 基本思路是首先找到每个字符的最后出现的位置
# 然后从字符串头开始遍历这个字符串，要保证当前的字符的位置要小于此字符出现的最后位置，在遍历的过程中，要动态更新最后的位置。
# 时间复杂度就是O(n)

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        output=[]
        map=[0]*26
        for i,ch in enumerate(S):
            map[ord(ch)-ord('a')]=i

        i=0
        while i<len(S):
            pos=map[ord(S[i])-ord('a')]
            start=i
            end=pos
            while i<end:
                i+=1
                pos=map[ord(S[i]) - ord('a')]
                end=max(pos,end)
            internal=end-start+1
            output.append(internal)
            i=i+1
        return output
solution=Solution()
print(solution.partitionLabels("ntswuqqbidunnixxpoxxuuupotaatwdainsotwvpxpsdvdbwvbtdiptwtxnnbtqbdvnbowqitudutpsxsbbsvtipibqpvpnivottsxvoqqaqdxiviidivndvdtbvadnxboiqivpusuxaaqnqaobutdbpiosuitdnopoboivopaapadvqwwnnwvxndpxbapixaspwxxxvppoptqxitsvaaawxwaxtbxuixsoxoqdtopqqivaitnpvutzchkygjjgjkcfzjzrkmyerhgkglcyffezmehjcllmlrjghhfkfylkgyhyjfmljkzglkklykrjgrmzjyeyzrrkymccefggczrjflykclfhrjjckjlmglrmgfzlkkhffkjrkyfhegyykrzgjzcgjhkzzmzyejycfrkkekmhzjgggrmchkeclljlyhjkchmhjlehhejjyccyegzrcrerfzczfelzrlfylzleefgefgmzzlggmejjjygehmrczmkrc"))
print(solution.partitionLabels("ababcbacadefegdehijhklij"))


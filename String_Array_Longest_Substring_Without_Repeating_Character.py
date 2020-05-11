class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_map = {}
        start = max_length = 0
        s_set = set(s)
        max_possible = len(s_set)
        for i, c in enumerate(s):
            curr = index_map.get(c, -1)
            if start <= curr:
                start = curr + 1
            elif i - start + 1 > max_length:
                max_length = i - start + 1
                if max_length == max_possible:
                    return max_length
            index_map[c] = i
        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = [0] * 95
        maxi = 0
        current = 0

        for ch in s:
            index = ord(ch) - ord(' ')
            if hash_table[index] == 0:
                current += 1
                hash_table[index] = current
            else:
                maxi = max(maxi, current)
                duplicate = hash_table[index]
                i = 0
                while i < 95:
                    hash_table[i] -= duplicate
                    if hash_table[i] <= 0:
                        hash_table[i] = 0
                    i += 1
                current -= duplicate
                current += 1
                hash_table[index] = current
        maxi = max(maxi, current)
        return maxi
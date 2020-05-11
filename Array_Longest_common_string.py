def longestCommonPrefix(strs):
    num_of_str = len(strs)
    if num_of_str == 0: return ''
    if num_of_str == 1: return strs[0]
    any_str_len = len(strs[0])
    com_prefix = ''
    for index in range(any_str_len):
        for word_index in range(1, num_of_str):
            if index == len(strs[word_index]) or strs[word_index][index] != strs[word_index - 1][index]:
                return com_prefix
        com_prefix += strs[word_index][index]
    return com_prefix

data_set = ['','']
assert(longestCommonPrefix(data_set) == '')
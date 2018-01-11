def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    dict_char2index = {}
    last_index = 0
    max_len = 0
    index = 0
    while True:
        try:
            cur_char = s[index]
            if cur_char in dict_char2index:
                rep_index = dict_char2index[cur_char]
                if rep_index >= last_index:
                    len_substr = index - last_index
                    if len_substr > max_len:
                        max_len = len_substr
                    last_index = rep_index + 1
            dict_char2index[cur_char] = index
            index += 1
        except:
            len_substr = index - last_index
            if len_substr > max_len:
                max_len = len_substr
            break
    return max_len

lengthOfLongestSubstring('abba')
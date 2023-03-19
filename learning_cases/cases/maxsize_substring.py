from typing import Generator, Tuple, Optional

def lengthOfLongestSubstring(s:str):
    if not s:
        return 0
    left = 0
    max_len = 0
    char_dict = {}
    for i,c in enumerate(s):
        if c in char_dict and char_dict[c] >= left:
            left = char_dict[c] + 1
        char_dict[c] = i
        max_len = max(max_len, i - left + 1)
    return max_len


def lengthOfLongestSubstring2(s: str) -> Tuple[str, int]:
    """
    返回输入字符串的最长连续子串及其长度，且该子串中的所有字符均不相同

    Args:
        s: 输入的字符串

    Returns:
        最长连续子串及其长度的元组
    """
    if not s:
        return "", 0

    # 初始化指针等变量
    max_len = 0
    start = 0
    end = 0
    char_set = set()

    for i in range(len(s)):
        while s[i] in char_set:
            char_set.remove(s[start])
            start += 1

        char_set.add(s[i])

        # i+1是子串的右边界，即对s切片时不包含i+1
        if i+1 - start > max_len:
            max_len = i+1 - start
            max_str = s[start:i+1] # 不包含位置i+1的元素

        print(max_str,max_len)
    return max_str, max_len


if __name__ == '__main__':
    # res = lengthOfLongestSubstring("ss1345ss1345612s134563579abcdefga")
    # print(res)
    res2 = lengthOfLongestSubstring2("ss1345ss1345612s134563579abcdefgabcd")
    print(res2)
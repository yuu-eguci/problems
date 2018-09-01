#!/usr/bin/env python
# coding: utf-8


# Given a string, find the length of the longest substring without repeating characters.

# "abcabcbb" -> 3
# Explanation: The answer is "abc", which the length is 3.

# "bbbbb" ->  1
# Explanation: The answer is "b", with the length of 1.

# "pwwkew" -> 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    # Empty string.
    if len(s) == 0:
        return 0

    # Chenhaoに教わったappend高速化テク。
    substring = []
    append = substring.append
    pop = substring.pop

    # 一文字目からカウントしていきます。
    longest = 0
    for char in s:

        # 文字がダブったときはダブりがなくなるまで substring を縮めます。
        while char in substring:
            pop(0)

        # substring に文字を追加します。
        append(char)

        # カウンター更新。
        if len(substring) > longest:
            longest = len(substring)

    return longest


test_cases = [
    "abcabcbb",  # 3
    "bbbbb",  # 1
    "pwwkew",  # 3
    " ",  # 1
    "au",  # 2
    "dvdf",  # 3
]
for case in test_cases:
    print(lengthOfLongestSubstring(case))

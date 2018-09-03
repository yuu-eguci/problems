
# https://leetcode.com/problems/longest-palindromic-substring/description/
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# "babad" -> "bab" or "aba"
# "cbbd" -> "bb"

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    # 最長回分。
    max_palindrome = ''

    # 左から1マスずつ見ます。文字単位ではない。
    for i in range(1, len(s)):

        # 要素と要素の間。
        base  = s[i:i]

        # 両側が同じとき回分です。
        palindrome = base
        j = 1
        while s[i-j:i-j+1] == s[i+j-1:i+j]:
            palindrome =s[i-j:i-j+1] + palindrome + s[i+j-1:i+j]
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome
            j += 1

        # 要素。
        base  = s[i:i+1]

        # 両側が同じとき回分です。
        palindrome = base
        j = 1
        while s[i-j:i-j+1] == s[i+j:i+j+1]:
            palindrome = s[i-j:i-j+1] + palindrome + s[i+j:i+j+1]
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome
            j += 1

    # 該当なければ一文字目を返します。
    return max_palindrome if max_palindrome else s[0:1]


test_cases = [
    "babad",  # "bab" or "aba"
    "cbbd",  # "bb"
    "ab",  # ""
    "aaaa",  # "aaaa"
    "abcba",  # "abcba"
]
for case in test_cases:
    print(longestPalindrome(case))

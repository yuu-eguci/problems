
# 正直これは "aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s" これが解けなくて答えをみた。
# さらに動的プログラミングのほうは理解できなくて普通の再起をみた。
# で答えみても "aaaaaaaaaaaaab" で Time Limit Exceeded になる。えぇ

# https://leetcode.com/problems/regular-expression-matching/description/
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    def foo(s, p):

        # パターンが尽きたとき、文字も尽きていればOK
        if not p:
            return not s

        # 一文字目のチェックです。
        matched = bool(s) and p[0] in ['.', s[0]]

        # p のほうが * 付の場合。
        if len(p)>=2 and p[1]=='*':

            # たとえ今回 matched してても次のパターンが優先。
            # それが True ならその結果で次の文字に進みます。
            return foo(s, p[2:]) or matched and foo(s[1:], p)

        # . や普通の文字の場合。
        else:
            return matched and foo(s[1:], p[1:])

    return foo(s, p)


test_cases = [
    ["aa", "a"],  # False
    ["aa", "a*"],  # True
    ["ab", ".*"],  # True
    ["aab", "c*a*b"],  # True
    ["mississippi", "mis*is*p*."],  # False
    ["mississippi", "mis*is*ip*."],  # True
    ["aaa", "a*a"],  # True
    ["aaa", "ab*a*c*a"],  # True
    ["ab", ".*.."],  # True
    ["aasdfasdfasdfasdfas", 
     "aasdf.*asdf.*asdf.*asdf.*s"],  # True
    ["ab", ".*c"],  # False
    # ["aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"],  # 
]
for case in test_cases:
    print(isMatch(case[0], case[1]))

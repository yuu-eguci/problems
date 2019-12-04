"""
Yukiさんはある文字列を間に何も挟まず繰り返し2回読み上げた。
同じ文字列を続けて2回読み上げたかチェックしよう。

yukicoderyukicoder -> YES
yukicoder -> NO
aaaa -> YES
aaaaa -> NO
"""

S = input()


def solve(S):

    # 文字数です。
    S_len = len(S)

    # 文字数が偶数ではない時点でダメです。
    # NOTE: べつに必要ない処理だけれど、下の「割る」処理が考えやすいから追加している。
    if S_len % 2 == 1:
        return 'NO'

    # 文字列を半分に割ります。
    #   前半: 最初から[長さの半分]でスライス
    #   後半: [長さの半分]から最後でスライス
    former = S[:S_len//2]
    latter = S[S_len//2:]

    # 前半と後半が同じであれば YES です。
    return former == latter and 'YES' or 'NO'
    # ↓これと同じ意味。「former == latter なら YES でなきゃ NO」と読む。
    # if former == latter:
    #     return 'YES'
    # return 'NO'


print(solve(S))

"""https://yukicoder.me/problems/no/458
N をそれぞれ異なる素数の和で表すことができる場合，その中での最大の和の回数 M を出力してください。
素数自身でしか表せない場合も含みます。
異なる素数の和で表すことができない場合は -1 を出力してください。
"""
# 最初に作ったやつ。答えは合うと思うんだけど、時間がぐちゃめちゃかかる。 N=3344 のときは一時間でも終わらなかった。

from math import sqrt
from itertools import combinations


def foo(N: int):

    # 2〜N の中の素数を列挙します。
    primes_in_N = get_primes_until_n(N)

    # 「は〜い i 人一組になって〜!」
    # 素数グループの中から、小さなグループを作っていきます。
    # グループの人数は、マックスからだんだん減らしていきます。
    for i in range(len(primes_in_N), 0, -1):
        # itertools.combinations は全組み合わせを作ってくれます。
        # N が大きくなるととんでもないパターン数になる箇所。
        for j, combination in enumerate(combinations(primes_in_N, i)):
            # 足して N になったらそれが答えです。
            if sum(combination) == N:
                return len(combination)

    # なかったら -1。
    return -1


def get_primes_until_n(N: int):
    """N までの素数一覧を返します。"""

    # 2〜N の dictionary です。
    # この先の処理で、素数でないものは False にしていきます。最終的に値が True のまま残った key が素数です。
    # NOTE: list にして、 index を key 扱いしたほうがイカすんだけど dictionary のほうがわかりやすいかと思って。
    dic = {i: True for i in range(2, N + 1)}

    # N の平方根までチェックすれば、全部の数の素数判定は終わります。
    for i in range(2, int(sqrt(N)) + 1):

        # すでに False(素数ではない)判定になっているものは計算不要です。
        if dic[i] is False:
            continue

        # 2 から始まるので、その先の倍数を全部 False(素数ではない)にしていけば最後には素数だけが True で残ります。
        j = i * 2
        while j <= N:
            dic[j] = False
            j += i

    return [i for i in dic.keys() if dic[i]]


# print(foo(18) == 3)
# print(foo(4) == -1)
# print(foo(3) == 1)
# print(foo(1) == -1)
# print(foo(3344) == 41)

# 提出用
print(foo(int(input())))

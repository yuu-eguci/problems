
"""ビットすごろく
https://yukicoder.me/problems/no/3

入力 N
1～Nのマスがある。1がスタートでNがゴール。
その場に書かれてる数字を2進数にしたときの1のビット数だけ前または後ろに進める。
1未満とN+1以上には移動できない。
正確にNに止まらないとゴールじゃない。

N(1<=N<=10k)を与えられたときゴールに到達できる最短の移動数を求めよ。
到達できない場合は-1。
"""

import time

start = time.time()
# ================================
# 処理、ここから。


"""概要
1. Nからスタート。
2. Nに来ることが可能なマスがあるか、Nより前、Nより後を見てみます。
   ただし戻りまくったり進みまくったりする必要はない。
   戻る範囲と進む範囲は、その数がある数値範囲のビットカウント最大値+1だけにします。
   数値範囲ごとのビットカウント最大値は下の bitcount(dictionary) に示してあります。
   +1してるのは、Nより後を見てる最中に次の最大値範囲に入っちゃうことを考慮しています。
3. その範囲中にNに来れるマスを reachable(set) に格納します。
4. reachable の中から進入禁止マスを除きます。
   0以下と、N+1以上のこと。
5. 残ったマスそれぞれを新たなNとして、手順1から繰り返します。ここで再帰関数を使っています。
6. もし reachable に1があれば繰り返さず、終了します。
   言い忘れていましたが手順5で count+1 しているのでそれを再帰関数の返り値にしています。
"""


# これは [1～2]範囲のビットカウント最大値は1 [3～6]範囲のビットカウント最大値は2 ～～～ [8191～16382]範囲のビットカウント最大値は13 であることを意味します。
bitcount = {2:1, 6:2, 14:3, 30:4, 62:5, 126:6, 254:7, 510:8, 1022:9, 2046:10, 4094:11, 8190:12, 16382:13, }
# 数値を与えるとその数値の範囲のビットカウント最大値を返します。手順2で使います。
def get_max_bitcount(n):
    for i in bitcount:
        if n <= i:
            return bitcount[i]


# 与えた数値setそれぞれへ到達できる数値をsetで返します。この中に1があれば終了します。
def get_reachable(st):
    reachable = set([])
    for l in st:
        # 手順2
        for i in range(1, get_max_bitcount(l)+1):
            fo, la = l-i, l+i
            fobi, labi = bin(fo).count('1'), bin(la).count('1')
            # 手順3
            if i == fobi:
                reachable.add(fo)
            elif i == labi:
                reachable.add(la)
    # 手順4
    return set(filter(lambda r: 1<=r<=N, reachable))


def foo(N):

    # 手順5
    def bar(st, count):
        # reachable がない(からっぽ)なら到達不可能。
        if not st:
            return -1
        # 手順6
        if 1 in st:
            return count
        return bar(get_reachable(st), count+1)

    if N == 1:
        return 1

    return bar(get_reachable(set([N])), 2)


print(foo(int(input())))


# 処理、ここまで。
# ================================
margin = time.time() - start
print(f'結果: {margin}秒')

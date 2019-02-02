
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
1.  みっつの配列を考えます。
    masu     [ 0,  1,  2,  3,  4 ...] ふつーにマス目番号
    distance [ 0,  1,  1,  2,  1 ...] 各マスにとまったときの移動可能数
    shortest [99,  1, 99, 99, 99 ...] 各マスに行くためにかかる歩数 マス1は最初から1
2.  マス1からスタート
3.  マス1から進む場合
        マス1から移動できる距離は distance[1]
        進む先のマス番号は 1+distance[1] これを dest とする。
        マス1に行くためにかかる最短歩数は shortest[1]
        マスdestまでに行くためにかかる最短歩数は shortest[1]+1
            これをマスdestまでに行くための今のところの最短歩数 shortest[dest] と比べる。
            より最短のほうが新しい shortest[dest] となる。
4.  マス1から戻る場合
        dest が 1-distance[1] になるだけであとは同じ。戻った先の最短歩数を更新する。
5.  マスnの場合
        dest = n+distance[n] (進む場合)
        dest = n-distance[n] (戻る場合)
        if shortest[n]+1 < shortest[dest]:
            shortest[dest] = shortest[n]+1
        みたいな感じ。
6.  最短距離の更新がなくなるまで 1～N を繰り返す。
7.  知りたいのはマスNへ行く最短歩数なので shortest[N] が答え。
        ただしその値が初期値から動いてないなら辿り着いてないので -1 を返す。
"""

"""ふしぎなこと
下のスクリプトでは進むほうだけに changed を置いているけどテストは通る。
逆に戻るほうにだけ置いても通る。
ってことは進むが発生したら絶対戻るが発生するってことか? それともたまたまか?
"""


def foo(N):

    distance = [bin(_).count('1') for _ in range(N+1)]
    shortest = [N for _ in range(N+1)]
    shortest[1] = 1

    changed = True
    while changed:
        changed = False

        for masu in range(1, N+1):

            dest = masu+distance[masu]
            if dest <= N:
                if shortest[masu]+1 < shortest[dest]:
                    shortest[dest] = shortest[masu]+1
                    changed = True

            dest = masu-distance[masu]
            if dest >= 1:
                if shortest[masu]+1 < shortest[dest]:
                    shortest[dest] = shortest[masu]+1

    return -1 if N!=1 and shortest[N]==N else shortest[N]


print(foo(int(input())))


# 処理、ここまで。
# ================================
margin = time.time() - start
print(f'結果: {margin}秒')

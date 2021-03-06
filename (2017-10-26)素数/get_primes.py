
'''
2 3 4 5 6 7 8 9 10 11
2の倍数を消す
2 3   5   7   9    11
3の倍数を消す
2 3   5   7        11
4は消えてる
5の倍数を消す
2 3   5   7        11
6は消えてる
7の倍数を消す……
ってやっていくと素数が残る。そういうロジックを使う。

終わりの数までずっとやっていく必要なくて、最大値の平方根まででよい。100なら10まで。
2*50 5*20 みたいに平方根以上の数は絶対平方根以下の組み合わせをもつ。


    2  3  4  5  6
 7  8  9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25

心配なのは平方根を超えた数の、倍数
だけど、平方根を超えた数の倍数でかつendまでに収まる数を作るには絶対平方根以下の数を相方に使わないといけない
平方根以上の数を相方に使ったらendを超えちゃうからそっちは心配いらない
よって、平方根を超えた数の倍数はチェック済み、または、対象外になる。
なんだー! ならおっけー!
'''

from math import sqrt

def get_primes(end):

    # boolスイッチ。素数じゃないもののスイッチをFalseにしていきます。
    switches = [b > 1 for b in range(end+1)]

    # 素数チェックはendの平方根まででOK。
    for i in range(int(sqrt(end))+1):

        # スイッチがFalseのものは、0,1,または下の倍数スイッチオフの対象になったものです。
        if switches[i] is False:
            continue

        # 素数を残しつつ、その倍数のスイッチをFalseにしていきます。
        j = i * 2
        while j <= end:
            switches[j] = False
            j += i

    # スイッチがTrueのものが素数です。
    return [i for i in range(len(switches)) if switches[i] is True]


if __name__ == '__main__':
    print(len(get_primes(100000)))

"""https://yukicoder.me/problems/no/458
N をそれぞれ異なる素数の和で表すことができる場合，その中での最大の和の回数 M を出力してください。
素数自身でしか表せない場合も含みます。
異なる素数の和で表すことができない場合は -1 を出力してください。
"""
# ナップサック問題の応用で、表の条件を「w 以下の重さ」ではなく「w ぴったりの重さ」に変更したもの。
# 解けたッ! と思ったけど、タイムアウトでアウトー。これは理解をするために説明変数とかをたくさん使っているから仕方ないね。

from math import sqrt
# from pprint import pprint


def prime(N: int):

    # 素数一覧。
    primes_ = get_primes_until_n(N)
    # (value, weight) 化します。
    # それぞれの数字の価値は全部 1 です。なるべく多く入ってほしい = 全価値同じ、ってことだから。
    primes = [(1, _) for _ in primes_]
    # print(primes)

    # 表のいちばん左の列。行の数は、冒頭の例でいえば 18+1。重量 0 のときの行があるからひとつ多い。
    # None は、「その重さは作れない」ことを意味します。だって 1 とか素数足しても作れないでしょ?
    dp = [[None] * (N + 1)]
    # だけど重さ 0 が、素数 0 個選択で作れることは分かってるので 0 に更新しときます。
    dp[0][0] = 0

    # 素数の個数分計算を行います。
    for i in range(len(primes)):

        # i の周回では primes[i] まで選べるときの計算をします。
        # 表でいえば i+1 列目ね。
        value = primes[i][0]
        weight = primes[i][1]

        # i+1 列目を作っておきます。
        dp.append([None] * (N + 1))
        dp[i + 1][0] = 0

        for w in range(N + 1):

            # dp[i][w] のマスに、 primes[i] を足したらどうなる? って検証をするんだけど、
            # そもそもこのマスが作成不可マス……どう素数を足しても作れない重さ……だったら計算する意味がないです。
            if dp[i][w] is None:
                continue

            # このマス右隣(dp[i + 1][w])と比較します。
            # 現在のマス dp[i][w] には、 primes[i] まで選べるときの最大値が入っていて、
            # 右隣には、 primes[i+1] を足した場合の値が入ってます。
            # それが不適切(今のままのほうが大きい)場合があるから、更新します。
            dp[i + 1][w] = max(dp[i][w], dp[i + 1][w] if dp[i + 1][w] else 0)

            # じゃあこのマスに primes[i] を足してみます。
            # ひとつ足すわけだから、格納する列は i+1 になります。
            # 格納する行は、 w + primes[i] の重さ になります。
            # ただ N を超えるようならどうだっていいのでスキップです。
            if w + weight > N:
                continue
            # 格納する値は、いまのところからひとつ足すので +1 です。今回では value が全部 1。
            dp[i + 1][w + weight] = dp[i][w] + value

    # dp テーブル作り終わりました。
    # この表には、素数が i 個選べるとき w をぴったり作れる素数の個数が入っています。
    # pprint(dp, width=200)
    # 今回知りたいのは、 N をぴったり作れるときの最大数です。
    # N をぴったり作れる個数の一覧がこれ。
    possible_values = [i[N] for i in dp]
    # その中で最大のものを返します。あっ、 None が混ざっているので None は -1 に変換します。
    possible_values = [_ if _ else -1 for _ in possible_values]
    return max(possible_values)


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


# print(prime(18) == 3)
# print(prime(4) == -1)
# print(prime(3) == 1)
# print(prime(1) == -1)
print(prime(3344) == 41)
# print(prime(int(input())))

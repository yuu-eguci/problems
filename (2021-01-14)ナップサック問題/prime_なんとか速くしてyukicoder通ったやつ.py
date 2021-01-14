"""https://yukicoder.me/problems/no/458
N をそれぞれ異なる素数の和で表すことができる場合，その中での最大の和の回数 M を出力してください。
素数自身でしか表せない場合も含みます。
異なる素数の和で表すことができない場合は -1 を出力してください。
"""
# prime.py を色々いじって、なんとか速くしたもの。
# だけど N=20000 で Memory limit exceeded が出る! しかも 518,652 KB だから……たったの 6MB オーバー!
# from memory_profiler import profile を使って
# メモリをたくさん使っているところを探そうとしたけど別にどこも大して使ってない!
# ↓
# Chenhao の正答コード(prime_3.py)を参考に、


from pprint import pprint
from math import sqrt
N = int(input())

# def get_primes_until_n(N: int):
#     """N までの素数一覧を返します。"""

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

primes = [i for i in dic.keys() if dic[i]]
del dic

# print(prime(18) == 3)
# print(prime(4) == -1)
# print(prime(3) == 1)
# print(prime(1) == -1)
# print(prime(3344) == 41)
# print(prime())

# 素数一覧。
# primes = get_primes_until_n(N)
# (value, weight) 化します。
# それぞれの数字の価値は全部 1 です。なるべく多く入ってほしい = 全価値同じ、ってことだから。
# HACK: 速度のため、わかりやすく (value, weight) にしていたのをやめます。
# primes = [(1, _) for _ in primes_]
# print(primes)

# 表のいちばん左の列。行の数は、冒頭の例でいえば 18+1。重量 0 のときの行があるからひとつ多い。
# None は、「その重さは作れない」ことを意味します。だって 1 とか素数足しても作れないでしょ?
# dp = [[None] * (N + 1)]
# だけど重さ 0 が、素数 0 個選択で作れることは分かってるので 0 に更新しときます。
# dp[0][0] = 0
# HACK: 速度のために、一番最初に全部作ることにしました。効果あった。
# HACK: 速度のために None -> -1 にしました。
# HACK: メモリ効率のため?? 繰り返し使うオブジェクトをあらかじめ作っておきます。
dp_ = [0] + [-1] * N
# range_ = range(N + 1)
dp = [dp_ * 1 for i in range(len(primes) + 1)]
# print(sys.getsizeof(dp))

# 素数の個数分計算を行います。
for i in range(len(primes)):

    # i の周回では primes[i] まで選べるときの計算をします。
    # 表でいえば i+1 列目ね。
    # value = primes[i][0]
    # weight = primes[i][1]
    # HACK: 速度のため、わかりやすく (value, weight) にしていたのをやめます。

    # i+1 列目を作っておきます。
    # dp.append([None] * (N + 1))
    # dp[i + 1][0] = 0
    # HACK: 速度のために、一番最初に全部作ることにしました。

    for w in range(N + 1):

        # HACK: 速度のために、下の if をひとつにします。効果あった。
        if w + primes[i] <= N and dp[i][w] != -1:
            dp[i + 1][w + primes[i]] = dp[i][w] + 1

        # dp[i][w] のマスに、 primes[i] を足したらどうなる? って検証をするんだけど、
        # そもそもこのマスが作成不可マス……どう素数を足しても作れない重さ……だったら計算する意味がないです。
        # if dp[i][w] == -1:
            # continue

        # このマス右隣(dp[i + 1][w])と比較します。
        # 現在のマス dp[i][w] には、 primes[i] まで選べるときの最大値が入っていて、
        # 右隣には、 primes[i+1] を足した場合の値が入ってます。
        # それが不適切(今のままのほうが大きい)場合があるから、更新します。
        # HACK: 速度のため max -> if にします。
        dp[i + 1][w] = max(dp[i][w], dp[i + 1][w])

        # じゃあこのマスに primes[i] を足してみます。
        # ひとつ足すわけだから、格納する列は i+1 になります。
        # 格納する行は、 w + primes[i] の重さ になります。
        # ただ N を超えるようならどうだっていいのでスキップです。
        # if w + primes[i] > N:
        #     continue
        # 格納する値は、いまのところからひとつ足すので +1 です。今回では value が全部 1。
        # dp[i + 1][w + primes[i]] = dp[i][w] + 1

# dp テーブル作り終わりました。
# この表には、素数が i 個選べるとき w をぴったり作れる素数の個数が入っています。
# pprint(dp, width=200)
# 今回知りたいのは、 N をぴったり作れるときの最大数です。
# N をぴったり作れる個数の一覧がこれ。
possible_values = (i[N] for i in dp)
# その中で最大のものを返します。あっ、 None が混ざっているので None は -1 に変換します。
# possible_values = [_ if _ else -1 for _ in possible_values]
print(max(possible_values))

# def test():
#     return prime(int(input()))

# profiler = cProfile.Profile()
# profiler.runcall(test)
# stats = pstats.Stats(profiler)
# stats.strip_dirs()
# stats.sort_stats('cumulative')
# stats.print_stats()

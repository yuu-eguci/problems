"""
ナップサック問題
- a = n 個の (int, int) tuple が入ってるリスト
- (weight, value) を表す
- a から「weight 合計が W を超えないよう」好きなだけ tuple を選んで value を足したときの最大値を出せ
"""


from pprint import pprint


def knapsack(lis: list, W: int) -> int:

    # 表を作ります。
    # dp[0] はリストから何も選んでないときの最大値じゃん? だから一番左の列は全部 0 です。
    dp = [[0] * (W + 1)]

    # リストの個数ぶん回します。
    for i in range(len(lis)):

        # i の周回では lis[i] までの品が選べるときの計算をします。
        weight = lis[i][0]
        value = lis[i][1]

        # lis[i] までの品が選べるときの情報を格納する配列です。もちろん [0]*W+1 です。
        dp.append([0] * (W + 1))

        # lis[i] までの品が選べる列のマスを埋めます。
        for w in range(W + 1):

            # lis[i] の重さが重量制限より上だったら、 lis[i] を追加することはできません。
            # この w 制限での value 最大値は、 lis[i] を追加する前の最大値(dp[i][w])と同じです。
            # NOTE: いま値を追加したいマスは、 dp[i][w] じゃなくて dp[i + 1][w] なのがちょっとわかりづらいトコ。
            if weight > w:
                dp[i + 1][w] = dp[i][w]
                continue

            # lis[i] を追加したときの最大値は、(ここがムズいんだが)
            # lis[i] を追加する前の最大値リストの中で、
            # lis[i] の入るスペースがあるときの最大値に lis[i] の価値を足したものです。
            _ = dp[i][w - weight] + value

            # lis[i] を足した場合の値と、 a[i] を足さなかったときの値(これまでの最大値)、大きいほうが、この条件下での最大値です。
            dp[i + 1][w] = max(_, dp[i][w])

    pprint(dp)

    # 一番はじっこ…… a の個数ぶん選べて、重量制限が W のときの最大値が、答えです。
    return dp[-1][-1]


print(knapsack([(2, 3), (1, 2), (3, 6), (2, 1), (1, 3), (5, 85)], 9) == 94)


"""雪子さん

直線上の位置0にいる雪子さんが、nの距離にある自宅に帰ろうとしています。
雪子さんは酔っ払ってるので前・後ろにランダムで歩きます。
ただしn*2歩あるくと疲れ果てて倒れます。
雪子さんが自宅に帰れるパターンの総数を求めよ。
"""


# 時間測るよ。
import time
start = time.time()


# これ。
def foo(n):

    # 家に辿り着いたルート数。
    answer = 0
    # 雪子現在地。
    yukiko = 0
    # 雪子現在歩数。
    cursor = -1
    # 雪子体力限界。
    max_cursor = n * 2 - 1
    # 歩行履歴リスト。
    lis = [None for i in range(n * 2)]
    # 問題の都合で登場する数値。
    big_num = pow(10, 9) + 7

    # ノードの考え方で再起する関数。図無しでなんて説明したらいいかわかんね。
    def bar(yukiko, cursor, lis):

        nonlocal answer

        for i in [1,-1]:
            # 1歩移動。
            cursor += 1
            lis[cursor] = i
            yukiko += i

            # 帰宅。記録してから、時間よ戻れ。
            if yukiko == n:
                answer += 1
                cursor -= 1
                yukiko -= i
            # 限界の半分まできたのにまだ現在地0を超えてなかったら無理。時間よ戻れ。
            # or 体力限界。時間よ戻れ。
            elif (cursor-1 == n and yukiko <= 0) or (cursor == max_cursor):
                cursor -= 1
                yukiko -= i
            # 次の1歩へ。
            else:
                yukiko, cursor, lis = bar(yukiko, cursor, lis)

        # for が終わったら時間よ戻れ。
        yukiko -= lis[cursor]
        cursor -= 1
        return yukiko, cursor, lis

    bar(yukiko, cursor, lis)
    # 問題の都合。10^9+7の余りを返却します。
    return answer % big_num


if __name__ == '__main__':

    test_cases = [
        # input, answer
        [1, 1],
        [2, 3],
        [3, 4],
        [4, 19],
        [5, 26],
        [6, 144],
        [7, 197],
        [8, 1171],
        [9, 1597],
        [10, 9878],
        # [3568, 802222045],  # 大魔王。これが超せない。
    ]
    for test_case in test_cases:
        answer = foo(test_case[0])
        if answer != test_case[1]:
            print(f'はずれー 出題:{test_case} 今出た答え:{answer}')
            exit()
    margin = time.time() - start
    print(f'結果: {margin}秒')

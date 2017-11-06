'''
*逆FizzBuzz問題*
あるリストが与えられたときに、FizzBuzzを実行するとそのリストを出力するような最短の連続数列を求めよ。
'''

FIZZ = 'fizz'
BUZZ = 'buzz'
FIZZBUZZ = FIZZ + BUZZ


def zzubzzif(lis):

    # 引数lisの個数を求めます。
    length = len(lis)
    if length == 0:
        return []

    # 1~15のfizzbuzzを用意します(1行fizzbuzz)。数字の部分はNoneにしときます。
    # あとlisの個数に合わせてfizzbuzzを伸ばしときます。1個:パターン1周でOK 2〜8:2周 9〜15:3周。
    import math
    fbs = list(map(
        lambda i: None if (i % 3 and i % 5)
        else ('' if i % 3 else FIZZ) + ('' if i % 5 else BUZZ),
        range(1, 16)
    )) * (1 + math.ceil((length - 1) / 7))

    # 今から求めるのは、一致するfizzbuzzの開始位置と、連続数列の長さです。
    fixed_start_index = None
    fixed_fbs_num = len(fbs)

    # まず開始位置を求めます。
    for start_index in range(len(fbs) - length + 1):

        # 空欄だったり、しょっぱなから一致しなかったらスキップです。
        if fbs[start_index] == None or fbs[start_index] != lis[0]:
            continue

        # 開始位置が決定したら以降のfizzbuzz並びを見ます。
        lis_num = 0  # lis[0]からの距離。範囲は0〜(length-1)
        fbs_num = 0  # fbs[start_index]からの距離。範囲は0〜(len(fbs)-start_index-1)
        while fbs_num < (len(fbs) - start_index):

            # 空欄はスキップです。
            if fbs[start_index + fbs_num] is None:
                fbs_num += 1
                continue

            # 一致しなければ今回のstart_indexはアウト。
            if fbs[start_index + fbs_num] != lis[lis_num]:
                break

            # 一致した! 次のチェックにいこう。
            lis_num += 1
            fbs_num += 1

            # え? もうlis終わり? じゃあ全部一致したってことだねおめでとう。
            if lis_num == length:

                # ただしfixするのは、fbs_numがこれまでで一番短ければだ。
                if fbs_num < fixed_fbs_num:
                    fixed_fbs_num = fbs_num
                    fixed_start_index = start_index
                break

    # さて結果は出たのかな?
    if fixed_start_index is None:
        return []

    # fixed_start_point+1の数字からfixed_fbs_numの距離の連続数列が答え。
    result = []
    for i in range(fixed_start_index + 1, fixed_start_index + 1 + fixed_fbs_num):
        result.append(i)

    return result


tests = [
    [FIZZ],              # 3
    [BUZZ],              # 5
    [FIZZ, BUZZ],        # 9,10
    [BUZZ, FIZZ],        # 5,6
    [FIZZ, BUZZ, FIZZ],  # 3,4,5,6
    [FIZZ, FIZZ],        # 6,7,8,9
    [FIZZ, FIZZ, BUZZ],  # 6,7,8,9,10
    [BUZZ, FIZZ, BUZZ],  # (空配列)
    [BUZZ,FIZZ,FIZZ,BUZZ,FIZZ,FIZZBUZZ,FIZZ,BUZZ,FIZZ,FIZZ,BUZZ,FIZZ,FIZZBUZZ,FIZZ],
]

for test in tests:
    print(test, '=>', zzubzzif(test))

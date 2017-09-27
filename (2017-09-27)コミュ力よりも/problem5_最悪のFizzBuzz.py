#!/usr/bin/env python
# coding: utf-8

'''プログラム問題
http://www.softantenna.com/wp/software/fizzbuzz-alternatives/

このファイルをこのまま実行すれば結果みれます。
・パターン1: problem5() 長い
・パターン2: problem5_oneline() 短い
'''


def problem5(start, end):
    '''5. 最悪のFizzBuzz
    最悪の - しかし動作する - FizzBuzzプログラムをかけ。
    '''

    print('========== 問題5 最悪のFizzBuzz 開始! ==========')

    # 最悪POINT 1: 変数名が日本語。
    結果リスト = []

    # 最悪POINT 2: 一回しか使わない変数をわざわざ作成してる。
    end2 = end + 1
    for i in range(start, end2):

        # 最悪POINT 3: 真偽用の変数を作るにしてもboolじゃなく文字列を使用。
        iは3の倍数です = 'いいえ'
        iは5の倍数です = 'いいえ'

        # 最悪POINT 4: 3の倍数の求め方が「ずっと3を足していって該当したら」。頭わるそう!
        three = 3
        while True:
            # 最悪POINT 5: コードを見れば分かることをわざわざ説明するコメント。
            # threeがiと同じときiは3の倍数ですを'はい'にする。threeがiより大きくなっちゃったらwhileを終了。
            if three == i:
                iは3の倍数です = 'はい'
            elif three > i:
                break
            # 最悪POINT 6: three += 3 という書き方を知らない。
            three = three + 3

        # 最悪POINT 7: 上と同じような処理なのに関数化してない。
        five = 5
        while True:
            if five == i:
                iは5の倍数です = 'はい'
            elif five > i:
                break
            # 最悪POINT 8: って、知ってんのかよ! だったら上のも += 3 にしろよ!
            five += 5

        # 最悪POINT 9: 無駄に ! を使ってる。この場合 == 'はい' にするべき。
        if iは3の倍数です != 'いいえ':
            if iは5の倍数です != 'いいえ':
                結果リスト.append('FizzBuzz')
                continue

        # 最悪POINT 10: このあたりは if elif でまとめればいいのにばらばらにifしてる。
        if iは3の倍数です != 'いいえ':
            結果リスト.append('Fizz')
            continue

        if iは5の倍数です != 'いいえ':
            結果リスト.append('Buzz')
            continue

        # 最悪POINT 11: ここまで処理が進むってことは絶対両方 'いいえ' なのにわざわざifに入れてる。
        if iは5の倍数です == 'いいえ':
            if iは3の倍数です == 'いいえ':
                結果リスト.append(str(i))

    # 最悪POINT 12: for部が長すぎる。

    結果の文字列 = ''
    # 最悪POINT 13: すごくダメな例外処理の使い方してる。NoIndexExceptionが出たらそこで処理が終了。
    try:
        i = 0
        while True:
            結果の文字列 = 結果の文字列 + 結果リスト[i] + ','
            i += 1
    except:
        pass

    return 結果の文字列


def problem5_oneline(start, end):
    # 最悪POINT: ワンラインで読みづらい。
    return list(
        map(
            lambda i:
                str(i)
                if (i % 3 and i % 5)
                else ('' if i % 3 else 'Fizz') + ('' if i % 5 else 'Buzz'),
            range(start, end + 1))
    )


# 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz
print(problem5(1, 10), end='\n\n')
# Buzz,101,Fizz,103,104,FizzBuzz,106,107,Fizz,109,Buzz
print(problem5(100, 110), end='\n\n')
# FizzBuzz,1501,1502,Fizz,1504,Buzz,Fizz,1507,1508,Fizz,Buzz
print(problem5(1500, 1510), end='\n\n')

# 上と同じ結果になる。
print(problem5_oneline(1, 10), end='\n\n')
print(problem5_oneline(100, 110), end='\n\n')
print(problem5_oneline(1500, 1510), end='\n\n')

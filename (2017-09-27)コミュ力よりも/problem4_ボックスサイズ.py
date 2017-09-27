#!/usr/bin/env python
# coding: utf-8

'''プログラム問題
http://www.softantenna.com/wp/software/fizzbuzz-alternatives/

このファイルをこのまま実行すれば結果みれます。

'''


def problem4(cm1, cm2, cm3):
    '''4. ボックスサイズ
    単位がセンチメートルの3つの引数をとり、体積を計算しリットルとして返す関数をかけ。
    '''

    print('========== 問題4 ボックスサイズ 開始! ==========')

    # 値チェックします。
    cm = [cm1, cm2, cm3]
    for c in cm:
        if not (isinstance(c, int) or isinstance(c, float)):
            print(f'引数はintかfloatにしてよー: {c}')

    # Decimal(正確な小数)化します。
    import decimal
    cm = map(lambda c: decimal.Decimal(str(c)), cm)

    # 立方センチメートル出します。reduceってのはなんか配列を片っ端から処理してくれるやつ。
    import functools
    cubic_cm = functools.reduce(lambda x, y: x * y, cm)

    # リットルに変換します。1000立方cm = 1.0リットル。
    return cubic_cm / 1000


print(problem4(2.0, 2.0, 2.0), end='\n\n')        # 0.008(l)
print(problem4(10.0, 10.0, 10.0), end='\n\n')     # 1.0(l)
print(problem4(123.4, 123.4, 123.4), end='\n\n')  # 1879.080904(l)
print(problem4(2, 2, 2), end='\n\n')              # 0.008(l)

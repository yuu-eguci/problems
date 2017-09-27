#!/usr/bin/env python
# coding: utf-8

'''プログラム問題
http://www.softantenna.com/wp/software/fizzbuzz-alternatives/

このファイルをこのまま実行すれば結果みれます。

この関数、みづらい。どうにかならんの。

'''


def problem2(dollar, tax_rate):
    '''2. 税金計算
    金額(ドル)と、税率(%)を引数にとり、答えの金額をセントとして配列で返せ。
    '''

    print('========== 問題2 税金計算 開始! ==========')

    if not (isinstance(dollar, float) and isinstance(tax_rate, float)):
        print(f'引数はfloatだけ認めるよ: {dollar}, {tax_rate}')
        return False

    '''以下のようにします。dollar, tax_rate = 100.1, 9.75 の場合
    100.1 * 9.75   + 100.1
    100.1 * 0.0975 + 100.1 (%を割合に)
    ((1001 * 975) + 10010000) / 100000 (小数点を消す)
    (975975       + 10010000) / 100000
    10985975                  / 100000
    109.85975 (答えが出る)
    [109, 85.975] (問題の指示に従う)
    '''

    dollar, tax_rate = str(dollar), str(tax_rate)

    # 小数点は右からいくつめにあるの? **.**** なら 4 を取得します。
    # [::-1]は文字列の逆転。pt_lctnはpoint_locationのこと。
    dollar_pt_lctn = dollar[::-1].find('.')

    # 税率は%単位だから、最後に/100ぶんの2を足すよ。 *.* なら 3 を取得します。
    tax_rate_pt_lctn = tax_rate[::-1].find('.') + 2

    # ドル、税率から小数点を削除ります。晴れてintになりました。さらばfloat。
    dollar_int = int(str(dollar).replace('.', ''))
    tax_rate_int = int(str(tax_rate).replace('.', ''))

    # 税金額を出します。floatでやると誤差が生じてワヤになるからintで。
    tax_amount = dollar_int * tax_rate_int

    # 元のドルを税金額に桁あわせします。float同士だと足し算ですら狂うのでintでやります。
    # 小数点を削除ったドルに、税率の小数点の位置ぶん0加えたものがそれ。
    original_dollar = int(str(dollar_int) + '0' * tax_rate_pt_lctn)

    # 元のドルに税金額を足します。
    result = str(original_dollar + tax_amount)

    # 削除ってた小数点を戻します。
    # 位置は、最初に削除ったふたつの小数点の位置を足したところ。
    # 100.1ドル と 9.75% だったら 右から5番目になる。(%ぶんの+2を忘れずに。)
    pt_lctn = dollar_pt_lctn + tax_rate_pt_lctn
    result_ = (str(result)[0:-pt_lctn] + '.' + str(result)[-pt_lctn:])

    print(f'額は ${result_} になりました。結果の配列は下に表示されます。')

    # なんやかんやで $***.***** を [***, **.***] にして返します。
    dollar_part = str(result)[0:-pt_lctn]
    dollar_part = int(dollar_part if dollar_part else '0')
    cent_part = str(result)[-pt_lctn:] + '0'
    cent_part = float(cent_part[0:2] + '.' + cent_part[2:])

    return [dollar_part, cent_part]


# Decimalを使った場合。
import decimal
def problem2_(dollar, tax_rate):

    # Decimal型(正確な小数)に変換します。
    dollar = decimal.Decimal(str(dollar))
    tax_rate = decimal.Decimal(str(tax_rate))

    # 元の額 + 税額
    result = dollar + dollar * (tax_rate / 100)

    # ドル部とセント部に分けます。
    return [int(result), float((result - int(result)) * 100)]


print(problem2(100.0, 8.00), end='\n\n')         # [108, 0]
print(problem2(0.10, 10.56), end='\n\n')          # [0, 11]
print(problem2(100.10, 9.75), end='\n\n')        # [109, 85]
print(problem2(100, 9.75), end='\n\n')           # False
print(problem2(123.456789, 8.1234), end='\n\n')  # [133, 48]
print(problem2(4.64, 9.75), end='\n\n')          # [5, 9]
print(problem2(0.10, 10.56), end='\n\n')         # [0, 11]
print(problem2(1.0, 100.0), end='\n\n')          # [2, 0]

# 0.10,       10.56
# 100.10,     9.75
# 100,        9.75
# 123.456789, 8.1234
# 4.64,       9.75
# 0.10,       10.56
# 1.0,        100.0

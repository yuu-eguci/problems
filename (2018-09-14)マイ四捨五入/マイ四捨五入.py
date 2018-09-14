
# @channel
# みな時間があったら、やってみない:question:
# 四捨五入の関数を作る。
# 多分仕事や遊びや時に偶に必要があるかも

# Let's make a function to round numbers!
def my_round(num, digit=0):

    # 引数チェック。
    if not (isinstance(num, int) or isinstance(num, float) or isinstance(digit, int)):
        return False

    # 整数部と小数部。
    _ = str(num).split('.')

    # digitで表された桁の右が5以上なら繰り上がりをTrueに。(小数部の場合)
    if digit >= 0:
        f_part = list(map(int, str(_[1]))) if len(_)==2 else [0]
        up = digit < len(f_part) and f_part[digit] >= 5

    # digitで表された桁の右が5以上なら繰り上がりをTrueに。(整数部の場合)
    else:
        i_part = list(map(int, str(_[0])))
        up = -digit < len(i_part) and list(reversed(i_part))[-digit] >= 5

    # 繰り上がりが起こるなら行って返す。digitより下の桁は切り落とす。
    return int((num + 1 * 10**-digit if up else num) * 10**digit) / 10**digit


cases = [
    [1.9001, None],  # 2
    [2.03, None],  # 2
    [2.5, None],  # 3
    [2.999, None],  # 3
    [2.4999999, None],  # 2
    [2.0, None],  # 2

    [1.55, 1],  # 1.6
    [123.456, -3],  # 0.0
    [123.456, 3],  # 123.456
]
for case in cases:
    if case[1]:
        print(my_round(case[0], case[1]))
    else:
        print(my_round(case[0]))

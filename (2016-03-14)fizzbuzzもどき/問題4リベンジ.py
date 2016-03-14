# coding: utf-8

# ==============================
# 問題4
# 正の整数のリストを与えられたとき、数を並び替えて可能な最大数を返す関数を記述せよ。
# 例えば、[50, 2, 1, 9]が与えられた時、95021が答えとなる。
# ==============================


def foo(number_list):
    '''やること
    1. 価値を決めます
        {'98':988, '9':999, '506':506, '50':500, '2':222, '1':111, '22':222,}
    2. 価値を降順にします
        [999, 988, 506, 500, 222, 111]
    3. 高い価値を持つものから順にくっつけます
        「999の価値をもつ9」「988の価値をもつ98」...「222の価値をもつ2と22」...という順番
    '''

    # 全部文字列にします。
    number_list = list(map(lambda num: str(num), number_list))

    # 最大桁数を求めます。
    maxdigit = 0
    for number in number_list:
        maxdigit = len(number) if maxdigit < len(number) else maxdigit

    # 数値の価値を決めます。{実値:価値}というディクショナリ。
    value_dic = {}
    for num_string in number_list:
        value_string = num_string
        for i in range(maxdigit):
            if len(value_string) < maxdigit:
                value_string += value_string[-1]
        value_dic[num_string] = int(value_string)

    # 価値の降順リストを作ります。重複を削除するためにsetを通します。(setにすると重複消える)
    value_list = list(set(value_dic.values()))
    value_list.sort(reverse=True)

    # 高い価値をもつものから順にくっつけます。
    result = ''
    for value_int in value_list:
        for actual, value in value_dic.items():
            result += (actual * number_list.count(actual)
                       if value == value_int else '')

    return result


# expected => 999998
print(foo([9, 99998, ]))
# expected => 100100
print(foo([100, 100]))
# expected => 31531
print(foo([31, 315, ]))
# expected => 998506506502221
print(foo([98, 9, 506, 506, 50, 2, 1, 22, ]))

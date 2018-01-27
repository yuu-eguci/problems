#!/usr/bin/env python
# coding: utf-8

'''
    [星座名] と [誕生した日にち]早見表

    牡羊座  Aries
           3月21日  から  4月20日生まれ
    牡牛座  Taurus
           4月21日  から  5月20日生まれ
    双子座  Gemini
           5月21日  から  6月21日生まれ
    蟹座    Cancer
           6月22日  から  7月23日生まれ
    獅子座  Leo
           7月24日  から  8月23日生まれ
    乙女座  Virgo
           8月24日  から  9月23日生まれ
    天秤座  Libra
           9月24日  から 10月23日生まれ
    蠍座    Scorpio
           10月24日 から 11月22日生まれ
    射手座  Sagittarius
           11月23日 から 12月22日生まれ
    山羊座  Capricorn
           12月23日 から  1月20日生まれ
    水瓶座  Aquarius
           1月21日  から  2月19日生まれ
    魚座    Pisces
           2月20日  から  3月20日生まれ
'''
# 入力された値をとる方法
# こうすると xは最初に入力したもの、yはその次に入力したもの、になります。
# ちなみに、入力された値は文字列として扱われます。
x = input()
y = input()


# [問題]
# 入力された、月日によって、その人の星座を教えてくれるプログラムを組んでください。


# 星座当てです。
def 星座当て(user_month, user_day):

    # 早見表をディクショナリ形式にしまーす。
    BORDER_, LESS_, MORE_ = 'border', 'less', 'more'
    zodiacs = {
        # 1月 20日まで 山羊座 それ以降 水瓶座
        '1': { BORDER_: 20, LESS_: '山羊座', MORE_: '水瓶座' },
        # 2月 19日まで 水瓶座 それ以降 魚座
        '2': { BORDER_: 19, LESS_: '水瓶座', MORE_: '魚座' },
        # 3月 20日まで 魚座 それ以降 牡羊座
        '3': { BORDER_: 20, LESS_: '魚座', MORE_: '牡羊座' },
        # 4月 20日まで 牡羊座 それ以降 牡牛座
        '4': { BORDER_: 20, LESS_: '牡羊座', MORE_: '牡牛座' },
        # 5月 20日まで 牡牛座 それ以降 双子座
        '5': { BORDER_: 20, LESS_: '牡牛座', MORE_: '双子座' },
        # 6月 21日まで 双子座 それ以降 蟹座
        '6': { BORDER_: 21, LESS_: '双子座', MORE_: '蟹座' },
        # 7月 23日まで 蟹座 それ以降 獅子座
        '7': { BORDER_: 23, LESS_: '蟹座', MORE_: '獅子座' },
        # 8月 23日まで 獅子座 それ以降 乙女座
        '8': { BORDER_: 23, LESS_: '獅子座', MORE_: '乙女座' },
        # 9月 23日まで 乙女座 それ以降 天秤座
        '9': { BORDER_: 23, LESS_: '乙女座', MORE_: '天秤座' },
        # 10月 23日まで 天秤座 それ以降 蠍座
        '10': { BORDER_: 23, LESS_: '天秤座', MORE_: '蠍座' },
        # 11月 22日まで 蠍座 それ以降 射手座
        '11': { BORDER_: 22, LESS_: '蠍座', MORE_: '射手座' },
        # 12月 22日まで 射手座 それ以降 山羊座
        '12': { BORDER_: 22, LESS_: '射手座', MORE_: '山羊座' },
    }

    # 入力チェックしまーす。
    if ((user_month not in zodiacs)
            or not user_day.isdigit()
            or (not 1 <= int(user_day) <= 31)):
        return 'エラーです。めんどくせーから詳しくは書かないけどなんか引数がおかしいよ。'

    # 日は数値化します。比較するからね。
    user_day_int = int(user_day)

    # その月のデータをもってきます。
    month_dic = zodiacs[user_month]

    # 日が、BORDER以下ならLESSの星座が答えです。より上ならMOREの星座が答えね。
    if user_day_int <= month_dic[BORDER_]:
        return month_dic[LESS_]
    else:
        return month_dic[MORE_]


print(星座当て(x, y))

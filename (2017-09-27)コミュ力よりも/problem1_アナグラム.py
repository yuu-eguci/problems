#!/usr/bin/env python
# coding: utf-8

'''プログラム問題
http://www.softantenna.com/wp/software/fizzbuzz-alternatives/

このファイルをこのまま実行すれば結果みれます。

'''


def problem1(arg1, arg2):
    '''1. アナグラム
    2つの引数を取り、引数がアナグラム(どちらも全く同じ文字を含んでいる)ならばtrueを、
    そうでないならばfalseを返す関数をかけ。
    '''

    print('========== 問題1 アナグラム 開始! ==========')

    # 引数チェック。
    if not (isinstance(arg1, str) and isinstance(arg2, str)):
        print(f'引数は文字列だけ認めるよ: {arg1}, {arg2}')
        return False

    # 長さが違う時点でダメ。
    if len(arg1) != len(arg2):
        print(f'長さが違う時点でダメ: {arg1}, {arg2}')
        return False

    # arg1の文字が全部arg2に同数含まれてるか? という判断基準でいく。
    for a in arg1:
        if arg1.count(a) != arg2.count(a):
            print(
                f'arg1の文字"{a}"がarg1には{arg1.count(a)}個あるけど'
                f'arg2には{arg2.count(a)}個あるよ: {arg1}, {arg2}'
            )
            return False

    print(f'OKだよーん: {arg1}, {arg2}')
    return True


print(problem1('abcde', 'edcba'), end='\n\n')   # True
print(problem1('abcde', 'abcdei'), end='\n\n')  # False
print(problem1('abcde', 1), end='\n\n')         # False
print(problem1('abcde', 'edcbf'), end='\n\n')   # False
print(problem1('日本語はどうでしょうね', 'ううしでどねはょ日本語'), end='\n\n')  # True
print(problem1('ABA', 'ABB'), end='\n\n')       # False

# 'abcde', 'edcba'
# 'abcde', 'abcdei'
# 'abcde', 1
# 'abcde', 'edcbf'
# '日本語はどうでしょうね', 'ううしでどねはょ日本語'
# 'ABA', 'ABB'

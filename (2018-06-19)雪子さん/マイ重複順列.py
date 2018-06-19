#!/usr/bin/env python
# coding: utf-8

# リストの長さ。
n = 3

# 重複順列にしたい配列。
a = [1, -1]

def my_product(a, n):

    # nぶんのリストを用意します。 [None, None, None] ここにTrue Falseを詰めていきます。
    lis = [None for i in range(n)]
    cursor = -1
    cursor_max = len(lis) - 1

    def foo(lis, cursor):

        for i in a:

            # 1階層もぐって1個詰める。
            cursor += 1
            lis[cursor] = i

            # 最深部だったら出力して1階層戻る。
            if cursor == cursor_max:
                print(lis)
                cursor -= 1

            # 次の階層へ。
            else:
                lis, cursor = foo(lis, cursor)

        # forが終わるとき、上に戻る。
        cursor -= 1
        return lis, cursor

    foo(lis, cursor)

my_product(a, n)

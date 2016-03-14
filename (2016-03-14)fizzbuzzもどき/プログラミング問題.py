# !/usr/bin/env python
# coding: utf-8

# ==============================
# 問題1
# forループ、whileループ、および再帰を使用して、リスト内の数字の合計を計算する3つの関数を記述せよ。
# ==============================

lis = [0, 1, 2, 3, -4]

# forループ
def func_for_Q1_1(lis):
    ret = 0
    for l in lis:
        ret += l
    return ret

# whileループ
def func_for_Q1_2(lis):
    ret = 0
    i = 0
    while i < len(lis):
        ret += lis[i]
        i += 1
    return ret

# 再起
def func_for_Q1_3(lis, ret=0):
    if len(lis) == 0:
        return ret
    else:
        ret += lis[0]
        lis.pop(0)
        ret = func_for_Q1_3(lis, ret)
        return ret

def problem1_recursive(lis, ret=0):
    if len(lis) == 0:
        return ret
    ret += lis[0]
    lis.pop(0)
    ret = problem1_recursive(lis, ret)
    return ret

print("問題1(for):", func_for_Q1_1(lis))
print("問題1(while):", func_for_Q1_2(lis))
print("問題1(再起):", func_for_Q1_3(lis))


# ==============================
# 問題2
# 交互に要素を取ることで、2つのリストを結合する関数を記述せよ。
# 例えば [a, b, c]と[1, 2, 3]という2つのリストを与えると、関数は [a, 1, b, 2, c, 3]を返す。
# ==============================

lisA = ["a", "b", "c"]
lisB = [0, 1, 2, 3, 4]
# [a,0,b,1,c,2,3,4]になって欲しい

def func_for_Q2(lisA, lisB):
    result = []
    maxlen = len(lisA) if len(lisA) >= len(lisB) else len(lisB)
    for i in range(maxlen):
        if i < len(lisA):
            result.append(lisA[i])
        if i < len(lisB):
            result.append(lisB[i])
    return result
print("問題2:", func_for_Q2(lisA, lisB))


# ==============================
# 問題3
# 最初の100個のフィボナッチ数のリストを計算する関数を記述せよ。
# 定義では、フィボナッチ数列の最初の2つの数字は0と1で、次の数は前の2つの合計となる。
# 例えば最初の10個のフィボナッチ数列は、0, 1, 1, 2, 3, 5, 8, 13, 21, 34となる。
# ==============================

def func_for_Q3():
    result = [0, 1]
    while len(result) < 100:
        result.append(result[-1] + result[-2])
    return result
print("問題3:", func_for_Q3())


# ==============================
# 問題4
# 正の整数のリストを与えられたとき、数を並び替えて可能な最大数を返す関数を記述せよ。
# 例えば、[50, 2, 1, 9]が与えられた時、95021が答えとなる。
# ==============================

lis4Q4 = [100, 50, 2, 1, 99, 98, 3, 3, 9, 10]

### 大きい順に並ぶ関数 ###
def mySort(lis):
    if len(lis) <= 1:
        return lis
    else:
        base = lis[0]
        biggerList  = []
        smallerList = []
        equalList   = []
        for num in lis:
            if   num > base: biggerList.append(num)
            elif num < base: smallerList.append(num)
            else           : equalList.append(num)
        biggerList  = mySort(biggerList)
        smallerList = mySort(smallerList)
        return biggerList + equalList + smallerList

### 一文字目が同じ数字である配列[9,99,98]みたいなのを受け取り、桁数の少なさと数字の大きさでソートする関数 意味不明だって? 俺もだ ###
def strSort(lis):
    # 文字列にする
    lis = [str(x) for x in lis]
    # 桁数の最大をもとめる
    maxNum = 0
    for l in lis:
        if maxNum < len(l):
            maxNum = len(l)
    # 桁数ごとに配列にする [[9], [98,99]]って感じになる
    ketaNumList = []
    for i in range(maxNum):
        ketaNumList.append([])
        for l in lis:
            if len(l) == i + 1:
                ketaNumList[i].append(l)
    # 二つ以上ある桁はソートする [[9], [99,98]]って感じになる
    for i in range(len(ketaNumList)):
        if len(ketaNumList[i]) >= 2:
            ketaNumList[i] = mySort([int(x) for x in ketaNumList[i]])
    # ketaNumListを、要素の並んでる順番に文字列化する "99998" って感じになる
    result = ""
    for ketaNum in ketaNumList:
        for num in ketaNum:
            result += str(num)
    return result

def func_for_Q4_ptn1():
    result = ""
    originalList = [str(x) for x in lis4Q4]

    # 一文字目のリスト(ダブリ無し)を作る
    tmp = mySort([int(str(x)[0]) for x in originalList])
    sortedList = []
    for num in tmp:
        if not num in sortedList:
            sortedList.append(num)

    # sortedListに入ってる数字を一文字目にもつ数字をリストにして、strSort()に渡し、返ってきた文字列をresultに足していく
    for firstNum in sortedList:
        numbersList = []
        for number in originalList:
            if str(firstNum) == number[0]:
                numbersList.append(number)
        # 一文字目の共通する連中がリストになったので、それをstrSort()に渡す
        result += strSort(numbersList)

    return result

print("問題4:", func_for_Q4_ptn1())

# ==============================
# 問題4 回答ふたつめ
# ==============================

def bossSort(lis):    # mySort()とstrSort()を足した機能 引数のリストは全部数値にしてね
    if len(lis) <= 1:
        return lis
    else:
        base     = lis[0]
        len_base = len(str(base))
        biggerList  = []
        smallerList = []
        equalList   = []
        for num in lis:
            len_num = len(str(num))
            # baseとnumの桁差を9で揃える 5と555なら、599と555にする
            digit = len_base if len_base >= len_num else len_num
            b = int(str(base).ljust(digit, "9"))
            n = int(str(num).ljust(digit, "9"))
            # 揃えた数値で比較するが、biggerListとかに追加するのは揃える前の数値
            if   n > b: biggerList.append(num)
            elif n < b: smallerList.append(num)
            else      : equalList.append(num)
        biggerList  = bossSort(biggerList)
        smallerList = bossSort(smallerList)
        return biggerList + equalList + smallerList

def func_for_Q4_ptn2():
    sortedList = bossSort(lis4Q4)
    result = ""
    for num in sortedList:
        result += str(num)
    return result

print("問題4ふたつめ:", func_for_Q4_ptn2())

# ==============================
# 問題5
# 1,2,…,9の数をこの順序で、”+”、”-“、またはななにもせず結果が100となるあらゆる組合せを出力するプログラムを記述せよ。
# 例えば、1 + 2 + 34 – 5 + 67 – 8 + 9 = 100となる。
# ==============================

print("===== 問題5 =====")
patterns = ["+", "-", ""]
for a in patterns:
    for b in patterns:
        for c in patterns:
            for d in patterns:
                for e in patterns:
                    for f in patterns:
                        for g in patterns:
                            for h in patterns:
                                if eval("1%s2%s3%s4%s5%s6%s7%s8%s9" % (a,b,c,d,e,f,g,h)) == 100:
                                    print("1%s2%s3%s4%s5%s6%s7%s8%s9" % (a,b,c,d,e,f,g,h))

# ==============================
# 問題5 回答ふたつめ
# ==============================

print("===== 問題5ふたつめ =====")
for i in range(3**8):
    numList = [1]
    for j in range(2, 10):
        if   i % 3 == 0:
            numList.append(j)
        elif i % 3 == 1:
            numList.append(-j)
        elif i % 3 == 2:
            lastNum = numList[-1]
            numList[-1] = lastNum * 10 + (j if (lastNum > 0) else -j)
        i //= 3

    # print処理
    if sum(numList) == 100:
        result = ""
        for num in numList:
            result += ("+"+str(num)) if (num > 0 and num != numList[0]) else str(num)
        print(result)
"""
解説
ループの数(i)を3進数で扱うと、
000 001 002 010 011 012 020...となる。
全桁ダブることはないので、0,1,2に+,-,.を当てはめていけば3**8の全パターンを網羅できる。
i%3で一桁目を取り出すことができ、i//3で一桁目を取り除く(二桁目を一桁目にシフト)ことができる。
"""

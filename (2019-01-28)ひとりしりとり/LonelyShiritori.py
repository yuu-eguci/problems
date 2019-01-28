
"""ひとりしりとり
ちょうどn回でしりとりを終わらせてください。

ルールは、以下です。
(1) 単語は、小文字アルファベットからなる長さ1以上20以下の文字列を使えます。
(2) 単語の終わりと、次の単語の始めが同じなら、しりとりが続きます。
(3) 最後にnがつく単語を言った時、またその時に限りしりとりが終わります。
(4) 初めはどの単語を使っても構いません。
(5) 同じ単語を2回以上使ってはいけません。

1 <= n <= 100000
"""

def foo(n):
    def bar():
        # n以外。
        alph = [_ for _ in 'abcdefghijklmopqrstuvwxyz']
        # nは100,000までだから4文字で十分。
        i = 0
        for _1 in alph:
            for _2 in alph:
                for _3 in alph:
                    for _4 in alph:
                        i += 1
                        yield first+_1+_2+_3+('n' if i==n else _4)
    first = 'a'
    for i,word in enumerate(bar()):
        if i == n:
            break
        print(word)
        first = word[-1]

if __name__ == '__main__':
    foo(int(input()))

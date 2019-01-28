
"""プログラミング問題: ヘイトプラス
https://yukicoder.me/problems/no/353

A+B を計算します。
しかし + が嫌いなので + を使ってはいけません。ソースコード上に + の文字があると不正解になります。
"""

def foo(a, b):
    return -(-a -b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(foo(a, b))

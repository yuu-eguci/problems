# https://yukicoder.me/problems/no/1217


# あっているやつ。
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def foo(S):
    """最初に思いついたやつ。
    """

    for x, y in zip(ALPHABET, S):
        if x != y:
            return f'{x}to{y}'


def foo(S):
    """zip なんて知らないー ばーじょん。
    """

    for i in range(26):
        x = ALPHABET[i]
        y = S[i]
        if x != y:
            return f'{x}to{y}'


def foo(S):
    """Python 会で頭いいなって言われたやつ。
    """

    for letter in ALPHABET:

        # 2個あるやつが xtoy <- こっち
        if S.count(letter) == 2:
            y = letter

        # 0個のやつが こっち -> xtoy
        elif S.count(letter) == 0:
            x = letter

    return f'{x}to{y}'


def foo(S):
    """set 使ったやつ。
    """

    # 集合の引き算です。 ALPHABET にあって S にないもの(こっち -> xtoy)がわかります。
    x = (set(ALPHABET) - set(S)).pop()
    # なくなったアルファベットは何番目のやつか?
    i = ALPHABET.index(x)
    # その場所は S では何になっているのか(xtoy <- こっち)!
    y = S[i]
    return f'{x}to{y}'


def foo(S):
    """Alan のやつ
    """

    result = ""
    for idx, char in enumerate(S):
        if chr(idx+97) != char:
            result = "{}to{}".format(chr(idx+97), char)
            break


def foo(S):
    """文字列を is で比較する人のやつ1つめ。
    """

    return [f'{c}to{s}' for c, s in zip(ALPHABET, S) if c is not s ][0]


def foo(S):
    """文字列を is で比較する人のやつ2つめ。
    """

    for idx, s in enumerate(S):
        if (c := chr(ord('a')+idx)) is not s:
            return f'{c}to{s}'


if foo('abcdefghijklmnopqrituvwxyz') == 'stoi':
    print('ok')

if foo('abcdefghujklmnopqrstuvwxyz') == 'itou':
    print('ok')

if foo('abcdefghijklmnnpqrstuvwxyz') == 'oton':
    print('ok')

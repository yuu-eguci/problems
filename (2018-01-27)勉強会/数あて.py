# 数当てゲームを作ろう！

# [問題] 次のルールで数当てゲームを作りましょう。

# ～ルール～
# 実行するとまず、答えの数字がランダムで決まります。
# 回答を入力させて、それが答えの数より上か、下か、というヒントを出してください。
# ヒントを頼りに数字を予想していきます。
# 入力された数字が答えと一致したときに、正解となりゲームが終了します。
# 正解するまでゲームは終わりません！

import random, time


# 数当てゲームです。
def 数当てゲーム(_FROM, _TO):

    # 挑戦回数です。
    _TRY = 1
    # 答えの数字をランダムに決めます。
    answer = random.randint(_FROM, _TO)

    while True:
        print('\n===============================================')
        print(f'※ 答えは{_FROM}から{_TO}までの数だよ。入力してね!')
        print(f'※ {_TRY}回目の挑戦です。')
        user_answer = input()
        print(f'あなたの答え:{user_answer}')

        # 入力チェック。
        try:
            user_answer_int = int(user_answer)
        except Exception as e:
            # 数字にできなかったらここに来ます。
            print('入力エラー! ちゃんと数値をいれてね。')
        else:
            # エラーにならないかったらこっちに来ます。
            if user_answer_int != answer:
                print('はずれー。もっと' + ('大きい' if user_answer_int < answer else '小さい') + '数だよ!')
            else:
                print(f'正解! 答えは {answer} でした!')
                return _TRY

            # 挑戦回数を追加です。
            _TRY += 1

        # ちょっと待機します(演出上の問題)。
        time.sleep(0.5)


result = 数当てゲーム(1, 10)

print(' _________________________________________ ')
print('/                                         \\')
print('|         Game Clear! Congrat!            |')
print('\                                         /')
print(' ----------------------------------------- ')
print('        \   ^__^')
print('         \  (oo)\_______')
print('            (__)\       )\/\\')
print('                ||----w |')
print('                ||     ||')
comment = 'かかりすぎやろ。カスやん。'
if result <= 3:
    comment = 'すっげええｇふぇげええええｗｗｗｗｗ'
elif result <= 6:
    comment = 'うおっやるやん。でもさすがに運やろ?'
elif result <= 9:
    comment = 'まあまあやね。もっかいやってかない?'

print(f'Your try: {result}  ' + comment)

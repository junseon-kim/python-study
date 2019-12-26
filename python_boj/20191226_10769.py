# 행복 :-) 슬픔 :-(
# 없으면 none, 같으면 unsure, 행복 happy, 슬픔 sad
emotion = input()
hpy = emotion.count(':-)')
sd = emotion.count(':-(')
if hpy == 0 == sd:
    print('none')
elif hpy > sd:
    print('happy')
elif sd > hpy:
    print('sad')
else:
    print('unsure')
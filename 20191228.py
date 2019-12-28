# 2019.12.28.(토) 오늘은 딕셔너리부터 시작해본다.

# 딕셔너리 만드는 법
lux = {'health': 500, 'mana': 700} # 키1: 값1, 키2: 값2
# 값에는 모든 자료형을 사용할 수 있다. 리스트와 딕셔너리 마저도.
# 하지만 키에는 리스트나 딕셔너리 등을 사용할 수 없다.
# 빈 딕셔너리 만들기
a = {}
b = dict()
# dict를 이용해서 딕셔너리 만드는 법
c = dict(A=300, B=600, C=450)
# 1. 키=값 의 형태로 만들 때에는 키에 따옴표를 쓰지 않는다. 이렇게 해서 만들어진 키는 모두
# 문자열로 바뀌기 때문.
print(c)
# 2. zip함수을 이용한다. 단, zip([키들의 리스트],[값들의 리스트])
d = dict(zip(['A', 'B', 'C', 'D'], [100, 300, 500, 700]))
print(d)
# 3. 튜플을 이용한다. (키1, 값1)으로 이루어진 튜플을 리스트 안에 넣어서 딕셔너리를 만든다.
e = dict([('he', 400), ('fe', 23), ('thre', 700), ('sfghnhq', 4323), ('fgr', 2315)])
print(e)

# 4. dict() 안에 중괄호{} 로 직접 만드는 것.
f =  dict({'menu1':7000, 'menu2': 6000, 'menu3': 5000})
print(f)

# 딕셔너리의 키로 접근하기 딕셔너리[키] -> 값
print(f['menu1'])
# 딕셔너리 키에 값 할당
f['menu1'] = 65000
print(f)
f['menu4'] = 43520
print(f)

# in, not in
print('menu4' in f) # 있으면 True
print('menu5' not in f) # 없으면 True

# if
a = 10
if a == 10:
    pass # TODO: 이렇게 해두면 나중에 해야할 일을 쉽게 볼 수 있다. ctrl + F 로 TODO를 찾으면 된다.
# if 에서 False로 취급하는 것.
# 1. 0
# 2. None
# 3. 빈 문자열, 튜플, 딕셔너리, 세트
b = 15
if a==10 & b==15:
    print('맞워')
else:
    print('아녀')
a = [1, 2, 3, 4, 5, 6]
print(max(a))
# scores = list(map(int, input().split()))
# if max(scores)>100 or min(scores)<0:
#     print('잘못된 점수')
# elif sum(scores)/4 >= 80:
#     print('합격')
# else:
#     print('불합격')

# 오늘의 파이썬 끝. 다음은 16. for와 range.
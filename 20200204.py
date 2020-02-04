# 2020.02.04 (화) 파이썬 다시 시작.

# unit25. 딕셔너리 응용하기

# 1. 딕셔너리에 키-값 쌍 추가하기
# setdefault : 키-값 쌍 추가
# update : 키의 값 수정, 키가 없으면 키-값 쌍 추가
a = {}
a.setdefault('e')
print(a)
# {'e': None}

a.setdefault('c', 500)
print(a)
# {'e': None, 'c': 500}

# 키의 값 수정하기 : update
a.update(e=300)  # 업데이트는 키 값이 문자열 기준으로, 따옴표를 생략하고 사용한다.
print(a)
a.update({1: 'one', 2: 'two'})  # 숫자로된 키 값을 사용하고 싶다면 딕셔너리로 만들어서 넣어준다.
print(a)
a.update({1: 'oneone', 2: 'twotwo', 3: 'three'})
print(a)
# 수정할 때도 사용하고, 추가할 때에도 사용한다.
# a.setdefault(1, 200) 불가.

# 반복가능한 객체를 사용하여 딕셔너리 사용하기
b={}
# b.setdefault([[123, '일이삼'],[456, '사오육']]) 이것은 업데이트만 가능하다.
b.update([[123, '일이삼'],[456, '사오육']])  # 키와 값의 쌍을 리스트로 묶고 그것을 또 리스트에
# 넣어서 딕셔너리로 넣는다.
print(b)
b.update(zip([123, 456],['일이삼일이삼', '사오육사오육']))
print(b)
# 혹은 zip([키들의 리스트],[값들의 리스트])를 이용하여 수정한닫. 서로 쌍이 맞아야 함.

# 딕셔너리에서 키-값 쌍 삭제하기 pop(키)
print('-------pop------')
c={}
c.update(e=500, f=300)
c.update({1:100, 2:200, 3:300})
print(c)
c.pop(2)
print('키 2를 뺌 : {0}'.format(c))
d = {'a': 100, 'b': 200}
print(d.pop('a'))
d.update(a=100)
print(d.pop('a', 333))
print(d.pop('asccas', '여기에 없음'))  # pop(삭제할 키 값, 기본값) 을 사용하면,
# 해당 딕셔너리에 키 값이 존재할 경우 해당 키-값 쌍의 값을 삭제 후 반환하고, 존재하지 않으면 기본값을
# 반환한다.
print(d)
del d['b']
print(d)
# 딕셔너리에서 임이의 키-값 쌍 삭제하기
'''
파이썬 3.5 이하에서는 popitem()을 사용하면 딕셔너리에서 임의의 값을 삭제하지만, 3.6 이상에서는
임의의 값이 아닌 마지막 키-값 쌍을 삭제한다.
'''
# 딕셔너리의 모든 키-값 쌍을 삭제하기
print('clear', a)
a.clear()
print(a)

# 딕셔너리에서 키의 값을 가져오기
e = {}
e.update(zip(range(1,6), [str(i) for i in range(101, 106)]))
print(e)
print(e.get(3))

# 딕셔너리에서 키-값 쌍을 모두 가져오기
f = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(f.items())
print(f.keys())
print(f.values())

# 리스트와 튜플로 딕셔너리 만들기
keys = {'a', 'b', 'c', 'd'}
g = dict.fromkeys(keys)  # dict.fromkeys(키리스트 혹은 튜플) 을 사용하면 값이 None인 딕셔너리를 생
# 성한다.
print(g)
# dict.fromkeys(키리스트, 특정값)을 사용하면 키들의 값을 모두 특정 값으로 저장한다.
h = dict.fromkeys(keys, 123)
print(h)

# defaultdict 사용하기 collections 모듈에 있다
from collections import defaultdict

aa = defaultdict(int)  # int로 설정하면 기본값이 0이 된다.
# 다른 값을 설정하고 싶다면 defaultdict(lambda: 'python') 처럼 람다 표현식을 쓰라고 한다.
print(aa['z'])

# 반복문으로 키-값 쌍 모두 출력하기

# f = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in f:
    print(i, end=' ')
print()
# 결과로는 키값만 출력된다. 키-값을 모두 출력하려면
for i in f.items():
    print(i, end=' ')
print()
# 아니면
for key, value in f.items():
    print(key, value)
print()
for key in f.keys():
    print(key, end=' ')
print()
for value in f.values():
    print(value, end=' ')
print()

# 딕셔너리 표현식 사용하기

keyyy = ['a', 'b', 'c', 'd']
ab = {key: value for key, value in dict.fromkeys(keyyy).items()}
'''
1. 키리스트를 만든다.
2. 키리스트를 이용하여 딕셔너리를 만들고, .items()를 이용하여 딕셔너리의 모든 값을 받는다.
3. 받은 값에서 키와 값을 분리하여 키는 key, 값은 value에 각각 집어넣는다.
4. 집어넣은 것을 key: value의 형태로 만들어 딕셔너리로 만든다.
5. 전체를 {}로 묶어 딕셔너리로 만든다.
'''
ac = {key: 3 for key in dict.fromkeys(keyyy).keys()}  # 키만 뽑아서 값을 0으로 만듦.
ad = {value: 0 for value in f.values()}  # 값을 키로 만듦.
ae = {value: key for key, value in f.items()}  # 값과 키의 자리를 바꾼다.
print(f, ae, sep='\n')

print(f)
af = {key: value for key, value in f.items() if value != 20}
print(af)

# 딕셔너리 안에 딕셔너리 사용하기
ag = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
} # 코딩도장에서 퍼옴.
# 찾을 때는
print(ag['Mercury']['mass'])

# 딕셔너리의 할당과 복사 : 딕셔너리도 함부로 할당하면 같은 객체로 취급한다.
# 이럴 때에는 .copy()를 이용하자.
ah = f
print(ah is f)
ah = f.copy()
print(ah is f, ah == f, sep='\n')

# 중첩 딕셔너리의 할당과 복사 : 이 또한 중첩 리스트에서와 같다. deepcopy를 사용해야 한다.
# deepcopy는 copy 모듈에 있다.

import copy
ai = copy.deepcopy(ag)
print(ai['Mars'] == ag['Mars'], ai['Mars'] is ag['Mars'])

# 오늘의 주목할 점은 딕셔너리의 반복문 사용이라고 한다.

'''
코딩도장 퀴즈
1 - 딕셔너리에서 키-값 쌍의 특정 키-값 쌍 제거는 pop(키) del 딕셔너리[키] 이다.
2 - 
    a. setdefault는 딕셔너링에 키-값 쌍을 추가한다. 맞는 것.
    b. setdefault는 키만 지정하면 값은 0으로 저장한다. 틀렸다. None으로 저장한다.
    c. keys는 딕셔너리의 키-값 쌍을 모두 가져온다. 틀렸다. 키만 가져온다.
    d. clear()는 딕셔너리의 모든 키-값 쌍을 삭제한다. 맞다.
    e. update는 딕셔너리에서 키의 값을 수정한다. 맞다.
3 - 딕셔너리의 모든 키를 출력하는 방법은
    1. for i in x:
    2. for i in x.keys():
    3. for i in x.items():
4 - 딕셔너리에서 값이 40인 딕셔너리를 삭제하는 방법은
    aa = {key: value for key, value in 딕셔너리.items() if value != 40}

'''

# 연습문제 평균점수 구하기
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum([i for i in maria.values()]) / len(maria)
# 멍청했다. maria.values 도 반복형 객체이므로 곧바로 sum()을 적용해도 된다.
print(average)




# 심사문제 키가 delta인 것과 값이 30인 키-값 쌍을 삭제해라.
# keys = input().split()
# values = map(int, input().split())
# x = dict(zip(keys, values))
# print(x)
# del x['delta']
# x = {key: value for key, value in x.items() if value != 30}
#
# print(x)


# 오늘의 파이썬! 오랜만의 파이썬 종료.


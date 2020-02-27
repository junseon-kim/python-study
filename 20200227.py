# 2020.2.27. 오늘의 파이썬 시작.

# unit 40. 제너레이터와 yield 알아보기

# 제너레이터 : 이터레이터를 생성해주는 함수. 발생자라고도 한다.
# 제너레이터는 함수 안에서 yield를 사용하면 만들어진다.

# 함수 안에서 yield 값 의 형태를 입력하면 제너레이터를 만들 수 있다.


def number_gen():
    yield 0
    yield 1
    yield 2
    yield 4
    return '에에에러러러'

try:  # 실험 결과 제너레이터를 할당해야 이터레이터가 만들어진다.
    g = number_gen()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    # next(number_gen())
    # next(number_gen())
    # next(number_gen())
    # next(number_gen())
    # next(number_gen())
    # next(number_gen())
    # next(number_gen())
    # next(number_gen())
except StopIteration as e:
    print(e)

# 제너레이터 객체에서 __iter__를 호출하면 self를 반환. 같은 제너레이터 객체가 반환된다.
# yield인 이유는 함수를 실행하는 중간에 코드실행을 바깥으로 양보하여서 이다.
# 호출하면 yield 하나의 줄만 실행하고, 바깥으로 코드실행을 양보한다.

# 제너레이터 안에서 return을 사용하면 사용하지 않았을 때와 똑같이 StopIteration 에러가 발생한다.
# 그리고 return의 반환값이 에러 메시지가 된다.

# 제너레이터 만들기

def mrange(stop):
    n = 0
    while n<stop:
        yield n
        n+=1

# 데이터로 저장하지 않고 작업을 실행한다는 점에서 매우 좋다.


fruit = ['apple', 'orange', 'grapes', 'strawberry', 'peach', 'pineapple']

def uppper_gen(x):
    for i in x:
        yield i.upper()


for i in uppper_gen(fruit):
    print(i)

# 대문자 변환이 손쉽게 뒤는 것을 알았다.

# yield from 으로 값을 여러번 전달하기

'''
yield from 반복가능한 객체
yield from 이터레이터
yield from 제너레이터
'''

def num_gen():
    yield from [1, 2, 3]

for i in num_gen():
    print(i)
# yield from은 객체에 들어있는 요소를 하나씩 밖으로 전달한다.

def three_gen():
    yield from mrange(3)

for i in three_gen():
    print(i)

# yield from에는 이터레이터, 제너레이터 모두 가능하다. yield from에 넣은 객체의 요소 하나를 순서대로
# 반환한다.

# 제너레이터 표현식 : []로 묶으면 리스트가 되지만, () = 소괄호 로 묶으면 제너레이터 표현식이 된다.

ab = (i for i in range(70) if i % 5 != 0)
for i in ab:
    print(i, end=' ')
else:
    print()
# 리스트가 아닌 제너레이터로 하는 것의 장점 : 저장공간 절약. 등

# 연습문제
def file_read():
    with open('./file practice/words3.txt') as file:
        lines = file.readlines()
        for line in lines:
            yield line.strip('\n')

for i in file_read():
    print(i)

# 심사문제 소수 제너레이터 만들기

def prime_number_generator(start, stop):
    # for k in range(start, stop):
    #     isprime = True
    #     for j in range(2, k):
    #         if k % j == 0:
    #             isprime = False
    #             break
    #     if isprime:
    #         yield k

    # while start<stop:
    #     isprime = True
    #     for i in range(2, start):
    #         if start % i == 0:
    #             isprime = False
    #             break
    #     yield start
    #     start += 1

    def isprim(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    yield from (qe for qe in range(start, stop) if isprim(qe))
    start +=1

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for abc in g:
    print(abc, end=' ')

#
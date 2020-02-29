# 2020.2.29. 오늘의 파이썬 시작!

'''
데코레이터(decorator) : 장식하는 도구. @staticmethod, @classmethod, @abstractmethod 등을 예로 들
수 있다.
함수(메서드)를 장식한다고 해서 데코레이터이다. = 장식자
데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용한다.

'''

# 데코레이터 만들기
# ex - 함수의 시작과 끝을 출력하는 데코레이터


def trace(func):  # 2. 데코레이터는 함수를 func로 받아옴.
    def wrapper():
        print(func.__name__, '함수 시작')  # func.__name__ 은 받아온 함수의 이름.
        func()  # 받아온 함수를 실행한다.
        print(func.__name__, '함수 끝')
    return wrapper  # trace는 감싸는 공장, wrapper는 감싸여진 물건으로 빗댈 수 있다.

def hello():
    print('hello')

def world():
    print('world')


trace_hello = trace(hello)  # 1. 데코레이터에 함수를 넣어 실행한 것을 할당.
trace_hello()
trace_world = trace(world)
trace_world()

def trace2(func):
    def wrapper(*args):  # 그냥 wrapper()로는 부족.
        print(func.__name__, '시작')
        func(*args)
        print(func.__name__, '종료')
    return wrapper


def add(a, b):
    return print(a+b)

trace_add = trace2(add)
trace_add(1, 2)
while True:
    # aa, ab = map(int, input('정수 둘을 입력하세요. : ').split())
    aa = ab = 0
    if aa == ab == 0:
        print('무한 루프 종료.')
        break
    trace_add(aa, ab)

# @로 데코레이터 사용하기.
'''
@데코레이터
def 함수이름():
    코드

의 형식으로 사용한다. 호출할 함수 위에 @데코레이터 형식으로 사용한다.
'''

@trace
def hello2():
    print('hello2')

@trace
def world2():
    print('world2')


hello2()
world2()

# 직접 함수에 넣어 할당해주지 않아도 위에 @데코레이터만 붙이면 된다.
# @trace
@trace2
def add2(a, b):
    return print(a+b)


add2(2, 3)  # 그러나 매개변수를 받으려면 데코레이터 역시 *args처럼 매개변수를 받는 형식이어야 한다.

# 데코레이터는 여러 개를 동시에 지정할 수 있다.
@trace
@trace2
def add3(a, b):
    return print(a+b)
# decorated_add3 = trace(trace2(add3)) 와 동작이 같다.
# add3가 trace2의 func자리에 들어가고, add3가 들어간 wrapper가 trace의 func자리에 들어간다.

# 매개변수와 반환값을 처리하는 데코레이터 만들기

def trace3(func):
    def wrapper(a, b):
        print('trace3')
        r = func(a, b)
        print(f'{func.__name__}(a={a}, b={b})')
        return r
    return wrapper

@trace3
def add_a(a, b):
    return a+b
print(add_a(10, 20))
# *args, **kwargs도 마찬가지로 언패킹에 주이하면 된다.

# 메서드에 데코레이터 사용하기 : 메서드에는 self가 들어가니 데코레이터 매개변수에도 self를 넣자.

def class_trace(func):
    def wrapper(self, *args):
        print('클래스 메서드 데코레이터 실험 시작.')
        r = func(self, *args)
        print('클래스 메서드 데코레이터 실험 종료.')
        return r
    return wrapper


class calc:
    def __init__(self):
        self.test1 = 20
        self.test2 = 40
    @class_trace
    def class_add(self, a, b):
        return self.test1 + self.test2 + a + b
c = calc()
print(c.class_add(100, 200))
# 중요 : 인스턴스를 만들 때에는,
# 인스턴스 = 클래스() 로, 괄호를 반드시 붙여서 만들어야 한다.

# 매개변수가 있는 데코레이터 만들기 ex) @deco(7)
# 매개변수가 있는 데코레이터를 만들기 위해서는, 함수가 하나 더 만들어져야 한다.
def ismut(x):
    def decorator(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print(f'{func.__name__}(a={a}, b={b})의 반환값은 {x}의 배수입니다.')
            else:
                print(f'{func.__name__}(a={a}, b={b})의 반환값은 {x}의 배수가 아닙니다.')
            return r
        return wrapper  # 안의 함수 반환
    return decorator  # 안의 함수 반환


@ismut(7)  # 데코레이터 제일 바깥의 함수의 매개변수를 넣는다.
def muti(a, b):
    return a*b

from random import randint as ran
print(muti(ran(1, 100), ran(1, 100)))

# 데코레이터를 여러개 사용하여 원래 이름이 안나올 때
# wrapper 함수 위에
'''
import functools
@functools.wraps(func)
를 사용하자.
'''
print('----------------------')



import functools


def ismut2(x):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print(f'{func.__name__}(a={a}, b={b})의 반환값은 {x}의 배수입니다.')
            else:
                print(f'{func.__name__}(a={a}, b={b})의 반환값은 {x}의 배수가 아닙니다.')
            return r
        return wrapper  # 안의 함수 반환
    return decorator  # 안의 함수 반환

@ismut(3)
@ismut(7)
def muti2(a, b):
    return a*b


@ismut2(3)
@ismut2(7)
def muti3(a, b):
    return a*b


print(muti2(ran(1,100), ran(1, 100)))
print(muti3(ran(1,100), ran(1, 100)))

# 클래스를 데코레이터 만들기
# 클래스를 데코레이터로 만들기 위해서는 __call__ 메서드를 구현해야 한다.


class Trace:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 종료')

@Trace
def hello_a():
    return print('hello')

hello_a()

# 훨씬 간단하게 데코레이터를 사용할 수 있다.
'''
1. __init__ 메서드에 호출할 함수를 초깃값으로 받고, self.func 처럼 속성으로 저장.
2. __call__ 메서드에 데코래이터를 만들고, 호출할 함수는 self.func 처럼 방금 저장한 속성을 호출.
3. 사용은 똑같이 @데코레이터이름 의 형식으로 함수 위에 사용.
4. 똑같이 trace_hello = Trace(hello) 의 형식으로도 사용할 수 있다.
'''

# 클래스로 매개변수가 있는 데코레이터 만들기
'''
간단히 요점만.
1. __init__에서 func를 받지 않고 매개변수 x를 받고 속성으로 저장한다.
2. __call__에서 호출할 함수에 넣을 매개변수를 받지 않고, func를 받는다.
3. __call__의 안에서 wrapper를 만들어 보통 데코레이터를 만들듯이 한다.
4. __call__ 메서드를 끝낼 때, wrapper를 반환해준다. return wrapper
5. @데코레이터(매개변수) 의 형식으로 사용한다.
'''
class tst:
    def __init__(self, x):
        self.x = x
    def __call__(self, func):
        def wrapper(a, b):
            print(f'{func.__name__}시작')
            r = func(a, b) + self.x
            print(f'a={a}, b={b}, x={self.x}')
            print(f'{func.__name__}종료')
            return r
        return wrapper

@tst(7)
def adder(a, b):
    return a+b


print(adder(3, 7))

# 연습문제 : 데코레이터로 자료형 검사하기

def type_check(type1, type2):
    def deco(func):
        def wrapper(a, b):
            if type1 == type(a) and type2 == type(b):
            # isinstance(객체, 클래스) 로 검사해도 되었다.
            # if isinstance(a, type1) and isinstance(b, type2):
                return func(a, b)
            else:
                raise RuntimeError('자료형이 다릅니다.')
        return wrapper
    return deco

@type_check(int, int)
def add_test(a, b):
    return a+b
print('---------------------------')
print(add_test(10, 20))
# print(add_test('hello', 'world'))

# 심사문제 : html 태크 데코레이터 만들기

# class html_tag:
#     def __init__(self, tag):
#         self.tag = tag
#
#     def __call__(self, func):
#         def wrapper():
#             line = f'<{self.tag}>{func()}</{self.tag}>'
#             return line
#         return wrapper

# 클래스 말고 작성해보자.
def html_tag(tag):
    def deco(func):
        def wrapper():
            # line = f'<{tag}>{func()}</{tag}>'
            # return line  원본. 6줄이 정답이길래 수정해 보았다.
            return f'<{tag}>{func()}</{tag}>'
        return wrapper
    return deco



a, b = input().split()
print('======================')
@html_tag(a)
@html_tag(b)
def hello_b():
    return 'Hello, world!'

print(hello_b())

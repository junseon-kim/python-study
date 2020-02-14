# 2020.2.14. 오늘의 파이썬 시작

# unit 29 함수 사용하기

'''
def 함수이름(매개변수):
    코드

'''
def hello():
    print('hello, world!')
hello()

# 함수를 작성하기 전에 호출하면 안된다.

def add(x, y):
    print(x+y)
add(1, 2)

# 독스트링, documentation string, docstring
# : 함수 맨 윗줄에 큰따옴표 세개를 입력하면 함수의 설명을 넣을 수 있다. """ """

def gggelp():
    """
    독스트링 시험용.
    :return: hi!
    """
    print('hi!')
print(gggelp.__doc__)
# 함수명.__doc__ 를 출력하면 독스트링이 출력된다.

def add2(x,y):
    return x+y
aa = add2(3, 5)
print(aa)

# 함수에서 값을 여러개 반환하기
"""
def 함수이름(매개변수):
    코드
    return 반환값1, 반환값2, ...

반환개수대로 받을 변수를 많이 둬도 되지만, 반환되는 것은 실제로는 튜플이고, 언팩이므로 하나의 변수에
받아서

"""

# 심사문제 사칙연산 함수 만들기

def calc(x, y):
    return x+y, x-y, x*y, x/y

# 오늘의 파이썬 종료.






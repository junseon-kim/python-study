# 2020.2.19. 오늘의 파이썬 시작.

# unit 33 클로저 사용하기(변수의 사용 범위 알아보기)

'''
전역 변수(global variable) : 함수를 포함하여 스크립트 전체에서 접근할 수 있는 변수
전역 범위(global scope) : 전역 변수에 접근할 수 있는 범위

지역 변수(local variable) : 변수를 만든 함수에서만 접근할 수 있고, 함수 바깥에서는 접근할 수 없다.
지역 범위(local scope) : 지역 변수를 접근할 수 있는 범위
'''

# 함수 안에서 전역 변수 변경하기
x=10
def aa():
    global x  # 이 함수 안에서 x를 전역 변수 x로 사용하겠다고 설정.
    # 혹은 존재하지 않는 변수를 전역 변수로 선언.
    x=20

    print(x)
aa()
print(x)

# 변수는 네임스페이스에 저장. locals() 를 사용하면 현재 네암스페이스를 딕셔너리 형태로 출력.

# 함수 안에서 함수 사용하기
def ab():
    x = 10
    def ac():
        nonlocal x
        x=20
        print(x)
    ac()
    print(x)
ab()

# global을 사용하면, 무조건 전역 변수를 사용한다.

# 클로저

def calc():
    a=3
    b=5
    def mul_add(x):
        return a*x+b
    return mul_add
c = calc()
print(c(1), c(2), c(3))
"""
함수 calc가 끝났는데도 c는 calc의 지역변수 a, b를 사용해서 계산을 하고 있다.
이렇게 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용
하는 함수를 클로저(closure)라고 한다.
"""
def calc2():
    a = 3
    b = 5
    def mul_add():
        nonlocal a, b
        a+=1
        b+=1
        return print(a, b)
    return mul_add
c = calc2()
c()
c()
c()
# 실험 결과, 클로저를 생성하면 지역 변수의 값이 3, 5로 계속 초기화되지 않고, 바뀐 값 그대로 유지
# 된다. 이는 아마도 calc2의 반환값이 mul_add이기 때문으로 판단된다.

# lambda 표현식으로 클로저 만들기
def calc3():
    a = 3
    b = 5
    return lambda x: a*x+b
c = calc3()
print(c(4), c(3), c(2), c(1))

# 연습문제 : 호출 횟수를 세는 함수 만들기
def counter():
    i = 0
    def count():
        nonlocal i
        i+=1
        return i
    return count

# 심사문제 : 호출할 때마다 1 감소 (클로저)

def countdown(n):
    n+=1
    def down():
        nonlocal n
        n-=1
        return n
    return down


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')


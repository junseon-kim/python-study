# 2019.12.24 Third day. how to debug 부터.

print('python! third day!!')

'''
파이썬은 들여쓰기가 매우 중요하다(indentation Error)


'''

# def 쓰는법 (함수)
'''
def 이름(받을 변수, x, t, ...) :
    실행할 것
    return 반환할 것
'''
# 호출 이름(x, y)
# import : 모듈을 불러온다.

def add(x, y) :
    return x+y
def mult(x, y) :
    return x*y
def divi_2(x) :
    return x/2
# input('윗변의 길이는?') 이라고 하면 윗변의 길이는? 하고 묻고 바로 옆에 입력이 가능하다.
'''
num = int(input('출력할 숫자를 입력하세요. : '))
print(num)'''

#import trapezium_area as ta ===== trapezium_area 라는 파일을 ta로 부를 것이다.
if __name__ == "__main__" :
    print(add(5, 10))

# if __name__ == "__main__" : 이라고 하면 import 했을 때 test문구를 출력하지 않는다.

# 함수
# 사각형의 넓이를 구하는 함수
def rectangle(x,y) :
    return x*y

'''
def 함수 이름(parameter, ...) :
    수행문 1
    수행문 2
    수행문 3
    ...
    return 반환값
'''
# 함수를 제외하고 메인 부분을 실행 후, 호출하면 함수로 돌아와 함수 실행 후 돌아감.
# print("사각형의 넓이는 :", rectangle(x, y)) 이라면, rectangle을 먼저 실행 후, print문을 실행한다.

# 함수 vs 함수

def f(x) :
    return 2*x+7
def g(x) :
    return x**2 # x의 제곱.
x = 2
print(f(x) + g(x) + f(g(x)) + g(f(x)))
# parameter와 Argument.
# parameter : 함수의 입력 값 인터페이스
# Argument : 실제 Parameter에 대입된 값.

'''
1. 반환값이 없을 때
    1-1 Parameter가 없다면, 수행문만 수행.
    1-2 Parameter가 있다면, 인자를 가지고 수행문을 수행.
2. 반환값이 있을 때
    2-1 Parameter가 없다면, 수행문을 수행 후, 결과값을 반환.
    2-2 Parameter가 있다면, 인자를 가지고 수행문을 수행 후, 결과값을 반환.
'''

# 함수의 호출 방식. call by value, call by reference
'''
파이썬의 함수 호출 방식.
객체의 주소가 함수로 전달되는 방식.

전달된 객체를 참조하여 변경시 호출자에게 영향을 준다.
그러나 새로운 객체를 만들 경우 호출자에게 영향을 주지 않는다.
'''
#예제.

def spam(eggs) :
    eggs.append(1) # eggs의 주소값의 리스트에 1을 추가. 현재 eggs는 ham의 주소값을 가지고 있음.
    eggs = [2, 3] # eggs라는 것에 다시 [2, 3]의 주소값을 할당. eggs의 주소값이 바뀜.

ham = [0]
spam(ham)
print(ham) # [0,1]

def test(t) :
    t= 20
    print("in function :",t)

x= 10
print("Before :", x)
test(x)
print("After :", x)

# 변수의 범위. Scoping rule
# 지역 변수 (local) : 함수 내에서만 사용.
# 전역 변수 (global) : 프로그램 전체에서 사용.

def x():
    # global s    라고 쓰면 이 함수 전체에서 사용 가능한 변수가 된다.
    s = "I love london!"
    print(s)
s = "I love Paris!"
x()
print(s)

print('___---------')
def y():

    m = "I love london!"
    print(m)
m = "I love Paris!"
x()
print(m)

# Swap 함수를 통해 변수간의 값을 교환하는 함수.
a = [1, 123, 456, 4, 5]

def swap(b, x, y) :
    temp = b[x]
    b[x] = b[y]
    b[y] = temp



print(a)
swap(a, 1, 2)
print(a)

# 재귀함수 : 자기 자신을 호출하는 함수. 점화식과 같은 재귀적 수학 모형을 표현할 때 사용.

# 재귀함수로 팩토리얼을 구현해보자.
'''
1. 그냥 재귀
def facto(x) :
    if (x==1) :
        return 1
    return x * facto(x-1)
fivefac = facto(6)
print(fivefac)

'''
# dp 로 해보자.

def facto(x) :
    if (cal_value == 1): # 계산할 변수가 1이면 1 반환.
        return 1
    elif (x==1): # x가 감소하여 1에 도달하면 계산을 전부 한 것이므로 리스트의 제일 끝값을 반환. 이전의 return은 이것의 결과이므로 모든 반환값이 이것이 된다.
        return fist[cal_value-2]
    elif ( x == cal_value ): # x가 cal_value와 같을 때에는 계산 리스트에 그저 붙인다.
        fist.append(x)
    else: # 팩토리얼을 계산할 때에는 현재의 값과 리스트의 끝 값을 곱하면 된다.
        fist.append(x*fist[len(fist)-1])
    return facto(x-1)





fist = [] # 연산을 위해 전역 변수로 선언.
# cal_value = int(input("팩토리얼을 계산할 수를 입력하세요. : "))
# print(facto(cal_value)) 20까지 정상 작동한다. 100 넣으니까
# 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223
# 758251185210916864000000000000000000000000 가 나온다. ?????


# 코딩 컨벤션과 함수 작성법. 좋은 코드, 무엇인가?
# 코딩 컨벤션 : 프로그래밍을 하는 규칙.
# 파이썬 코딩 컨벤션 : 일관성. 딱히 정해진 것은 없다.
'''
나의 규칙. :은 항상 띄우지 않는다. 연산자는 붙인다. indantation은 4space로 한다.
        원래는 tab으로 하지만 동영상을 따라보자.
        
        PEP8 : 들여쓰기는 4space, 한 줄에 79자, 불필요한 공백은 ㄴㄴ
        - = 연산자는 1칸 이상 안 띄움.
        - 주석은 항상 갱신, 불필요한 주석은 삭제
        - 소문자 l(엘), 대문자 O(오) 대문자 I(아이) 금지
        - 함수면은 소문자로 구성, 필요하면 _로 나눔
        - flake8 모듈로 체크해보자.

    함수
        - 함수 이름에 함수의 역할, 의도가 명확히 드러낼 것. 줄 수는 최대한 짧게.
        - 하나의 함수에는 유사한 역할을 하는 함수만.
        - 인자로 받은 값 자체를 바꾸지 말아라.
    함수는 언제 만드나?
        - 공통적으로 사용되는 코드는 함수로 변환
        - 복잡한 수식 -> 식별 가능한 이름의 함수로 변환
        - 복잡한 조건 -> 식별 가능한 이름의 함수로 변환      
'''


# 문자열 다루기 : 시퀀스 자료형. 문자형 data를 메모리에 저장.
# 영문자 1글자는 1byte를 사용.

import sys
print(sys.getsizeof('a'))
# ASCII 0 = 48, a = 97, A = 65

# Python 정수형 : 1. int - 4바이트의 크기. 2. long - 무제한
# python 실수형 : float - 8byte
'''
 문자열의 각 문자는 개별 주소를 가진다.
 C의 문자열과 비슷.
'''
a = 'abcde'
print(a[0], a[2])
print(a[-1], a[-5])

a= '1234567890'

print(a[:])
print(a[4:10])
print(a[-50:50])
print(a[::1])
print(a[::2])
print(a[::3])
print('1' in a) # ['문자' in 문자열] '문자'가 들어있으면 True, 없으면 False.
print(a[::-1])
print(a[::-2])# 끝부터 출력. 단, 출력 후 1칸을 띄운다.
print(a*2)
print((a+'\n')*3)

'''   문자열 함수들.
len(a) : 문자열 a의 길이를 반환.
a.upper() : 문자열 a를 모두 대문자로 바꿈.
a.lower() : 문자열 a를 모두 소문자로 바꿈.
a.capitalize() : 첫 글자를 대문자로 바꿈.
a.title() : 띄어쓰기 후에 있는 모든 단어의 첫 글자를 대문자로 변환.
a.count('abc') : 문자열 a에 abc가 들어간 횟수를 반환.
a.find('abc') : 문자열 a에 abc가 있는 index를 반환.
a.rfind('abc') : 오른쪽 끝부터 문자열 a에 abc가 있는 index를 반환.
a.startswith('abc') : abc로 시작하는 문자가 있는지 여부 반환.
a.endswith('abc) : abc로 끝나는 문자가 있는지 여부 반환.

a.strip() : 문자열 a의 양쪽 끝에 불필요한 공백을 지움.
a.rstrip() : 오른쪽의 공백만 지움.
a.lstrip() : 왼쪽의 공백만 지움.
a.split() : 공백을 기준으로 문자열을 자르고, 리스트로 반환.
a.split('abc') : abc를 기준으로 문자를 나누고 리스트로 반환.
a.isdigit() : 문자인지, 숫자인지 구분하는 것. (숫자형 문자형일 때 True)
a.islower() : 소문자인지 True, False
a.isupper() : 대문자인지 True, False
'''

ttt ='aBcDeFgh'
t4 = ' aB Cd eF gh aB Cd '
print(ttt.lower())
print(ttt.upper())
print(ttt.capitalize())
print(t4.title())
print(t4.split())
print(t4.split('eF')) # 구분할 문자를 빼고 양쪽의 문자를 반환한다.
print(t4.find('a'))
print(t4.rfind('a'))
print(t4.startswith(' aB')) #startswith는 문자열 전체를 한 단어로 취급하여, index 0 부터 본다.
print(ttt.endswith('h')) # endswith도 똑같이 문자열 전체를 한 단어로 취급, 끝부터 본다.
print(t4.islower())
print(t4.isupper())
print(t4.strip())
print(t4.rstrip())
print(t4.lstrip())
print(t4.upper().count('A'))
# 작은 따옴표는 1. 따옴표로 (") 문자열을 선언, (')를 그냥 사용
# 2. 작은 따옴표(')로 선언, (\')로 사용.

# enter를 사용하고 싶다면,
print('''이렇게 사용하면
엔터를 파이썬이
인식을
한다.''')
print('혹은 \n 을 사용한다. \\n을 사용한다는 \n것이다.')

# \b = 백스패이스, \t = 탭, \n = 줄바꿈, \e = ESC

# 2019.12.24.(화) 오늘의 파이썬 종료!
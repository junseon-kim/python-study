# 2020.2.24. 오늘의 파이썬 시작!

# unit 38. 예외 처리 사용하기

# 예외(exception) : 코드를 실행하는 중에 발생한 에러.


def div10(x):
    return 10/x

# print(div10(0))  # ZeroDivisionError: division by zero
# 위와 같이 10/0은 값을 구할 수 없다.
# 예외 발생시 스크립트 실행을 중단하지 않고 계속 실행하게 해주는 예외 처리 방법 : try, except


try:
    print(div10(0))
except:
    print("예외 발생!")


print('정상 실행')

# 특정 예외만 처리하기
try:
    div10(0)
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:
    print('잘못된 인덱스입니다.')

'''
try:
    실행될 코드
except 에러이름1:
    해당 에러가 발생했을 때 실행될 코드
except 에러이름2:
    해당 에러가 발생했을 때 실행될 코드

try는 그저 코드 실행. except는 코드를 실행하다 에러, 예외가 발생할 때에, 스크립트를 중지하지 않고
그 상황에 실행할 코드를 설정한다.
'''

# 에러 메시지 받아오기
try:
    print(div10(0))
except ZeroDivisionError as e:
    # e는 에러 메시지를 담을 변수이다.
    print('숫자를 0으로 나눌 수 없습니다.', e)

# else와 finally 사용하기
# else는 예외가 발생하지 않았을 때 실행할 작업을 한다.

try:
    y = div10(2)
except ZeroDivisionError as e:
    print(e)
else:
    print(f'정상 실행! : {y}')

# 예외와는 상관없이 항상 코드 실행하기
# finally는 예외가 발생하거나 말거나 항상 실행한다.

try:
    aa = div10(3)
except ZeroDivisionError as e:
    print(e)
else:
    print(f'정상 실행! : {aa}')
finally:
    print('10 나누기 3을 실행!')

# try 는 함수가 아니므로 스택 프레임(변수를 저장하는 칸)을 만들지 않는다고 한다.
# 즉, 전역 스코프에서 예외사항만 건든다.

# 예외 발생시키기 : raise Exception('에러메시지')

try:
    ab = 3
    if ab == 3:
        raise Exception('ab가 3이네요.')
except Exception as e:
    print(e)

# 예외를 발생시키면, except를 만날 때까지 상위 블록으로 이동한다.
print('---------------------')
def test1():
    try:
        print('1')

        raise Exception('2')
    except Exception as t:
        print(t)
        raise  # 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘긴다.

try:
    test1()

    raise IndexError('인덱쯔에렁')
except IndexError as y:
    print(y)
except Exception as e:
    print(e)

# assert로 예외 발생시키기. 조건문 형식으로, 참이면 넘어가고 거짓이면 예외가 발생한다.
x = 2
# assert x==5, 'x가 5가 아닙니다.'
# assert 조건식, '에러메시지'
# assert는 디버깅 모드에서만 실행되고, 파이썬은 기본적으로 디버깅 모드이다.
# 디버깅 모드 해제하려면 python -O 스크립트파일.py

# 예외 만들기 : Exception을 상속받아 클래스를 만들고, 기반 클래스의 __init__에 에러메시지 전달.
class expt(Exception):
    def  __init__(self):
        super().__init__('에러다')


class NotThreeError(Exception):
    def __init__(self):
        super().__init__('3이 아닙니다.')

x = 2
try:
    if x!=3:
        raise NotThreeError
    print(x)
except NotThreeError as e:
    print('예외가 발생했습니다.', e)

# 연습문제 : 파일 예외 처리하기
try:
    file = open('maria.txt', 'r')
except FileNotFoundError:
    print('파일이 없습니다.')
else:
    s = file.read()
    file.close()

# 심사문제
class NotPalindromeError(Exception):  # 에러 정의
    def __init__(self):
        super().__init__('회문이 아닙니다.')
def palindrome(s):
    if s[:] != s[::-1]:  # 회문 판별
        raise NotPalindromeError  # 조건을 걸고, 어차피 raise만 해도 except를 실행하므로
    # try와 except로 해줬던 것을 빼고 간단히 if만으로 실행하게 한다.
    print(s)  # 조건 : 회문이면 문자열 출력. 예외발생시 except를 찾으므로 else로 따로 실행할 필요가
    # 없다.

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)


# 오늘의 파이썬 종료.

# 2020.2.16. 오늘의 파이썬 시작.

# unit 31. 함수에서 재귀호출 사용하기
# 재귀 호출(recursive call) : 함수 안에서 자기자신을 호출하는 방식
# 파이썬의 최대 재귀 깊이(maximum recursion depth)는 1000으로 정해져 있다.
# 그래서 종료조건을 만든다.


def hello(count):
    if count <1:
        return 0
    print('hello %d' % count)
    hello(count-1)


hello(5)

# 재귀호출로 팩토리얼 구하기. 공부 전에 직접 해본다.

faclist = [1, 2]
def facto(number):
    if number <3:
        return faclist[number -1]
    elif len(faclist) == number:
        return faclist[len(faclist)-1]
    else:
        faclist.append(faclist[len(faclist)-1]*(len(faclist)+1))
        return facto(number)

# num = int(input('자연수를 입력하세요. : '))
# result = facto(num)
# print(result)

# 연습문제 재귀호출로 회문 판별하기

def is_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        print(word, word[1:-1], word[1:-2])
        return is_palindrome(word[1:-2])
# 슬라이스에서, [-1] 은 반대로, [1:-1]은 두 번째에서 뒤에서 두 번째까지다.
is_palindrome('hello')
is_palindrome('level')
is_palindrome('wdfg')

# 심사문제 : 재귀호출로 피보나치 수 구하기
# fiblist = [0, 1]  내가한 것 재귀 + dp
# def fib(num):
#     if num == 0:
#         return fiblist[num-2]
#     fiblist.append(fiblist[len(fiblist)-1]+fiblist[len(fiblist)-2])
#     return fib(num-1)


def fib(num):  # 답이다. 맞았지만 답을 보니 진짜 재귀를 알 것 같다.
    if num <2:
        return num
    return fib(num-1)+fib(num-2)

n = int(input())
print(fib(n))
'''
이 피보나치 수를 구하는 함수는, 밑바닥에서 연산을 시작해야하므로, num을 제외한 현재의 값으로 연산을 하
지 않고, 끝에서부터의 연산을 return에 넣고, 맨 끝에서의 반환조건을 넣어 맨 끝에서만 값이 구해지고, 나
머지는 그 값만을 이용하여 연산이 가능하도록 만들었다. 재귀함수란 것이 이런 것이구나.
'''

# 오늘의 파이썬 종료! 재귀함수를 배웠다.

# 2020.2.18. 오늘의 파이썬 시작.

# unit 32. 람다 표현식으로 함수 만들기
# def를 이용한 함수 정의


def plus_ten(x):
    return print(x+10)

# 람다 표현식으로 만들기
lambda x: x+10  # 이대로는 아무것도 안되므로 이 표현식을 변수에 할당한다.
plus_ten2 = lambda x: print(x+10)
plus_ten(15)
plus_ten2(15)

# 람다 표현식 자체를 호출하기
(lambda x: x+10)(1)  # 람다 표현식을 괄호로 감싸고 그 밖에 괄호로 값을 넣어준다.

# 람다 표현식 안에서는 변수를 선언할 수 없으므로 변수가 필요할 때에는 def를 이용하자.
# 람다 표현식을 인수로 사용하기
def plus_two(x):
    return x+2
print(list(map(plus_two, [1, 2, 3])))
# 위의 방법은 3줄이 필요하다. 그러나 람다 표현식을 사용하면,
print(list(map(lambda x: x+2, [1, 2, 3])))

# 한 줄만 사용하게 할 수 있다.

# 람다표현식에서 조건부 표현식 사용하기 lambda 매개변수: 식1 if 조건식 else 식2
# 조건식을 만족할 때에 식1을 사용, 조건식을 만족하지 않으면 식2를 사용한다.

aa = lambda x: str(x) if x%3 ==0 else x
print(list(map(aa, list(range(1, 11)))))

# 람다 표현식에서는 elif를 쓸 수 없고, if else의 연속으로만 된다.
ab = lambda x: x+1 if x%3==0 else x+2 if x%4==0 else x+3
# ab = lambda x: 식1 if 조건식1 else 식2 if 조건식2 else 식3
# 조건식1이 참이면 식1, 조건식2가 참이면 식2, 전부 거짓이면 식3을 실행한다.
# 보통 이렇게 되면 def를 사용하자.

# map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
ac = lambda x, y: x*y
print(list(map(ac, a, b)))
# 람다 표현식에서 필요한 변수의 개수를 맞춰준다.

# filter(함수, 반복가능한 객체) 사용하기 : filter는 함수에 반복가능한 객체를 집어넣고, 그 중에서
# 함수의 반환값이 True일 경우에만 값을 반환한다.
def lese_10(x):
    return x<10
print(list(filter(lese_10, list(range(-5, 20)))))  # 필터를 통과하면 필터 객체로 반환되기 때문에
# 리스트로 변환해준다.
# 람다 표현식 사용하기
ad = list(filter(lambda x: x>5 and x<10, list(range(-5, 20))))
print(ad)

# reduce(함수, 반복가능한 객체) 사용하기 : 반복가능한 객체의 각 요소를 지정된 함수로 처리한 뒤
# 이전 결과와 누적해서 반환하는 함수
from functools import reduce
def ae(x, y):
    return x+y
print(reduce(ae, [1, 2, 3, 4, 5]))
# 1+2 = 3, 3+3 = 6, 6+4 = 10, 10+5 = 15

# reduce로 최대, 최솟값 구해보기
af = lambda x, y: x if x>y else y
ag = lambda x, y: x if x<y else y
print('max', reduce(af, list(range(-5, 20))))
print('min', reduce(ag, list(range(-5, 20))))

# 연습문제 : 이미지 파일만 가져오기
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: '.png' in x or '.jpg' in x, files)))
# 문자열 메서드를 이용하여 수정
print(list(filter(lambda x: x.find('.png') != -1 or x.find('.jpg') != -1, files)))
# .find 는 반환값이 -1이 아니면 찾았다는 것이므로, != -1 을 사용하여 판단해준다.

# 심사문제 : 파일 이름 한꺼번에 바꾸기
files = input().split()
print(list(map(lambda x: '{0:0>3}'.format(x.split('.')[0]) +'.'+ x.split('.')[1], files)))
print(list(map(lambda x: '{0:0>3}.{1}'.format(*x.split('.')), files)))  # 언패킹


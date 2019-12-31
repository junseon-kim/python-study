# 2019.12.31 (화) 오늘의 파이썬 시작. 코딩도장 22.2부터.

a = [0, 0, 0, 0, 0]
b = a

# 이렇게 하면 리스트는 2개일 수 있지만, 실제로는 1개라고 한다.
print(a is b)  # is 는 객체의 동일성 여부를 판단. True가 나왔으므로 두 객체는 같은 객체.
print('Before')
print(a, b, sep='\n')
b[2] = 99
print('After', a, b, sep='\n')  # b만 바꿔도 a까지 바뀌는 것을 알 수 있다.
# 즉, a와 b는 이름만 다를 뿐 같은 객체. 주소를 공유한다.

# a와 b를 완전히 다른 두 객체로 만드려면 copy를 사용.
b = a.copy()  # copy()는 복사한 리스트를 반환.
print('copy : ', a is b) # a is b 의 결과는 False. 복사했지만 둘은 같은 객체가 아니다.
# 실험 : 만약 b = a 가 아닌 b = [0, 0, 0, 0, 0](a의 내용)을 하면?
a = [0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0]
print('ex : ', a is b)  # a is b의 값이 False로 나온다. 한 객체를 다른 객체로 집어넣는 것이
# 같은 주소를 공유하게 만든다.
a = 1
b = 1
print(a is b)  # 다만 파이썬은 0? 1인가부터 256? 255까지는 뭘 해도 같은 주소를 공유한다고 한다.
a = [1]
b = [1]
print(a is b)  # 리스트로 만들면 달라진다.
# 결론 : 내용을 할당하면 다른객체, 객체를 할당하면 같은 객체.
a = list(range(10))
b = a.copy()
b[2] = 50
print('is', str(a is b), a, b, sep='\n') # copy를 이용하면 원본을 건드리지 않고도 수정이 가능.


# 인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)
# enumerate(리스트) 인덱스와 값을 반환
for index, value in enumerate(a, start=1):
    print(index, value)
# start=1은, 실제 시작 인덱스는 건들지 않고 그저 출력 값만 바꾸는 것. 1부터 시작.
# enumerate(a, 1)로 줄일 수 있다.
print(enumerate(a))
print(list(enumerate(a)))
print(list(enumerate(a))[0])
print(list(enumerate(a))[0][1])
b = list(enumerate(a))[0]
print(b)
print(type(b))  # 예상대로 튜플이 나왔다.
# enumerate는 튜플로 이루어진 리스트로 이루어진 객체이다.
print(type(enumerate(a)))
'''
min(리스트) : 리스트의 최소값 반환
max(리스트) : 리스트의 최대값 반환
sum(리스트) : 리스트의 합 반환
'''
# sum을 문자열 리스트에 해보면 어떻게 될까?
a = ['Hello', 'World']
b = a[0] + a[1]
print(b)
# print(sum(a)) # 문자열 리스트는 더할 수 없었다.

# 리스트 컴프리헨션
a = [i for i in range(10)] # [식 for 변수 in 시퀀스객체]
print(a)
# 식에는 for에서 사용하는 변수를 이용해야 식이 바뀌면서 리스트에 들어간다.
a = [i*3 for i in range(1, 11)]
print(a)
a = [i for i in range(10) if i%2==0]
print(a)  # 1. for의 결과를 if로 2. i를 이용한 식을 if로
a = [i*2 for i in range(1, 11) if i%2==0]
print(a) # 결과는 for의 결과를 if에 넣고, 또 그 결과가 참이면 식에 대입한다.

# 리스트안의 중첩 for문

# a = [i for i in range(1) if i%2==0 for j in range(2) if j%2==0]
'''
포와 이프는 각 1세트로 움직이고, 제일 왼쪽의 포문이 제일 바깥쪽의 포문이 되어
실행된다.
'''

# 리스트에 map을 사용해보자.
# map : 리스트의 요소를 지정된 함수로 처리해주는 함수. 원본 리스트를 변경하지 않고 새 리스트를 생성한다.

a = '23 50 60 83 69 835 393 57329 9205 9538 34'
print(a)
# 내가 boj를 풀 때 자주 쓰는
a = list(map(int, a.split()))  # a대신 input()을 넣어서 입력받을 때 썼다.

# 튜플
a = tuple(i for i in range(10))
print(type(a), a, sep=' : ')
b = (i for i in range(10))  # 과연 ()만 씌워도 튜플이 될까?
print(type(b), b, sep=' : ')
# 안됀다 generator라고 나온다. 그저 값을 만드는 객체이다. tuple을 반드시 붙여야 한다.
print(list(b))

a = list(range(10))
print(a)
a[len(a):] = [5]  # 슬라이스는 시퀀스 객체만 할당 가능.
print(a)

# 코딩도장 심사문제. 정수 범위를 지수로 하는 2의 거듭제곱 리스트 만들기
# 단, 앞과 뒤 2번째는 전부 삭제.
start, stop = map(int, input().split())
a = [2**i for i in range(start, stop+1) if not(i == start+1 or i == stop-1)]
print(a)
# 코드 길이가 짧을 뿐, 비효율적이다. pop(1), pop(-2)하면 된다.
# 오늘의 파이썬 종료. 개인 사정으로 짧게 하고 장고로 넘어간다.
# 2019.12.29 (일) 오늘의 파이썬 시작

# 코딩도장 16 for와 range

'''
for 변수 in range(반복할 횟수):
    반복할 코드
'''
# range는 리스트가 아닌 (반복 가능한)객체를 만들어낸다.
print(range(10), 'range(10)를 출력하면 range객체가 출력된다.')
print(list(range(10)), '리스트를 만드려면 list()를 씌워주자.')
# 파이썬 2.7에서는 range도 리스트를 생성했다고 한다. 그래서 xrange를 사용했다고 한다.
a = reversed(range(5, 30, 2))
print(list(a)) # reversed를 사용하면 range의 순서가 바뀐다.

for i in range(5): # for 문의 i를 안에서 바꿔도 아무 상관 없다. 이유는, range로 계속 덮어쓰기 때문.
    print(i)
    i = 11

a = list(range(3, 40, 3))
b = tuple(a)
print(b)
c = 'MONGODATABASES'
for i in a:
    print(i, end=' ')
else:
    print('list')
for i in b:
    print(i, end=' ')
else:
    print('tuple')
for i in reversed(c):
    print(i, end=' ')
else:
    print('string')

# range 대신 다른 시퀀스 객체를 넣어도 무방하다.

# while문.
'''
i = 0           초기식
while i < 100:  조건식
    print(i)    실행할 코드
    i += 1      변화식
'''

# random 모듈 사용하기
import random
print('random')
print(random.random()) # random 모듈의 random함수
for i in range(5):
    print(random.random())
print('randint')
for i in range(5):
    print(random.randint(1, 10)) # random 모듈의 randint 함수 사용. randint(a, b) 는 a~b 까지의 난수를 생성.

a = ['apple', 'orange', 'pineapple', 'banana', 'cherry']
for i in range(5):
    print(random.choice(a)) # random.choice(시퀀스 객체) 함수는 넣어둔 시퀀스 객체에서 랜덤으로 값을 하나씩 뽑는다.
print('dict')
b = dict(zip(list(range(100, 105)), a)) # key 는 1~5, 값은 a에 있는 것을 넣음.
print(b)
for i in range(5):
    print(random.choice(list(b.values()))) # 과연 딕셔너리는 어떻게 출력 될까?
    print(random.choice(list(b.keys())))
    # key를 1~5로 설정했더니 오류가 계속 났다. 이유는, 시퀀스 객체가 들어가면, 그 길이를(len) 계산하여
    # 0 부터 len(객체) 까지 반환을 하는데, 딕셔너리는 딕셔너리[key]이기 때문에 계속 오류가 나는 것이었다.
    # 이것으로, 딕셔너리를 random.choice로 보내어 랜덤으로 밸류나 키를 가져오고 싶다면,
    # list(b.keys()) 나 list(b.values())를 사용해야 함을 알았다.

# N = int(input())
# for i in range(N):
#     for j in range(2*(N+i)):
#         if j > N+i:
#             break
#         elif j >= N-i-1 and j <= N+i-1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# go, stop = map(int, input().split())
# for i in range(go, stop+1):
#     print('Fizz'*(i%5==0) + 'Buzz'*(i%7==0) or i)

# 오늘의 파이썬 종료. 하려고 했으나 django에서의 문제로 class를 잠깐 본다.

'''
class는 객체를 표현하는 방법이다. 객체 지향(object oriented) 프로그래밍이라고 한다.
클래스에는 메서드(mathod)와 속성(attribute)이 있고, 메서드는 기능, 속성은 데이터이다.
클래스를 선언하는 방법은
class 클래스이름:(콜론)
    def 메서드이름(self, 다른 매개변수, ...):
        코드
        # 메서드는 첫 매개변수는 반드시 self로 하여야 한다.
'''


class knight: # camelCase 표기법 : 단어의 첫글자를 첫 단어는 소문자, 나머지는 대문자로 표기하는 방식.
    def __init__(self, name, age, address): # __init__은 initialize. 초기화하는 것이다.
        # 이 메서드는 인스턴스에 클래스를 할당할 때에 실행된다.
        self.hp = 500 # 이 클래스의 hp라는 객체에 500을 할당한다.
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("'Hello, I'm knight of 카타리나, 지크벨트")

    def hello(self):
        self.greeting() # 메서드에서 자신의 메서드를 또 호출하려면 self.메서드()의 형식으로
        #사용해야 한다. self를 붙이지않으면, 외부의 함수를 호출하는 것이다.

    def tellMaxHp(self):
        print(self.hp)

    def tellName(self):
        print(self.name)

# james = knight() # 클래스는 특정 개념을 표현한 것일 뿐, 사용시에는 instance(인스턴스)를 생성
# 해야 한다. james 같은 것이 인스턴스이다.

# mathod 호출하기
# james.greeting() # 인스턴스를 통해 호출하는 메서드를 인스턴스 메서드라고 한다.

# int, list, dict도 클래스였다. 파이썬에서는 자료형도 클래스다. 이래서 객체 지향.
# type을 사용하여 객체가 어떤 클래스인지 알 수 있다.
# print(type(james))

# 인스턴스와 객체는 같다. 보통 객체만 말할 때는 그냥 객체라고 하나, 클래스와 연관지을 때는
# 인스턴스라고 한다.


a = list(range(10))
b = list(range(20))
# a, b는 객체이다. 그리고 a, b는 list클래스의 인스턴스이다.

# 특정 클래스의 인스턴스인지 확인하기
# isinstance(james, knight) # isinstance(인스턴스, 클래스)

# 예제. 실수인지 판단하기
N = 5.6
print(isinstance(N, int)) # N이라는 인스턴스가 int에 속하는지 알아보는 것.
print(isinstance(N, float)) # N이라는 인스턴스가 float에 속하는지 알아보는 것.

# 속성(attribute) 만들기 : __init__ 메서드 안에서 self.속성이름 에 값을 할당한다.

# self 의 의미. 인스턴스 자기 자신.
Rose = knight("Rose", 20, 'earth')
Rose.tellName()

# format()
Q = 123456
W = 'qweerr'
print('의미없는 숫자 {0}, 의미없는 문자 {1}'.format(Q, W))

# '{0} {1} {2}'.format(a, b, c)는 {0}에 a, 순서대로 b, c가들어가게 한다.
# 그럼 순서를 바꾸면?
print('{0} 이렇게 {1} 해도 {0} 되는지 {1} 모르겠다. {0}'.format(Q, W))
# 된다. {0} 과 {1}은 0번째와 1번째를 의미하는 것. 얼마든지 써도 된다.

# 지금 필요한 것은 여기까지. 클래스는 나중에 또 보도록 하자.


# 2020.2.21. 오늘의 파이썬 시작.

# unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기

# 클래스에서 속성은 클래스 속성과 인스턴스 속성 두가지의 종류가 있다.
class Person:
    bag = []  # 이렇게 클래스에 직접 속성을 넣는 것이 클래스 속성.
    def put_bag(self, thing):
        self.bag.append(thing)

james = Person()
maria = Person()

james.put_bag('1000만원')
maria.put_bag('자동차키')
print(Person.bag)
print(james.bag)
print(maria.bag)

# 결과로 보아 클래스 속성은 클래스 전체에 적용되고, 인스턴스 속성은 인스턴스에만 적용된다.

# 보통 클래스 속성은 해당 클래스의 이름, 즉 self.bag이 아닌 Person.bag로 사용한다.
# 속성을 찾는 과정은 현재 인스턴스 내에서 찾고, 그 다음 클래스에서 찾는다.

# 정적 메서드
class test1:
    @staticmethod  # 메서드 위에 @staticmethod 를 붙이면 그 밑에 있는 메서드는 정적 메서드가 된다.
    def a1(a, b):  # 정적 메서드는 매개변수에 self를 넣지 않는다.
        pass
'''
정적 메서드는 test1.a1(10, 20) 처럼 클래스에서 바로 호출한다.
정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없다.
그러므로 보통 인스턴스 속성, 인스턴스 메서드가 필요없을 때 사용한다.

정적 메서드는 순수 함수를 만들 때 사용.
순수 함수(pure function) : 메서드의 실행이 외부 상태에 영향을 끼치지 않는 함수.

인스턴스의 내용을 변경해야 할 때에는 인스턴스 메서드, 인스턴스의 내용과는 상관없이 결과만 구하면 될
때는 정적 메서드.

'''
class test2:
    pay = 20

    @classmethod
    def a2(cls, a, b):  # 클래스 메서드는 @classmethod 밑에 cls를 받는 메서드.
        p = cls()
        print(cls.pay)
        return p
# 클래스 메서드는 클래스 속성에 접근할 수 있고, 그 안에서 인스턴스를 만들 수도 있다.
max = test2.a2(1, 2)
print(isinstance(max, test2))  # True. 이렇게 해도 인스턴스가 생성된다.

# 연습문제 날짜 클래스 만들기


class Date:
    def __init__(self):
        pass
    @staticmethod
    def is_date_valid(day):
        dat = day.split('-')
        return int(dat[1]) <13 and int(dat[2])<32
print(Date.is_date_valid('2000-10-31'))

class a2:
    def plus(self, a, b):
        return print(a+b)
man = a2()
man.plus(1, 2)

# 스태틱 메서드로 된 이유는, 클래스에서 직접 사용해서이다.
# 단순 메서드로 만들기 위해서는 인스턴스를 만들고 사용해야 한다.

# 심사문제 시간 클래스 만들기
# @staticmethod
# def is_time_valid(time):
#     hour, minute, sec = map(int, time.split(':'))
#     return hour <= 24 and minute < 60 and sec <= 60
# def from_string(self, time):
#     self.hour, self.minute, self.second = map(int, time.split(':'))
#

# class Time:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @staticmethod
#     def is_time_valid(time):
#         hour, minute, sec = map(int, time.split(':'))
#         return hour <= 24 and minute < 60 and sec <= 60
#     @classmethod
#     def from_string(cls, time):
#         hour, minute, second = map(int, time.split(':'))
#         p = cls(hour, minute, second)
#         return p
#
# time_string = input()
#
# if Time.is_time_valid(time_string):
#     t = Time.from_string(time_string)
#     print(t.hour, t.minute, t.second)
# else:
#     print('잘못된 시간 형식입니다.')




# unit 36. 클래스 상속(inheritance) 사용하기
'''
클래스 상속 : 물려받은 기능을 유지한 채로 다른 기능을 추가할 때 사용하는 기능
기반 클래스(base class) : 기능을 물려주는 클래스. 부모(parent), 슈퍼(super) 클래스라고도 불린다.
파생 클래스(derived class) : 상속을 받ㄷ아 새롭게 만드는 클래스. 자식(child), 서브(sub) 클래스
라고도 불린다.
'''

# 상속하는 법
'''
class 기반클래스이름:
    코드
    
class 상속클래스이름(기반클래스이름):
    코드
'''

class Person2:
    def greeting(self):
        print('hi')

class New_person(Person2):
    def study(self):
        print('공부하기')

james = New_person()
james.greeting()
james.study()

# 상속관계 확인하기 issubclass(파생, 기반)

# 기반 클래스의 인스턴스 속성 사용하기

# 기반 클래스를 실행하지 않는한, 기반 클래스의 인스턴스 속성은 사용되지 않는다.
# 그러므로 super().__init__() 로 기반클래스의 __init__ 메서드를 호출한다.
# >>> 상속 클래스를 호출하면 상속 클래스의 __init__ 메서드만 실행되고, 기반 클래스의 __init__은
# 실행되지 않는다. 그래서 super()의 __init__ 메서드를 __init__()을 사용해 직접 실행시켜주어서
# 기반 클래스의 __init__ 메서드를 실행시킨다. super().__init__()
# 단, 상속 클래스에 해당 속성이 있으면 기반 클래스의 속성을 사용하지 않는다.
# 그리고 상속 클래스에서 __init__을 만들지 않으면 기반 클래스의 __init__도 자동으로 상속된다.

# 오버라이딩(overriding) : 같은 이름으로 메서드를 만들었을 때, 상속 클래스를 우선하는 것.
class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        super().greeting()  # 기반 클래스의 메서드 호출하여 중복을 줄임
        # print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
        # 안녕하세요. 가 중복이므로 기반 클래스에서 greeting을 사용.
        print('저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()

# 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용한다고 한다.
# 만약 안녕하세요가 중복이 아닌 복잡한 수식 계산이 중복된다면, 또다시 복잡한 공식을 쓸 필요 없이
# super().계산메서드()를 사용하여 기반 클래스의 기능을 사용하고, 뒤에 기능을 덧붙이는 것이다.

# 다중 상속 사용하기
# class 상속클래스이름(기반1, 기반2, ...):

# 다이아몬드 상속
'''
        A
      <   >
    B       C
      >   <
        D
A > B, C
B, C > D
이렇게 되면 순서나 다른 문제가 많으므로 죽음의 다이아몬드라고 불린다.
'''

# 해결을 위해 mro(Method Resolution Order)를 따른다.
# 클래스.mro() 를 사용하면 클래스의 메서드 탐색 순서가 나오며, 그 순서대로 메서드를 찾는다.
# 1번에서 못 찾으면 2번, 3, 4, ... 로 넘어간다.

# objet클래스. 모든 클래스의 기반 클래스.
# class 클래스이름(object) 와 같음.

# 추상 메서드
'''
abc : abstract base class

from abc import *

class 추상클래스이름(metaclass=ABCMeta):
    @abstractmethod
    def 메서드이름(self):
        코드

metaclass = ABCMeta
@abstractmethod

추상클래스는 메서드 목록만 가진 클래스이다. 상속을 하면 메서드의 목록만 넘겨주고, 상속받은 클래스는
메서드의 목록에 있는 것들은 전부 구현해야 한다. 구현하지 않으면 에러가 발생한다.
구현한 여부를 확인하는 시점은 인스턴스를 만들 때이다. ex- james = student()

추상 메서드는 인스턴스로 만들 수 없다. 그래서 추상 메서드도 pass로 만든다. 인스턴스로 만들 수 없
다면 쓸 일도 없기 때문이다.
'''

# 연습문제

class AdvancedList(list):
    def replace(self, bechanged, value):
        while bechanged in self:
            self[self.index(bechanged)] = value

# 심사문제
class Animal:
    def eat(self):
        print('먹다')


class Wing:
    def flap(self):
        print('파닥거리다')


class Bird(Animal, Wing):
    def fly(self):
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))

# 오늘의 파이썬 종료.




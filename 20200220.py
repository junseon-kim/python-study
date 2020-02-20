# 2020.2.20. 오늘의 파이썬 시작.

# unit 34 클래스와 메서드 만들기
# 예전에 했지만 복습 겸 공부한다.
'''
객체(object) : 특정한 개념이나 모양으로 존재하는 것
이 객체를 만들 때 사용하는 것이 클래스이다.
체력, 마나, 물리 공격력 등의 데이터를 클래스의 속성(attribute)라 부른다.
베기, 찌르기 등의 기능을 메서드(method)라고 부른다.

이와 같은 것이 객체 지향(object oriented) 프로그래밍이라고 한다,
'''
'''
class 클래스이름(첫 글자는 대문자):
    def 메서드이름(self, ...):
        pass
메서드의 매개변수의 첫 번째는 반드시 self 이어야 한다.

클래스를 사용하려면 인스턴스를 만들어야 한다.
클래스는 설정값, 인스턴스는 클래스로 만든 객체이다.
메서드 안에서 메서드 호출시에는 self.메서드() 를 사용한다.
'''
class Person:
    def greetings(self):
        print('hello')
james = Person()
james.greetings()

# isinstance(인스턴스, 클래스) 인스턴스가 클래스의 인스턴스인지 확인한다.
print(isinstance(james, Person))

# 속성 사용하기 : 속성은 __init__ 메서드에 self.속성이름 에 값을 할당한다.
# 인스턴스를 만들 때 호출되는 특별한 메서드이다.
class aa:
    def __init__(self):
        self.health = 20
james = aa()
print(james.health)

# 앞뒤로 __ 가 붙은 메서드를 스페셜 메서드 혹은 매직 메서드라고 부른다.

# 인스턴스를 만들 때 값 받기

class ab:
    def __init__(self, age, address, name):
        self.age= age
        self.address = address
        self.name = name
    def greetings(self):
        print(f'안녕하세요, 저는 {self.name}라고 합니다. 나이는 {self.age}살이고, '
              f'사는 곳은 {self.address}입니다.')

james = ab(15, '지구', '제임스')
james.greetings()

# 속성에 접근할 때에는 인스턴스.속성이름 으로 접근.
print(james.age, james.address)

# 클래스의 위치 인수, 키워드 인수 사용하기
'''
def __init__(self, *args):
    self.name = args[0]
    self.age = args[1]
    self.address = args[2]
'''

# 딕셔너리는 **로 언패킹.

# 비공개 속성 사용하기 self.__속성이름 = 값

class ac:
    def __init__(self, money):
        self.__money = money
    def pay(self, amount):
        self.__money -= amount
        print('남은 돈은 {0}원 입니다.'.format(self.__money))
james = ac(5000)
james.pay(3000)

# 메서드도 이름은 def __메서드() 로 만들면 클래스 안에서만 호출이 가능한 비공개 메서드로 만들 수 있다.

# 연습문제

class knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def slash(self):
        print('베기')

# 심사문제
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        print('티버: 피해량 {0}'.format(self.ability_power *0.65+400))


health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
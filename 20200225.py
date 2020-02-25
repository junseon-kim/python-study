# 2020.2.25. 오늘의 파이썬 시작.

# unit 39. 반복 가능한 객체 알아보기

# iterator : 값을 차례대로 꺼낼 수 있는 객체(object)

# range는 수를 만드는 것이 아니라 수를 만들어내는 이터레이터. range(10)은 0부터 9까지의 수를 가진
# 것이 아니라 필요할 때 0부터 9까지 하나씩 만든다.

# 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용한다.
# >>> 데이터 생성을 뒤로 미룸 : 지연 평가(lazy evaluation)

# 이터레이터 = 반복자

aa = [1, 2, 3]

# dir을 사용하면 객체에 있는 메서드를 확인할 수 있다.
# 메서드에 __iter__ 가 있으면 반복가능한 객체이다.
print(dir(aa))
print(aa.__iter__())  # 이터레이터가 나온다.
# 이터레이터를 변수에 저장한 뒤 __next__()를 사용하면 순서대로 나온다.
ab = aa.__iter__()
print(ab.__next__())
print(ab.__next__())
print(ab.__next__())
try:
    print(ab.__next__())  # 이터레이터의 끝에서 한 번 더 실행하면 에러가 발생한다.
except StopIteration:
    print('예외')

# 반복가능한 객체는 __iter__ 메서드를 이용해 이터레이터를 얻고 __next__로 반복한다.
# 반복 가능한 객체(iterable) != 이터레이터 : 반복가능한 객체에서 이터레이터를 뽑아쓴다.

# 클래스에 __iter__, __next__를 모두 구현하면 이터레이터를 만들 수 있다.
# 둘 모두를 가진 객체를 이터레이터 프로토콜을 지원한다고 말한다.

# range 구현

class myrange:
    def __init__(self, stop, start=0, step=1):
        self.stop = stop
        self.start = start
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        result = self.start
        if self.start == self.stop:
            raise StopIteration
        self.start+=self.step
        return result

ac = myrange(10)
ad = ac.__iter__()
print(ac.__iter__(), '\n\n\n')

for i in myrange(10):
    print(ad.__next__())

# 이터레이터 언패킹
a, b, c = myrange(3)
print(a, b, c)

# _ 에 값 저장

a, _, c = range(3)

print(a, _, c)  # 출력은 되지만, _의 의미는 이 값은 사용하지 않곘다는 것이다.

# 인덱스로 접근 가능한 이터레이터 만들기 : __getitem__ 메서드.
class Counter:
    def __init__(self, stop):
        self.stop = stop
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

# __iter__, __next__ 없이도 __getitem__ 으로만 이터레이터 구현이 된다. 초깃값이 없다면 __init__도
# 없어도 된다고 한다.

# iter, next 함수 활용하기
# iter(객체) : 객체의 __iter__ 메서드를 호출해준다.
# next(객체) : 객체의 __next__ 메서드를 호출해준다.

af = [1, 2, 3]
ag = iter(af)
print(ag)
print(next(ag))
print(next(ag))
print(next(ag))

# iter(호출가능한 객체, 값) : 호출 가능한 객체를 호출, 실행하고 값이 나오면 멈춘다.
# 값은 sentinel이라고 부른다.
print('-----------------')
import random
ah = iter(lambda : random.randint(0, 5), 3)
# print(next(ah))
# print(next(ah))
# print(next(ah))
# print(next(ah))
# print(next(ah))
# print(next(ah))

# 혹은 for 반복문에 넣어서 이터레이터가 종료될 때까지 반복하게 할 수도 있다.
ai = iter(lambda: random.randint(1, 100), 5)
for i in ai:
    print(i, end=' ')
else:
    print()
# 반복문에 넣는 경우, StopIteration 에러는 나오지 않는다.

# for i in iter(lambda: range(5), 4):
#     print(i, end=' ')
# iter에 넣는 호출 가능한 객체의 경우, return 값이 있어야한다.

# next(이터레이터이름, 기본값) : next를 실행할 때, 끝에 가서 에러가 나지 않고 기본값이 출력된다.

aj = iter(range(3))
ak = range(3).__iter__()
print(next(aj, 10))
print(next(aj, 10))
print(next(aj, 10))
print(next(aj, 10))
print(next(aj, 10))
print(next(aj, 10))
print(next(ak, 20))
print(next(ak, 20))
print(next(ak, 20))
print(next(ak, 20))
print(next(ak, 20))
print(next(ak, 20))
print(next(ak, 20))
print(next(ak, 20))

# 연습문제 : 배수 이터레이터 만들기

class MultipleIterator:
    def __init__(self, stop, multiple):
        self.stop = stop
        self.multiple = multiple
        self.start = multiple

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            res = self.start
            self.start += self.multiple
            return res
        else:
            raise StopIteration


for i in MultipleIterator(20, 3):
    print(i, end=' ')

print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')

# 심사문제 : 시간 이터레이터 만들기

class TimeIterator:
    def __init__(self, stt, stp):
        # self.time = stt
        self.start = stt
        self.stop = stp
    # def __iter__(self):
    #     return self
    # def __next__(self):
    #     if self.time < self.stop:
    #         res = '{0:0>2}:{1:0>2}:{2:0>2}'.format(str(self.time//3600%24), str((self.time%3600)//60), str((self.time%3600)%60))
    #         self.time += 1
    #         return res
    #     else:
    #         raise StopIteration  고생이 무색하게도 이걸 지워도 실행이 아주 잘 된다.
    def __getitem__(self, index):
        if index < self.stop - self.start:
            value = index + self.start
            return '{0:0>2}:{1:0>2}:{2:0>2}'.format(str(value//3600%24), str((value%3600)//60), str((value%3600)%60))
        else:
            raise IndexError


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')

aa = iter(TimeIterator(5, 10))
print(next(aa, 15))




'''
{순서:02d} : 2글자 정수를 왼쪽을 0으로 채운다.
이터레이터 생성시, __getitme__만 써줘도 __iter__부터 __next__까지 아주 잘 된다.
'''

# 오늘의 파이썬 종료.

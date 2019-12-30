# 2019.12.30 (일) 오늘의 파이썬 시작.

# 터틀 그래픽스로 그림 그리기

import turtle as t

# t.shape('turtle')

# t.forward(100)
#
# t.right(90)

'''
앞으로 이동 : forward, fd
뒤로 이동 : backward, bk, back
왼쪽으로 회전 : left, lt
오른쪽으로 회전 : right, rt
t.mainloop() : 터틀 창이 종료될 때까지 마우스, 키보드 입력을 대기한다.
'''
#다각형 그리기

N = 6 # int(input())
# t.shape('turtle')
# t.color('red') # 색깔을 정함
# t.begin_fill() # 색칠할 영역 시작
#
# for i in range(N):
#     t.forward(1000/N)
#     t.right(360/N)
# t.end_fill() # 다각형이 끝났으면 색을 칠함. 도형이 끊어져 있더라도 자동으로 연결하여 색을 칠함.

# 원 그리기
# t.circle(120) # 반지름이 120
# 거북이가 > 방향이면 위로 원을 그린다.
# 원을 반복해서 그리기
# t.speed('fastest') # 거북이의 이동속도. 0 > 10 > 6 > 3 > 1   0이 제일 빠르다.
# 'fastest', 'fast', 'normal', 'slow', 'slowest'
# for i in range(N):
#     t.circle(120)
#     t.right(360/N)
# t.clear() # 그림 초기화
# t.speed('fastest')
# for i in range(300):
#     t.forward(i)
#     t.right(91)
# 터틀 모양(shape) : arrow, turtle, circle, square, triangle, classic
n = 6
line = 150

# for i in range(n):
#     t.forward(line)
#     t.right(720/n)
#     t.forward(line)
#     t.lt(360/n)
# t.mainloop()

# 22챕터 리스트 조작하기
'''
append : 요소 하나를 추가
extend : 리스트를 연결하여 확장
insert : 특정 인덱스에 요소 추가
'''

# append에 리스트를 넣으면 한 요소가 리스트가 되어 중첩 리스트가 된다.
a = list(range(5))
print(a)
b = list(range(70, 101, 10))
print('b', b)
a.append([789, 3282])
print(a)
a.extend(b)
print(a)

# append와 extend는 리스트를 변경할 뿐, 새 리스트를 생성하지 않는다.
c = 3456
print(c)
a.insert(2, c) # 특정 인덱스에 넣기
print(c)
a.insert(len(a), c) # 리스트 맨 끝에 넣기

# 리스트에서 요소 삭제하기
'''
pop(인덱스) : 특정 요소 또는 마지막 요소를 삭제. 인덱스를 쓰지 않아야 마지막을 삭제한다.
remove() : 특정 값을 찾아서 삭제. 여러 값이 있을 경우, 처음 찾은 값을 삭제 한다.
'''

# deque(double ended queue) 덱. 양쪽 끝에서 추가/삭제가 가능한 자료 구조.
from collections import deque # collections 패키지에서 deque 모듈을 임포트.
a = deque([10, 20, 30])
# append, appendleft
# pop, popleft
# 를 사용가능하다.

# 리스트에서 특정 값의 인덱스 구하기

a = [10, 20, 30, 15, 20, 40]
print(a.index(20)) # index(값) 값이 있는 인덱스를 반환. 여러개면 처음 찾은 것을 반환.

# 특정 값의 개수 구하기
a.count(20) # count(값) 값이 몇 개 있는지 찾는다.

# 리스트의 요소를 정렬하기 sort(), sorted()

b = sorted(a) # sorted(리스트)는 리스트를 정렬해서 반환한다. 원래의 리스트는 변하지 않는다.
print('sorted', a, b, sep='\n')
a.sort() # 리스트.sort()는 리스트를 정렬, 변경시킨다.
# sort(reverse=True)면, 큰 순서대로 정렬(내림차순)
# sort(reverse=False)면, 작은 순서대로 정렬한다.
print('sort', a, b ,sep='\n')

# 리스트 모든 요소 삭제하기
print('Before clear', a, b, sep='\n')
a.clear()
del b[:] # b리스트의 시작부터 끝까지 삭제.
print('After clear', a, b, sep='\n')

# 슬라이스로 조작하기
a = list(range(13))
print(a)
a[:5] = [0]
print(a)
a[len(a):] = [5]
print(a)
b=a
# 모든 값을 0으로 만들기
# 제일 간단한 것
def mkZero(num):
    return 0
for i in range(len(a)):
    a[i] = 0
print(a)
a=b
print(a)
a = list(map(mkZero, a))
print(a)

# 오늘의 파이썬 끝. 개인사정상 오늘은 짧게 하고 마친다. 다음은 20.8 튜플의 정보를 구하고 연산하기.
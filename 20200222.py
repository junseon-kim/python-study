# 2020.2.22. 오늘의 파이썬 시작.

# unit 37. 두 점 사이의 거리 구하기

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(20, 40)
p2 = Point(10, 70)


a = abs(p1.x-p2.x)
b = abs(p2.y - p1.y)

import math as m

distance = m.sqrt(a*a+b*b)
print(distance)
dis2 = m.sqrt(m.pow(a, 2) + m.pow(b, 2))
print(dis2)
dis3 = m.sqrt(a**2 + b**2)
print(dis3)

# namedtuple 사용하기

import collections
# 클래스이름 - collections.namedtuple('자료형이름', ['요소이름1', '요소이름2']
'''
인스턴스 = 클래스(값1, 값2)
인스턴스 = 클래스(요소이름1 = 값1, 요소이름2 = 값2)
인스턴스.요소이름1
인스턴스[인덱스]
'''

point3 = collections.namedtuple('point', ['x', 'y'])
pt1 = point3(x=10, y=20)
pt2 = point3(x=30, y=80)
dis = m.sqrt((pt1.x-pt2.x)**2 + (pt1.y - pt2.y)**2)
print(dis)

# 연습문제 사각형 넓이 구하기
# width = abs(rect.x1-rect.x2)
# height = abs(rect.y1-rect.y2)
# area = width*height

# 심사문제
# length = 0
# for i in range(3):
#     length += math.aqrt((p[i].x - p[i+1].x)**2 + (p[i].y - p[i+1].y))

import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

for i in range(3):
    length += math.sqrt((p[i].x - p[i+1].x)**2 + (p[i].y - p[i+1].y)**2)

print(length)


# 오늘의 파이썬 종료.

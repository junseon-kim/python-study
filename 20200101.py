# 오늘의 파이썬 시작.

# 2차원 리스트
a = [[1, 2], [4, 6], [7, 8]]
# 파이썬은 가로 크기가 불규칙한 톱니형 리스트(jagged list)도 만들 수 있다.
a = ((10, 20), (30, 40), (50, 60))
b = ([10, 20], [30, 40], [50, 60])
c = [(10, 20), (30, 40), (50, 60)]
# a는 변경 불가, b는 튜플 안의 리스트를 변경 가능, c는 리스트에 추가 가능
from pprint import pprint
pprint(a, indent=4, width=20)
# a를 띄어쓰기 4번, 가로 폭 20이다.

# 반복문으로 리스트 출력
for x, y in a:  # a의 요소가 2개씩이므로 2개를 받아온다.
    print(x, y)

for i in a:  # i는 a의 요소 하나를 받음
    for j in i:  # 그 요소는 리스트이므로 리스트의 요소를 한개씩 j로 넣음.
        print(j, end=' ')
    print()

# for 반복문으로 1차원 리스트 만들기
a = []
for i in range(10):
    a.append(0)
b = []
for i in range(5):
    inner = []
    for j in range(3):
        inner.append(0)
    b.append(inner)
print(b)
pprint(b, indent=0, width=10)

# list comprehension으로 2차원 리스트 만들기
c = [[i*j for j in range(3)] for i in range(6)]
print(c)

# for하나로 2차원 리스트 만들기
d = [[0]*2 for i in range(4)] # [0]*2 = [0, 0]
print(d)
e = [0]*6 # 이걸로 0으로 이루어진 리스트를 쉽게 만들 수 있다.
print(e)

# 2차원 리스트 정렬하기 sorted사용.
# sorted(반복가능한객체, key=정렬함수, reverse=True 또는 False)
students =[['john', 'C', 19], ['maria', 'A', 25], ['andrew', 'B', 7]]
print(sorted(students, key=lambda student: student[1]))
# student는 students의 요소를 말한다. lambda표현식은 나중에 배운다.
# 요소의 리스트의 1번 인덱스를 기준으로 정렬한다(A, B, C)
print(sorted(students, key=lambda student: student[2]))
# 2번 인덱스를 기준으로 정렬한다. (7, 19, 25)

# 2차원 리스트의 할당과 복사
# 2차원 리스트의 경우 copy를 사용해도 동일한 객체로 취급된다. 그래서 deepcopy를 사용한다.
import copy

st =students
stu = st.copy()
st[0][0] = 6000
print('1', st, '\n2', stu, sep=' ')
# copy는 제일 바깥의 리스트를 분리한다. 그래서 제일 바깥의 리스트를 변경하면 분리되나,
# 안의 리스트는 서로 같은 객체로 취급되기 때문에 안의 리스트를 변경하면 copy를 사용한 리스트 안의
# 리스트도 변경된다. 그래서 deepcopy를 사용한다.
# copy는 리스트.copy()로 사용하나, deepcopy는 copy.deepcopy(리스트) 로 사용한다.
qwe = copy.deepcopy(stu)
qwe[0][0] = 'dsdafsasf'
print("1", stu, '\n2', qwe, sep=' ')

# 코딩도장 심사문제 지뢰찾기
# import copy
# col, row = map(int, input().split())
# mine = []
# for i in range(row):
#     mine.append(copy.deepcopy([0]*col))
# for i in range(row):
#     temp = list(input())
#     for j in range(col):
#         if temp[j] == '*':
#             for a in [-1, 0, 1]:
#                 for b in [-1, 0, 1]:
#                     if not(a == 0 and b == 0) and 0<=i+a<=row-1 and 0<=j+b<=col-1:
#                         mine[i+a][j+b] +=1
#                     else:
#                         mine[i][j] =9
# for i in range(row):
#     for k in range(col):
#         if mine[i][k] >= 9:
#             mine[i][k] = '*'
#         else:
#             mine[i][k] = str(mine[i][k])
#     print(''.join(mine[i]))


# !!! mine을 선언할 때, 같은 객체가 됨을 무시하고 코드를 짜서 이 사단이 났다.
# mine = [[0]*col]*row를 바꾸자. copy를 이용하여 모두 다른 객체로 선언하였다.

# 24. 문자열 응용하기
# 문자열.replace('바꿀 문자열', '새 문자열') : 문자열 안의 바꿀 문자열을 새 문자열로 바꾼다.
# 단, 문자열을 바꾸지 않고 교체한 결과만 반환한다.
a = 'hi helow mama papa gogo gugu hi helow'.replace('hi', 'repaced')
print(a)
# 바꿀 문자열은 몇 개가 있든 전부 바꾼다.

# 문자 바꾸기 : 바꿀 테이블(규칙)을 만들고, tanslate(테이블)을 사용하여 변환한 결과를 반환한다.
# 테이블은 table = str.maketrans('aeiou', '12345') 와 같이, a=1 e=2 ... 식으로 바뀐다.
table = str.maketrans('aeiou', '12345')
b = a.translate(table)
print(b)
table2 = str.maketrans('aeiou', '00000')
b = a.translate(table2)
print(b)
'''
문자열.split(기준문자열) : 문자열을 리스트로, 기준문자열로 구분하여 생성.
구분문자열.join(합칠리스트) : 합칠리스트를 사이사이에 구분문자열을 넣어서 문자열 생성.
문자열.upper() : 문자열을 대문자로 변환
문자열.lower() : 문자열을 소문자로 변환
문자열.title() : 단어의 첫글자를 대문자로 변환
문자열.strip() : 문자열 양 끝의 공백 삭제, lstrip은 왼쪽, rstrip은 오른쪽.
문자열.strip(삭제할문자들) : ',.'과 같이 삭제할 문자들을 입력하면, 문자열 양쪽에서 ,와 .을 전부
                           지운다. 공백은 넣지 않았으므로 공백은 삭제되지 않음.
'''
import string
# string 모듈의 punctuation에는 모든 구두점이 들어있다고 한다.
print(string.punctuation)
# 이것을 이용하여 strip을 실행하면 손쉽게 구두점을 지울 수 있다.
a = '#$%^&*(^%$%^&*(*&^%$# I like python $%^&*(*&^%$#$%^&*'
print(a, a.strip(string.punctuation), sep='\n')

'''
문자열 정렬하기.
문자열.ljust(자연수) : 문자열을 문자열+공백의 글자수가 자연수만큼 되게 하고, 왼쪽으로 정렬한다.
문자열.ljust(자연수) : 문자열을 문자열+공백의 글자수가 자연수만큼 되게 하고, 오른쪽으로 정렬한다.
문자열.center(자연수) : 문자열을 문자열+공백의 글자수가 자연수만큼 되게 하고, 중간으로 정렬.
                       단, 공백이 홀수일 경우 왼쪽에 1칸을 더 준다.
'''
a = 'four'
print(a.ljust(10))
print(a.rjust(10))
print(a.center(10, '0')) # center(self, width, fillchar)로 돼있길래 '0'을 넣었더니
# 공백이 0 으로 바뀌었다.
# method chaining : 메서드를 계속 연결하여 사용하는 것.
print('python'.rjust(13).upper())

# 문자열 왼쪽에 0채우기 문자열.zfill(자릿수) : 자릿수가 될때까지 문자열 왼쪽에 0을 넣는다.
a = '323'
b = a.zfill(20)
print(b)

# 문자열 위치 찾기 문자열.find(찾을 문자열), rfind()
# find는 왼쪽부터, rfind는 오른쪽부터 찾는다. 최초로 찾은 문자열이 있는 인덱스를 반환하며,
# 없으면 -1을 반환한다.
# 문자열.index(찾을 문자열), rindex() 도 find와 비슷하지만, 찾는 것이 존재하지 않으면 에러가 발생.
# count

# 서식 지정자(format specifier)와 포매팅
# 서식 지정자
speci = 'I am %s' % 'james'  # %s가 서식 지정자. %로 연결해준다.
print(speci)
s = '%d %.2f %s' % (50, 2.3, 'try')
print(s) # % 로 묶으려면 ()로 묶어야 한다.
'''
길이 지정
%20d : 총 길이 20의 정수를 출력. 기본 오른쪽 정렬.
%23.5f : 총 길이 23(자릿수 5 포함)의 실수를 출력. 기본 오른쪽 정렬.
왼쪽은 길이에 -를 붙이면 된다.
'''

# format method
a = '1번 : {0} 2번 : {1} 3번: {2}'.format(123, 232.45345, 'third')
b = '1번 : {0} {2}{2}{1}2번 : {1} 3번: {2}'.format(123, 232.45345, 'third')
print(a)
print(b)
# format method는 format()안의 내용을 얼마든지 쓸 수 있다.
# 이름도 지정할 수 있다.
c = '1번 : {dec} {dec}{fl}{stir}2번 : {stir} 3번: {fl}'.format(dec=123, fl=232.45345, stir='third')
print(c)
# 변수를 사용하기 # f'내용{변수}{변수}{변수}{변수}'
sss = '이걸 넣어?'
deci = 3456
flt = 2345.23456
d = f'dsa{sss}djfs{deci}djddg{flt}jfaodk{flt}fhaji{sss}'
print(d)

# format으로 문자열 정렬하기
print('{0:<10}'.format('string'))  # < : 왼쪽, > : 오른쪽

# 개수 맞추기
print('서식 지정자는 %03d 씁니다' % 2)  # %와 d 사이에 03을 넣으면 공백을 0으로 대체하고 3자리까지 수를 만든다.
print('포맷은 {0:03d} 씁니다'.format(23))  # {} 안에 0:자릿수 를 사용하면 된다. 정수d 실수f
print("스트링은? {0:<10}::".format('abcd'))
# 형식 : 'dddsdd {인덱스:채울것<자릿수}'
a = 34
b = 6.383823
print(f'{a:|>30d}\n{b:9>30.8f}')

# 코딩도장 심사 문제
# import string
# ssss = input().split()
# cnt=0
# for i in ssss:
#     if i.strip(string.punctuation) == 'the':
#         cnt +=1
# print(cnt)

# 코딩도장 심사 문제
# import copy
# cost = list(map(str, sorted(list(map(int, input().split(';'))), reverse=True)))
# for i in cost:
#     if len(i)>6:
#         c = list(i).copy()
#         c.insert(-3, ',')
#         c.insert(-7, ',')
#         t = ''.join(c)
#         print('{0: >9}'.format(t))
#     elif len(i)>3:
#         c = list(i).copy()
#         c.insert(-3, ',')
#         t = ''.join(c)
#         print('{0: >9}'.format(t))
# format(값, 형식규칙) 이라는 함수가 있다. 형식규칙에 ','를 넣으면 천단위마다 ,를 넣는단다
N = sorted(list(map(int, input().split(';'))), reverse=True)
for i in N:
    print('{0: >9,}'.format(i))
    print('%9s' % format(i, ','))
# 51900;83000;158000;367500;250000;59200;128500;1304000

# 오늘의 파이썬 종료. 다음은 25장
# 2019.12.23. (월) 오늘의 시작은 조건문이다. C 에서 이미 배웠으므로 형태만 보도록 하자.
# 파이썬은 조건문으로 if, else, elif를 사용한다.
'''
print("what is your age?")
age = int(input())
if (age < 20) :
    print("you are down twenty!")
else :
    print("over twenty!")
'''
'''
    if (조건) : 콜론이 중요하다.
        실행할 것
    elif (조건) :
        실행할 것
    else :
        실행할 것
'''
# 파이썬의 조건문은, 같은 if문일 경우 들여쓰기로 if문을 구분한다. 수행할 block은 들여쓰기가 같아야 한다. 콜론(:)이 매우 중요.
# x == y 는 x is y 와 같고, x != y 는 x is not y 와 같다. 다른 것은 C와 같다.
x = 1
y = 1
# x is y 는 메모리의 주소가 같은지 판단하는 것.
if (x is y) :
    print(1,x,y)
if (x==y) :
    print(2,x,y)

# and or not 은 문자 그대로 사용한다.
if (x and y) :
    print(3)
elif (x or y) :
    print(4)
    x=0
elif (not x) :
    print(5)
elif not(x) :
    print(6)

print('당신의 점수를 입력하세요. :')
#score = int(input())
score = 1
if (score >= 90) :
    grade = 'A'
elif (score >= 80) :
    grade = 'B'
elif (score >= 70) :
    grade = 'C'
elif (score >= 60) :
    grade = 'D'
else :
    grade = 'F'
print('당신의 학점은',grade,'입니다')

# 정리 : 파이썬의 조건문은 if, elif, else로 이루어지며, 콜론(:)으로 실행을 하며, 구분은 들여쓰기로 한다.

# 2019.12.23 반복문
# 파이썬은 for, while 문을 사용. 반복 구문은 들여쓰기와 block으로 구분함. 반복 시작 조건, 종료 조건, 수행 명령으로 구분.
# if문과 똑같이 콜론(:)으로 시작한다.
for looper in [1,2,3,4,5]:# looper 변수에 리스트의 변수 할당. 명령 수행.
    print("hello")
for looper in [1,2,3,4,5]:
    print(looper)

# 많은 반복을 위해 range(x,y) 를 사용한다. x 부터 y개 를 사용한다.
for i in range(0,10):
    print('range :',i)
for i in 'abcdefgh':
    print(i)
# 문자열을 넣어서 한 글자씩 출력하게 할 수도 있고, 리스트에 문자열을 넣어서 문자열을 출력하게 할 수로 있다.
# range 는 range(1, 10, 2) 의 의미는 1부터 10개 범위인데, 2개 단위로 뛰어서 출력한다. 1> 3 > 5 > 7
# range 는 정수만 취급한다.
for i in range(1, 9, 2) :
    print(i)

# range 의 연산 결과, 앞의 두개의 숫자 범위에 연산 결과가 없으면, 출력하지 않는다.

# while
print('while')
i = 1
while (i< 10) :
    print(i)
    i += 1
# for 와 while은 서로 변환 가능하나, for는 반복 횟수를 확실히 알 때. while문은 확실히 모를 때 사용.
# 제어문 break, continue
print("제어문")
for i in range(1,20,1):
    if (i==7) : break
    print(i)
print("continue")
for i in range(1,20,1):
    if (i%2 == 1) : continue
    print(i)
# else 가 반복문에 들어갈 수 있다. else는 반복문 종료시, 혹은 조건이 맞지 않을 때 사용.
for i in range(1, 5, -1) :
    print(i)
else:
    print("EOP")
i = 1
while(i<=5) :
    print(i)
    i+=1
else : print("EOP")

# 구구단 계산기 만들기.
'''
print("구구단 몇 단을 계산할까요?")
dan = int(input())
for i in range(1,10,1) :
    print(dan, "*", i, '=', i*dan)

'''
for i in range(5, 8, 1) : #range(start, stop, step) 으로 구성. stop을 만나면 멈추는 것으로??
    # range(x, y, z) 의 범위는 i 가 씩 더해지고, 범위는 x <= i < y 이다. x 부터 시작해서, y보다 1 작을때까지 스텝을 반복.
    print(i)

a = 10
b = 15
print('a는'+str(a)+'b는'+str(b)) # print문에서 구분은 쉼표(,) 혹은 플러스(+)로 한다. +로 구분하는 것은 띄어쓰기 없이 문자열만
# 가능하고, 쉼표로 구분하는 것은 띄어쓰기가 자동으로 된다.
'''
print("구구단 몇 단을 계산할까요?")
dan = int(input())
print("구구단"+ str( dan ) +"단을 계산합니다") # 띄어쓰기 가 있어도 띄우지 않음.
for i in range(1,10) : # 1 부터 10보다 작은 값까지. 10, 1 이면 10부터 1보다 큰 값까지.
    print(dan, "*", i, '=', i*dan)
'''
# 반대로 출력하는 프로그램
'''
print("반대로 출력할 것을 입력 :")
stri = input()
rev_sentense = ""
for i in stri :
    rev_sentense =  i + rev_sentense # rev_sentense를 기준으로 i + rev 면 rev 왼쪽에 붙이므로 거꾸로. rev + i 면
    # rev 오른쪽에 붙이므로 정방향으로 대입한다.
print(rev_sentense)
'''

'''
# 이진수 구하기
print("이진수로 바꿀 숫자를 입력하세요")
decimal = int(input())
binary = ""
while(decimal != 0) :
    binary = str(decimal % 2) + binary
    decimal //= 2
    # decimal = int(decimal /2)
else : print(binary)
'''
'''
# 숫자 찾기 게임
import random # random 호출
rint = random.randint(1, 100) # 1부터 100까지의 범위에서 난수 생성.
print("숫자 찾기 게임입니다. 1~100까지의 숫자를 찾아보세요.")
cnt = 0
anw = 0
while (anw != rint):
    cnt += 1
    print('답을 입력하세요.')
    anw = int(input())
    if (anw > rint) :
        print('DOWN')
    elif (anw < rint) :
        print('UP')
else :
    print(str(cnt)+'회만에 찾기 성공! 축하드립니다!')# +가 구분이 아니라 그저 문자열을 더한 것 이었다.
# is not 은 메모리 주소를 비교, !=는 값을 비교하는데, 파이썬은 1~256을 할당 시에는 같은 숫자는 같은 메모리 주소를 사용하기 때문에
# 파이썬에서는 1~256에서는 is not을 사용해도 된다.
'''
# 구구단 프로그램 1~9, 0입력 시 종료, 그 외에는 잘못 입력.
print("구구단 출력 프로그램 입니다. 1~9까지, 0은 종료입니다.")
cal = 1
while (cal) :
    print("계산할 구구단을 입력하세요.(1~9) :")
    cal = int(input())
    if (cal == 0) : continue
    elif(cal> 9 or cal < 0):
        print('잘못된 입력입니다.')
        continue
    print("구구단 "+str(cal)+'단은')
    for i in range(1,10) :
        print(cal,"*",i,'=',cal*i)
    print('입니다.')
else : print('프로그램을 종료합니다.')

# 2019.12.23 오늘의 python 종료. 다음은 how to debug 부터.

#2019.12.22 기본자료형과 연산

a = 1
b = 2
c = a+b
print(c, a)

a = True
b = False
print(a,b)
# 주석 처리는 #(한 줄), '''내용''' ('''안에 들어온 내용 모두 주석처리. 2줄 이상 가능하다.)
#파이썬에는 세미콜론이 필요없다고 한다. 그저 한 줄에 구문이 많을 때 그것들을 구분해준다고 한다.

a = 1.3
b = 4.5
print(a+b,'\n' )
print('\\n은 어떻게 쓰나??')
# print 에서는 ,로 사용하는 변수를 구분하는 것 같다.

a = 'abc'
b = "def"
print(a, b)

a= 1.3
b = 2
print(a+b)
#자동으로 형변환이 된다.


#연산자는 + - * / % 등이 있다.

print('더하기 : ',3+5)
print('빼기 : ',3-5)
print('곱하기 : ',3*5)
print('나누기 : ',10/5)
print('나머지 : ',6%5)
a=1
print(a)
a+=1
print(a)
a+=3
print(a)

#2019.12.22 형변환

a= 10
print(a)
a = float(a)
print(a)
#컴퓨터는 10 과 10.0 을 비교하면 같다고 출력한다. 왜냐하면 파이썬은 둘이 형변환을 하고 비교를 하기 때문.
b= 5
print(a/b)
print(int(a/b))
a = 10.3
b = 10.7
print(a+b)
a = int(a)
b = int(b)
print(a+b)
a = 34.3
b = '34.3'
print(a)
print(b)
print(a+float(b))
a = 'Hello'
b = ' World!'
print(a + b)
# 문자열을 더하면 문자열이 이어진다.
# int() 과 float()은 문자열을 숫자열로, 서로를 서로로 바꿀 수 있다.
# str()은 숫자열을 문자열로 바꿀 수 있다.
a= '53.2'
print(a)
a = float(a)
print(a)
# 문자열이 숫자로만 이뤄져 있다면, 숫자형으로 바꿀 수 있다.

#a = 'as52ds561 sda'
#print(float(a))# 문자열에 숫자가 아닌 것이 하나라도 섞이면, 변환 불가
# 에러가 났다면, 그 에러 이후로는 코드 실행이 안된다.

a = int(10.3)
b = float(10.30)
c = str(10.3)
print(a)
print(b)
print(c)
# 자료형을 알고 싶다면, type()을 사용하면 된다.
print(type(a),type(b),type(c))

# 2019.12.22 콘솔 다루기??

# print는 값을 출력, input은 값을 받는다.
print('Enter your name')
'''
name = input()
print('Hi', name)
'''
print('온도를 입력하세요. : ')
#temperature = float(input())
'''입력받고 바로 형변환을 할 수 있다. 아니, 해야한다. 왜냐하면 input()함수는 받은 것은 문자열로 취급하기 때문이다.
반드시 사용할 자료형으로 만들자.'''

#print(temperature)

''' 
결론 : print는 값을 출력, ',' 로 값을 구분. 문자열은 '로 출력.
input()은 받은 값을 문자열로 인식하여 반환. 받을 변수에 할당해주자.

'''
# 2019.12.22 화씨 = (섭씨 * 1.8) + 32
print('화씨로 변환하고 싶은 섭씨 온도를 입력해주세요.')
'''
dgreecelcious = float(input())
fah = (9/5) * dgreecelcious + 32
print("섭씨온도 :", dgreecelcious)
print("화씨온도 :", fah)'''
# 32.2를 넣으면 89.96000000000001 이라고 나온다. 이것은 이진수 소주점의 문제라고 한다.

# 2019.12.22 List data type : 배열, array

# 만약 내가 100명의 성적을 처리해야 한다면, >> 리스트
'''
 - 시퀀스 자료형, 여러 데이터들의 집합.
 - int, float 같은 다양한 데이터를 같이 넣을 수 있다.
'''

colors = ['red', 'blue', 'green']
# index : list에 있는 값들은 주소(offset)를 가진다. 그것을 호출.
print(colors[0])
print(colors[2])
# len()은 list의 길이를 반환.
print(len(colors))

# slicing 슬라이싱. list의 값들을 잘라서 쓰는 것이 슬라이싱. colors[0 : 6]
# list의 주소값을 기반으로 부분값을 반환. index는 0부터 사용.
alphabet = ['a','b','c','d','e','f','g','h'] # 8개이므로 0 ~ 7.
print(alphabet[0:5]) # 0부터 5까지 출력 (6개)
print(alphabet[-3:])# 변수에 -가 붙으면 끝에서 9번째부터 끝까지이다. : 뒤에 아무것도 없으면 끝까지라는 뜻.
# 단, 맨 끝이 -1이다.
print(alphabet[-50:50]) # 범위를 넘어가면 자동으로 최대 범위 지정.
print(alphabet[:])# 처음부터 끝까지
print(alphabet[::2])# 2칸 단위로 슬라이싱
print(alphabet[::3]) # 3칸
print(alphabet[::-1]) # 역으로 슬라이싱. 끝에서부터 처음까지 전부다. 그럼 끝에서부터 2칸은?
print(alphabet[::-2]) # is this? 맞다. 이거다 ㅇㄴㅇㅁㅁㅇㅈㅇㅁㅇㅁ
print(alphabet[-5:-3]) # 3개를 예상했으나 -3 전까지만 출력한다.
print('------------------------------------------')
# list의 연산.

c = ['a', 'b', 'c']
c2 = ['d','e','f']
print(c+c2)
print(c,len(c+c2)) #합친 것의 길이도 가능하다.
c[0] = 'A'
print(c*2) # 문자열 c 를 2번 출력.
'e' in c2 # e가 c2문자열에 있는지 확인. 있으면 True, 없으면 False.
print('e' in c2)
total_c = c+c2
print('-----------------------------')
# list 의 추거와 삭제 append, extend, insert, remove, del 등 배열이름.함수(내용)
cl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j']
print(cl)
cl.append('k') # 하나의 자료를 추가
print(cl)
cl.extend(['l','m','n']) # 리스트에 새로운 리스트 추가.
print(cl)
cl.insert(1,'A') # n번째 주소에 A 추가. n번째를 바꾸는 게 아니라 n번째 부터 뒤로 밀고 그 자리에 넣는다.
print(cl)
cl.remove('b') # b가 있으면 b를 제거.
print(cl)
del cl[0] # 0번째 주소에 있는 값을 제거
print(cl)

print(3/5)
print(3//5) # 몫만 출력됨.

# 다양한 type이 하나의 리스트에 들어갈 수 있음.
print('------------------')
a= ["cl", 1, 3.4, 12321] # 문자열, 정수, 실수
cl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j']

print(a)
a[3] = cl # 리스트 안에 리스트 넣기.
print(a)

# 리스트 메모리 방식
print('-----------------------')
a = [5, 4, 3, 2, 1]
b = [1, 2, 3, 4, 5]
print(a+b)
b=a
print(a,'\n',b)
print(b)
a.sort() # a에 새로운 것을 넣은 것이 아니라 a를 바꾸는 것이므로 주소값이 바뀌지 않음.
print('after sort a :',b) # 배열의 할당은 주소값을 할당하는 것.할당한 것을 바꾸면 할당된 것도 바뀐다.
a = [2, 3, 4, 5, 6] # a에 새로운 것을 넣어서 a=b의 관계를 해제.
print(a,b)
b = [6, 7, 8, 9, 10]
print(a, b)

# packing and unpacking
print('packing and unpacking')
t = [1, 2, 3]
a, b, c =t # t의 처음부터 a, b, c에 집어넣음. 그러나 언팩할 변수의 개수가 전체 개수와 맞지 않으면 언팩 불가.
print(t, a, b, c)

# 2차원 리스트
print('2차원 리스트')
ksc = [49, 79, 20, 100, 80]
msc = [10, 20, 30, 40, 50]
esc = [67, 34, 30, 60, 98]
midterm = [ksc, msc, esc]

print(midterm)
print(midterm[0][2])

# 가천대 학생은 아니지만 해보는 Assignment. 학점 계산기. 는 반복문과 함수를 못배웠기 때문에 불가.

# 2019.12.22(일) 오늘은 Team Lab의 강좌 List Data Type 까지 배웠다.







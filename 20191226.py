# 2019.12.26.(목) 오늘의 파이썬 시작.
# 자료구조 개요 - 이 유튜브 동영상에서는 간단히 설명만 한다. 따로 배울 것.

# 특징이 있는 자료는 어떻게 저장하면 좋을까?
'''
 - 스택과 큐(stack and Queue)
 - 튜플과 집합
 - 딕셔너리
'''

# stack : 나중에 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조 LIFO(Last In First Out)
# 입력 : Push, 출력 : Pop

# push -> append, pop -> pop

a = [1, 2, 3, 4, 5]
a.append(10)
a.append(20)
print(a)
print(a.pop())
print(a)
for i in range(0, len(a)):
    print(a.pop()) # pop() : pop(0) -> 0번째 인덱스의 값을 빼옴

# 입력된 글자를 역순으로 출력

inputstr = list("abcdefghijk")  # list()는 한 글자씩 하나의 리스트로 넣는다.
print(inputstr)

for i in range(len(inputstr)):
    print(inputstr.pop()) # list() 는 자료형을 리스트로 변환.

# Queue : FIFO(First In First Out)
# Push : append
# Pop : 뽑을자료.pop(0)

# Tuple & Set

# Tuple : 값의 변경이 불가능한 리스트 선언시 []가 아닌 ()을 사용.
# 튜플은 리스트의 연산, 인덱싱, 슬라이싱 등을 동일하게 사용.

t = (1, 2, 3)
print(t + t, t*2)
t = (1) # 이것은 int형이다. (,)를 찍어야 튜플이 된다.
print(type(t))
t = (1,)
print(type(t))

# Set : 집합과 비슷한 개념. 값을 순서없이 저장하나, 중복이 불가능하다.
# Set 객체 선언을 이용하여 객체 생성. set(리스트 혹은 문자열?)
print('Set')
s = {1, 2, 3, 4, 5} #set() 혹은  {} 을 사용하면 set으로 된다.
print(s)
s.add(6) # set 객체에 자료를 추가 add(추가할 자료)
print('Add 6', s)
s.remove(1)# set 객체에서 자료를 제거 remove(제거할 자료)
print('remove 1', s)
s.update([10, 20, 30, 40, 50, 60])# set 에 자료를 대량으로 추가. 그러나 순서는 섞임. 반 잘라서 각 1, 2, 3 씩 넣음.
print('update', s)
s.discard(3) # remove와 같이 특정 자료를 제거
print('discard 3', s)
s.clear() # set객체를 지움

print('집합 연산')
print(''' union : 합집합 ( | )
 intersection : 교집합 ( & )
 difference : 차집합 ( - )''')

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9, 10])
s3 =s1.union(s2) # s1과 s2의 합집합.
print(s3)
s4 = s1 | s2 # |이 합집합 연산이다.
print(s4)
s5 = s1.intersection(s2) # s1과 s2의 교집합.
print(s5)
s6 = s1 & s2 # &가 교집합 연산.
print(s6)
s7 = s1.difference(s2) # s1과 s2의 차집합.
print(s7)
s8 = s1 - s2 # 빼기하면 차집합이다.
print(s8)

print('Dictionary')
# Dictionary
'''
 - 구분지을 수 있는 값을 함께 저장.
 - 구분을 위한 데이터를 Identifier 또는 Key Value 라고 한다
 - dict 타입이라고 한다. (Hash Table)
'''
stinfo = {1001: "junseon", 1002: "qunseon", 1003: "wunseon"}
stinfo[1004] = "eunseon" # 키 값은 자료형을 구분한다.
stinfo['1004'] = 'runseon'
print(stinfo)
print(stinfo[1003])
print(stinfo.items()) # 키 값과 그에 해당하는 자료를 출력
print(stinfo.keys()) # 키 값만 출력.
print(stinfo.values()) # 밸류만 출력.
print('\n', stinfo)
print("qunseon" in stinfo)
print('qunseon' in stinfo.keys())
print('qunseon' in stinfo.values())
print('qunseon' in stinfo.items()) # 결과로 보아 자료의 값은 in Dict.values()로만 찾을 수 있다.
print('keys')
print(1003 in stinfo) # 기본적으로 키 값만 찾는다.
print(1003 in stinfo.keys())
print(1003 in stinfo.values())
print(1003 in stinfo.items()) # 키 값을 못 찾는다. 혹시? 아니다. items로는 못찾는다.

# 당분간 coding dojang으로 파이썬을 공부한다. team lab은 너무 축약하는 것 같다.

# 다수의 변수 선언하기
print("코딩 도장")

x, y, z = 10, 20, 30
print(x, y, z)
# x, y, z = 10 할당할 것과 개수가 맞아야 한다. 다음의 것이 맞다.
x = y = z = 10
print(x, y, z)
x, y, z = 10, 200, 3000
print(x, y, z)
x, y, z = z, x, y # 3개 변수의 값을 바꾼다.
print(x, y, z)
# 빈 변수 None 반드시 'None' 이라고 적어야 한다. Nonetype이라고 따로 있다.
k = None
print('k', k)
k = 5
print(k)
k = -1234
print(+k) # +를 붙이면 그대로 나온다.
print(-k) # -를 붙이면 -를 곱해서 나온다. 음수 -> 양수, 양수 -> 음수

#값을 입력받기
# num1, num2 = input().split(',') # input().split(기준 문자열)
# print(num1 + num2)
# num1, num2 = map(int, input().split()) # int(input().split()) 이 먹히지 않는다. map을 사용하면 된다고 한다.
# print(num1 + num2)

# 값 출력시(print) 공백 대신 출력하기 sep(seperate)
print('Hello', 'World!')
print('Hello', 'World!', sep='') # 빈 문자열을 넣으면, 공백을 대체하므로 공백이 사라진다.
print('Hello', 'World!', sep='X') # 다른 문자열을 넣을 수도 있다.
print('Hello', 'World!', sep='\n') # \n 을 넣어 줄바꿈을 할 수도 있다.

# 값 출력시 end
print('Hey', end='') # 끝날 때 빈 문자열이기 때문에 줄바꿈을 하지 않는다.
print('World!')
print('Hey', end=' ') # 끝날 때 공백. 띄어쓰기.
print('World!')
print('Hey', 'World!', end='ended!') # 끝날 때 출력되기 때문에 띄어쓰기가 되지 않을 것이다. 맞다.

# 2019.12.26 오늘의 파이썬 종료.
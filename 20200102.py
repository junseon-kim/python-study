# 2020.01.02 (목) 오늘의 파이썬은 그동안의 복습이다. 오늘은 복습으로 간단하게 훑고 장고를 하기로 했다.
# 자료형
a = True  # boolean
b = 'string'
c = 10
d = 10.2
e = [True, 'string', 10, 10.2, ['kfd']]
f = tuple()
g = dict()
'''
range
for
if elif else
h = [i for i in range(10) if i%2==0] >>>> for에서 뽑아낸 것이 조건에 맞으면 리스트로 만든다.
'''


k = 'anskd'
print('{0} {1}'.format(50, k))
print(f"이것도 문자열{'-안에 있는 것이 그대로 들어간다.-'} 이다 {k}")
print('%s %d %f' % ('문자열', 10, 32.2))

def add(x, y):
    return x+y
def addone(r):
    r.append(1)
t = [30, 20, 10]
addone(t)
print(t)

'''
tuple
set
stack
queue
deque
dict - items keys values

'''
a = [1] * 10
print(a)
a[0] = 2
print(a)

# 여기에 적진 않았지만 그동안 해온 py파일들을 훑었다. 오늘의 파이썬 종료. 장고를 하러 가자.
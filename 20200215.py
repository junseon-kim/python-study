# 2020.2.15. 오늘의 파이썬 시작!

# unit 30. 함수에서 위치 인수와 키워드 인수 사용하기

# 위치 인수(positional argument) : print(10, 20, 30)

def print_num(a, b, c):
    print(a)
    print(b)
    print(c)
print_num(10, 20, 30)

# 언패킹 하는 법 : 함수(*리스트 혹은 *튜플) *(애스터리스크)
x = [10, 20, 30]
print_num(*x)
# 이 때에는 리스트 요소 개수와 매개변수의 개수가 같아야 한다.

# 가변 인수 함수 :
'''
def 함수이름(*매개변수):
    pass
'''
def print_num2(*args):
    for arg in args:
        print(arg)
aa = list(range(20))
print_num2(*aa)
# 고정 인수와 가변 인수 동시에 사용하기 : def 함수이름(매개변수1, 매개변수2, *매개변수):

# 키워드 인수 : 순서에 상관없이 인수를 넣는다.
# print_num(name = 'dsad', address= 'dsadsa', age='25')
# sep, end 도 키워드 인수라고 한다.

# 키워드 인수와 딕셔너리 언패킹 : 딕셔너리를 언패킹할 때는 애스터리스크를 2개 붙여준다.
def personal_info(name, age, address):
    print('이름 :', name)
    print('나이 :', age)
    print('주소 :', address)

ab = {'name': '김준선', 'address': '일도 이시 삼동', 'age': 345}
personal_info(**ab)

# 딕셔너리 언패킹을 사용할 때에는 매개변수의 이름과 딕셔너리의 키의 이름이 같아야 한다.
# 딕셔너리 언패킹을 할 때, *를 한 번 사용하면 키를 불러오고, *를 두 번 사용하면 키와 값을 사용한다.

# 키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ':', arg)
ac = {'name': '김준선2', 'address': '서울시 용산구', 'age': 3456, 'job': 'police'}
personal_info(**ac)
# 보통 if 'name' in kwargs: 와 같이 해당 키의 존재 여부를 따진 후 실행하도록 한다고 한다.

# 매개변수의 초깃값 정하기 : 그저 함수 선언시 매개변수에 값을 넣으면 된다.
def just_func(name, age, address="비공개"):
    print(name)
    print(age)
    print(address)

# 초깃값을 넣은 매개변수는 순서가 가장 뒤로 가야한다.

# 연습문제 가장 높은 점수가 출력되게 하라.

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)
# max(객체) :
max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

# 심사문제 : 가장 높은, 낮은 점수, 평균 점수 출력

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    return sum(kwargs.values())/len(kwargs)



min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

# 오늘의 파이썬 종료!
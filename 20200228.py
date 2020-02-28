# 2020.2.28. 오늘의 파이썬 시작.

# unit 41. 코루틴에 값 보내기

# 코루틴(coroutine, cooperative routine) : 종속이 아닌 대등한 관계로, 특정 시점에 상대방의 코드를
# 실행한다. 메인 > 코루틴 > 메인 > 코루틴 > ...
# 진입점(entry point) : 함수의 코드를 실행하는 지점

# 코루틴은 제너레이터의 특별한 형탸. 코루틴은 yield로 값을 받아온다.
# 코루틴에 값을 보내면서 코드를 실행할 때는 send 메서드를 사용. send로 보낸 값을 반으려면 (yield)

def num_cor():
    while True:
        x = (yield)
        print(x, '1')


aa = num_cor()
next(aa)  # 코루틴의 yield까지 코드를 실행.
aa.send(1)
aa.send(2)
aa.send(3)
# 다음 (yield)를 만나면 코루틴은 send 로 받을 값을 기다린다.
# 코루틴객체.send(None) 를 사용해도 코루틴의 코드를 최초실행할 수 있다.

def sum_cor():
    total = 0
    while True:
        x = (yield total)
        total += x
co = sum_cor()
print(co.send(None))
print(co.send(1))
print(co.send(4))
print(co.send(8))
print(co.send(10))
# 변수1 = (yield 변수2) 함수 밖에서 send로 값을 전달하면, 변수2를 반환해주고 값을 변수1에 받아온다.
# next는 코드를 실행하지만 값은 보내지 않고, send는 값도 보내고 코드도 실행한다.

# 보통 코루틴은 실행 상태 유지를 위하여 무한 루프로 만든다. 강제 종료를 하려면 객체.close()를 사용.
# 코루틴을 종료하면 코루틴 함수 안에서 GeneratorExit 예외가 발생한다.
def numb_cor():
    # try:
    while True:
        x = (yield)
        print(x, end=' ')
    # except GeneratorExit:
    #     pass
co = numb_cor()
co.__next__()
for i in range(20):
    co.send(i)
co.close()
print('ddddd')

# 코루틴 안에서 예외 발생시키기 : 코루틴객체.throw(예외이름, '에러메시지')

def sum_cr():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print('예외 발생', e)
        yield total
co = sum_cr()
next(co)
for i in range(11):
    co.send(i)
print(co.throw(RuntimeError, '런타임 에러 발생'))
'''
print()실행. -> co.throw 실행. -> 코루틴 실행 -> 코루틴에서 예외 발생 -> 코루틴의 print()실행.
-> yield total로 코루틴 밖으로 값 전달. -> co.throw의 반환값으로 yield된 total을 받음.
-> total 을 print()로 출력.
'''

# 코루틴으로 하위 코루틴에 값 보내기
# 변수 = yield from 코루틴()
def accumulate():
    total = 0
    while True:
        x = (yield)
        if x == None:
            return total
        total += x


def sum_coro():
    while True:
        x = yield from accumulate()
        print(x)
print('----------------')
co = sum_coro()
next(co)
for i in range(1, 11):
    co.send(i)
# co.send(None)
next(co)

'''
next(co)로 코루틴 최초 실행. -> yield from을 만남. -> 상위 코루틴(sum_coro)를 일단 멈추고, 받은
값을 하위 코루틴(accumulate)에 전달. -> 하위 코루틴에서 return을 만날 때까지 상위 코루틴에서 받은
값은 하위 코루틴으로 전달되고, 연산이 된다. -> next(co)를 통해 상위 코루틴에 None을 보냄.
-> return을 아직 못 만났으므로 하위 코루틴으로 None을 전달. -> if문에 의해 return total을 만남.
-> 하위 코루틴에서 total을 반환. -> yield from에서 total을 받아 x에 할당. -> x를 출력.
'''
# 파이썬 3.6 이하에서는 return 대신 raise StopIteration(반환값) 으로도 사용했으나
# 파이썬 3.7 이상에서는 RuntimeError로 바뀌므로 쓰지 못한다.
# 하위 코루틴에서 변수 = (yield 변수2)를 사용했다면, 상위 코루틴에서 yield from 을 거쳐서 밖으로
# 값을 반환한다. send와 똑같이 값을 주고 받을 수 있다. 전역 -> 상위 -> 하위, 하위 -> 상위 -> 전역

# 연습문제
def find(line):
    result = 0
    while True:
        x = (yield result)
        result += 1


f = find('Python')
next(f)  # 최초실행. yield result를 사용. : 값을 받고, 코드를 전부 실행 후 다시 yield result로
# 되돌아와 값을 "반환" 후 다시 값을 받기 위해 대기.
print(f.send('Hello, Python!'))  # send로 값을 전달. 대기중이던 코루틴은 값을 받고 코드를 실행
# 후 while 한 바퀴 돌아 yield result를 만나 값을 반환 후 대기.

print(f.send('Hello, world!'))  # 또다시 send로 전달, 코드 실행, 한 바퀴 돌고 yield result를
# 만나 값을 반환.
print(f.send('Python Script'))

f.close()

''' 코루틴 :
최초실행 -> 루프 한 바퀴 돌아 yield 만남. -> 값을 받기 위해 대기 -> send로 바깥에서 값을 전달
-> 값을 받아 연산을 하고, 루프를 한 바퀴 돌아 yield를 만나면 값을 "반환" -> 값을 전달 받기 위해
대기
'''

# 심사문제 : 사칙연산 코루틴 만들기

def calc():
    result = 0
    while True:
        line = (yield result)
        num1, oper, num2 = line.split()
        if oper == '+':
            result = int(num1)+int(num2)
        if oper == '-':
            result = int(num1)-int(num2)
        if oper == '*':
            result = int(num1)*int(num2)
        if oper == '/':
            result = int(num1)/int(num2)

expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))
c.close()
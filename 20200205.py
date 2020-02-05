# 2020.2.5. 수요일 오늘의 파이썬 시작!

# unit 26 세트 사용하기

'''
세트는 중괄호로 값을 저장하며, 콤마로 구분한다.
세트를 출력해보면 매번 요소의 순서가 다르게 나온다.
세트에 들어가는 요소는 중복될 수 없다.
세트는 대괄호를 사용하여 특정 요소를 출력할 수 없다.

'''

aa = {1, 2, 3, 4, 5, 6, 7, 8, 8, 9}
print(aa)

print(2 in aa, 10 in aa)
print(2 not in aa, 1231532 not in aa)

# 반복가능한 객체를 세트로 만들기 : set()

ab = set('apple')
print(ab)
# 비어있는 세트를 만들려면 x = set()를 사용하자. {}를 사용하는 것은 딕셔너리다.
ac = set()
print(ac)

# 세트에는 세트를 넣을 수 없다.
# frozenset라는 것이 있다. 변경할 수 없는 집합이고, 이것은 중복이 가능하다.

# 세트의 연산.

ad = {1, 2, 3, 4}
ae = {3, 4, 5, 6}
# 합집합 |, .union(집합1, 집합2)

print(ad | ae, set.union(ad, ae))

# 교집합 &, set.intersection(집합1, 집합2)

print(ad & ae, set.intersection(ae, ad))

# 차집합 -,difference(집합1, 집합1에서 뺄 집합)

print(ad - ae, set.difference(ad, ae))

# 대칭자집합(XOR) ^, symmetric_difference : XOR는 서로 다르면 참이므로 겹치지 않는 것을 구한다.

print(ad ^ ae, set.symmetric_difference(ad, ae))

# 집합 연산 후 할당 연산자.

# |=는 or 후 할당한다. update와 같다.
af = {1, 2, 3, 4}
print(af)
af |= {5}
print(af)
af.update({6})
print(af)

# &= 는 and 후 할당. intersection_update()와 같다.

af &= {0, 1, 2, 3, 4, 54431}
print(af)
af.intersection_update({-1, 0, 1, 2})
print(af)

ag = {1, 2, 3, 4, 5, 6}

# -=는 차집합한다. .difference_update와 같다.
ag -= {1}
print(ag)
ag.difference({3, 5})
print(ag)

# ^=는 XOR후 할당. symmetric_difference_update와 같다.
ah = {1, 2, 3, 4, 5}
ai = {3, 4, 5, 6, 7, 8}
ah ^= ai
print(ah)
ah = {1, 2, 3, 4, 5}
ah.symmetric_difference_update(ai)
print(ah)

# 부분집합, 상위집합 확인하기
'''
현재 세트 <= 다른 세트  ==> 현재 세트가 다른 세트의 부분집합인지 확인한다. issubset
현재 세트 < 다른 세트  ==> 현재 세트가 다른 세트의 진부분집합인지 확인한다.
현재 세트 >= 다른 세트  ==> 현재 세트가 다른 세트의 상위 집합인지 확인한다. issuperset
현재 세트 > 다른 세트  ==> 현재 세트가 다른 셑의 진상위 집합인지 확인한다.
'''

# 세트 조작하기

# .add() 세트에 추가
print(ai)
ai.add(11)
print(ai)

# .remove() 세트에서 삭제
ai.remove(11)
print(ai)
# 없는 것을 지우려 하면 오류가 발생 이 때문에 discard를 사용.

# .discard()
ai.discard(11)
print(ai)

# .pop() 임의의 요소 삭제
print(ai.pop())
print(ai)
print(ai.pop())
print(ai)
print(ai.pop())
print(ai)
# 비어있는 세트에 사용하면 오류가 난다.

# .clear() 를 사용하면 모두 삭제된다.
ai.clear()
print(ai)

# len(집합) 을 사용하면 길이를 구한다.

print(len(ai))

# 세트도 똑같이 그저 할당을 하면, 2개의 객체가 아니다. 그러므로 .copy()를 사용한다.

aj = {1, 2, 3}
ak = aj
print(aj is ak, aj == ak)
ak = aj.copy()
print(aj is ak, ak == aj)

# for문으로 반복가능한 객체를 넣는 것처럼 가능하다.
for i in aj:
    print(i)
# 숫자로 된 세트는 순서대로 출력한다.
for i in {'a', 'b', 'c', 'd'}:
    print(i)

# 세트 표현식 사용하기 : 리스트나 딕셔너리와 비슷하다.
am = {i for i in 'apple' if i != 'a'}
print(am)

# 세트가 같은지 다른지 확인하기 ==, !=
an = {1, 2, 3}
ao = {1, 2, 3}
print(an == ao, an != ao)
ap = {4, 5, 6}

# 세트가 겹치는지 확인하기 a.isdisjoint(b)
print(ap.isdisjoint(ao))

'''
정리
set는 집합이다. 만드는 법은 set(), {} 이 있다.
연산으로는
1. 합집합 : a.union(b) 혹은 |
2. 교집합 : a.intersection(b) 혹은 &
3. 차집합 : a.difference(b) 혹은 -
4. 베타적 논리합 : a.symmetric_difference(b) 혹은 ^

상위, 부분집합 확인(확인할 것 : a, 기준 : b)
a <= b a 가 b 의 부분집합인지
a < b a가 b의 진 부분집합인지
a >= b a가 b의 상위집합인지
a > b a가 b의 진 상위집합인지

집합이 같은지 확인 ==, !=
집합에 겹치는 것이 있는지 확인 : a.isdisjoint(b)

연산 후 할당 연산자
a |= b, a.update(b)
a &= b, a.intersection_update(b)
a -= b, a.difference_update(b)
a ^= b, a.symmetric_difference_update(b)

자료 수정
a.add(추가할 요소)
a.remove(제거할 요소)
a.discard(제거할 요소)
a.pop() : 임의의 요소를 뽑아냄
a.clear()
len(a)

표현식
a = {i for i in range(5)}
'''

# 심사문제

num1, num2 = map(int, input().split())
a = {i for i in range(1, num1+1) if num1 % i == 0}
b = {i for i in range(1, num2+1) if num2 % i == 0}
divisor = a & b
result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)

# 오늘의 파이썬 종료. 내일도 하자.

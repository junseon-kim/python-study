# 2020.3.3. 오늘의 파이썬 시작.

# unit 43. 정규 표현식(regular expresion)

import re

# 문자열 판단하기 : re.match('패턴', '문자열')
# 문자열에 특정 문자열이 포함되어 있는지 판단한다.
print(re.match('hello', "hello, world!"))

# 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기
# re.search('패턴', '문자열') 맨 앞 >> ^패턴, 맨 뒤 >> 패턴$
print(re.search('^hello', 'hello, world!'))
print(re.search('world!$', 'hello, world!'))

# 지정된 문자열이 하나라도 포함되는지 판단하기
# re.match 를 사용, 패턴에는 '문자열|문자열|문자열|...' 이 들어간다.
print(re.match('hello|world|!', 'hello, world!'))

# 범위 판단하기
# 문자열에 숫자가 있는지 판단 : [숫자 범위]* or + +는 1개 이상 있는지, *는 0개 이상 있는지
# ex : re.match('[0-9]+', '1234')
print(re.match('[0-9]*', '123456'))

# 활용
print(re.match('a+b', 'b'))  # b는 반드시 있어야 하고, a가 1개 이상 있는지 본다.
print(re.match('a*b', 'b'))  # b는 반드시 있어야 하고, a가 0개 이상 있는지 본다.
print(re.match('a+b', 'ab'))
print(re.match('a*b', 'acbcab'))  # 패턴과 문자열은 서로의 위치를 보고 판단한다.

# 문자가 한 개만 있는지 판단하기 : ?는 그 위치에 그 문자가 0개 또는 1개 인지 판단, .은 1개인지 판단.
print(re.match('abc?d', 'abd'))
print(re.match('abc.d', 'abd'))

# 문자 개수 판단하기 : 문자나 문자열 뒤에 {개수} 를 붙인다.
# 문자{개수}, (문자열){개수}
print(re.match('abc{3}d', 'abccd'))
print(re.match('abc{3}d', 'abcccd'))

print(re.match('(hello){3}', 'hellohellohello'))  # 문자열을 검사할 때는 (), 띄어쓰기는 없어야함.

# 휴대전화의 패턴이 맞는지 확인 {시작개수,끝개수} 공백이 없게 써야 한다. {2,3}
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1234-1234'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-231-3214'))

# 숫자와 영문 문자를 조합해서 판단하기 [a-zA-Z0-9]+ or *
print(re.match('[a-zA-z0-9]+', 'Hello'))
# 한글은 가-힣
print(re.match('[가-힣]+', '어머'))

# 특정 문자 범위에 포함되지 않는지 판단하기 : [^범위]+ or *
print(re.match('[^a-z]+', 'HE'))  # 범위 밖의 문자가 1개 이상 있는지 판단
print(re.match('[^a-z]*', 'Ha'))  # 범위 밖의 문자가 0개 이상 있는지 판단

# 특수 문자 판단하기 : 보통 \ 를 붙여준다. [] 안에서는 붙이지 않아도 되지만 에러가 발생할 경우 붙인다.
print(re.match('\*+', '*dsad**'))  # \특수문자
# +나 *는 전체의 개수를 판단, {}는 그 자리의 개수를 판단한다.

print(1, re.match('\d+\d+\d+', 'j1bobo'))  # \d = [0-9]  첫 글자나 전체가 숫자인지 판단
print(2, re.match('\D+', '1984189a'))  # \D 는 [0-9]를 제외한 모든 문자 가 있는지.
print(3, re.match('\w+', '1259283480a'))  # \w = [a-zA-z0-9_] 소문자, 대문자, 숫자, 밑줄 여부
print(4, re.match('\W+', 'QNVEFKDALa'))  # \W는 \w 이외의 문자가 있는지 판별

# 공백 처리하기
'''
' '로 공백 문자를 넣어도 되고, \s 나 \S를 사용해도 된다.
\s = [ \t\n\r\f\v]
\S = [^ \t\n\r\f\v] 이 문자가 외의 문자가 있는지 판별
\t : 탭
\n : 새 줄, 라인 피드
\r : 캐리지 리턴
\f : 폼피드
\v : 수직 탭
'''
print(re.match('[\s ]+', '\t fdfaa'))
print(re.match('[\S]+', 'a \t'))

# 표현식 할당 : re.compile('패턴')
p = re.compile('[0-9]+')
print(p.match('1'))

# 그룹 사용하기 : 패턴을 (패턴1) (패턴2) 로 표현하면 문자열을 공백을 기준으로 그룹화한다.
m = re.match('([0-9]+) ([0-9]+)', '124 324')
print(m.group(1))
print(m.group(2))
print(m.group())
print(m.group(0))
# 1은 그룹 1번, 2는 2번, ()는 전부, 0 도 전부. 매칭되지 않으면 에러가 발생한다.
print(m.groups())  # 매치객체.groups()는 각 그룹의 문자열을 튜플로 반환한다.

# 그룹 이름 짓기 (?P<이름>정규표현식)
aa = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<args>\w+)\)', 'print(1234)')
print(aa.group('func'))
print(aa.group('args'))

# 패턴에 매칭되는 모든 문자열 가져오기 : re.findall('패턴', '문자열')
# 공백 기준으로 그룹화 하고, 패턴에 매칭되는 것만 뽑아와서 리스트의 형태로 반환.
print(re.findall('[0-9]+', '1 2 3 4 Fizz Buzz 4 geeda 4'))

# +, * 와 그룹 활용하기
# (.[a-z]+)* 는 점과 영문 소문자가 1개 이상 있는지 판단하고, 이것 자체가 0개 이상인지 판단한다.
# 규칙은 반드시 지켜야 하지만 있어도 되고 없어도 되는 상황에 사용.
print(re.match('[a-z]+(.[a-z]+)*$', 'hello.world'))  # .문자 가 있고 패턴에 매칭.
print(re.match('[a-z]+(.[a-z]+)*$', 'hello.1234'))  # .문자 가 있으나 숫자이므로 매칭 불가
print(re.match('[a-z]+(.[a-z]+)*$', 'hello'))  # .문자가 없으므로 0개 이상의 조건 만족. 매칭
# (패턴+)* 는 패턴이 있으면, 이 패턴이 특정 패턴을 만족하거나 아예 이 패턴이 없을 때 매칭.

# 문자열 바꾸기 : re.sub('패턴', '바꿀문자열', '문자열', 바꿀 횟수)
# 문자열에서 패턴을 찾아 바꿀문자열로 바꾼다.
print(re.sub('apple|orange', 'fruit', 'pan pine apple apple pan'))

# 바꿀 문자열은 교체함수를 넣어도 된다.
# 교체함수는 매치객체를 받아 바꿀 결과를 문자열로 반환하면 된다.
# 예시
def multiple10(m):
    num = int(m.group())
    return str(num*10)
print(re.sub('[0-9]+', multiple10, '1 2 3 4 abc def 5 6 hg 8 10'))

# 찾은 문자열을 결과에 다시 사용하기 : 그룹으로 묶고, 1번 그룹은  \\1 의 형식으로 사용한다.
print(re.sub('([a-z]+) ([a-z]+)', '\\2 \\1 \\2 \\1', 'hello world'))
# 그룹화 하고, 2번 1번 2번 1번 으로 문자열을 반환.
# 활용 : { "name": "james" } 를 '<name>james</name>' 로 바꾸기
ab = re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }')
print(ab)

# 그룹 이름으로 가져오기 : 이름을 ?P<이름> 으로 이름을 지정했다면 사용할 수 있다.
# \\g<이름>
# \\g<숫자>

# raw 문자열 : r'문자열' 의 형태로 사용하면, 특수문자 앞에 \를 붙일 필요 없이 사용할 수 있다.
# \g<이름>, \1 \2 \3 등.

# 연습문제 : 이메일 주소 검사하기

import re
p = re.compile('^[\w+\-.]+@[\w-]+\.[\w\-.]+$')
emails = ['python@mail.example.com', 'python+kr@example.com',  # 올바른 형식
         'python-dojang@example.co.kr', 'python_10@example.info',  # 올바른 형식
         'python.dojang@e-xample.com',  # 올바른 형식
         '@example.com', 'python@example', 'python@example-com']  # 잘못된 형식

for email in emails:
    print(p.match(email) != None, end=' ')


# 심사문제 : url 검사
import re
url = input()
print(re.match('^https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[/a-zA-Z0-9-_.?=]*', url) != None)

# 왜 자꾸 틀리나 했더니 import re 를 사용하지 않아서 였다. 아효

# 오늘의 파이썬 종료!




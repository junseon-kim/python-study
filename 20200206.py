# 2020.2.6. 오늘도 파이썬을 배우러 왔다.

# unit 27 파일에 문자열 쓰기, 읽기

# 파일에 문자열 쓰기 : open > write > close 파일객체를 얻고 write메서드를 사용.

# file = open('./file practice/hello.txt', 'w')
# file.write('hello, world!')
# file.close()

# 파일의 문자열 읽기 : read
# file = open('./file practice/hello.txt', 'r')
# s = file.read()
# print(s)
# file.close()

# 자동으로 파일 객체 닫기 : with open('파일이름', '파일모드') as 파일객체:

# with open('./file practice/hello.txt', 'r') as file:
#     s = file.read()
#     print(s)

# 문자열 여러줄을 파일에 읽고 쓰기

# 읽기
# with open('./file practice/hello.txt', 'w') as file:
#     for i in range(3):
#         file.write('hello, world! {0}\n'.format(i))
# 파일에 문자열을 넣을 때에는 자동 개행이 되지 않기 때문에 수동으로 해주어야 한다.

# 리스트에 들어있는 문자열을 파일에 쓰기
# lines = ['hihi..\n', 'python\n', 'coding dojang.\n']
#
# with open('./file practice/hello.txt', 'w') as file:
#     file.writelines(lines)

# 파일의 내용을 한 줄씩 리스트로 가져오기
# with open('./file practice/hello.txt', 'r') as file:
#     s = file.readlines()
#     print(s)

# 파일의 내용을 한 줄만 가져오기
# with open('./file practice/hello.txt', 'r') as file:
#     s = None
#     while s != '':
#         s = file.readline()
#         print(s.strip('\n'))

'''
파일에 문자열이 몇 줄이나 있는지 모르므로 readline 으로 파일을 읽을 때에는 while을 이용.
readline은 읽을 문자열이 없을때에는 빈 문자열을 반환하므로 조건식에 적용.
문자열 한 줄을 읽고 넘기고 읽고 넘기고 이렇게 작동한다.

특히 문자열을 받을 객체를 None으로 초기화 시켜주는데, 이는 조건식을 의식한 것이다.
'''

# for 문으로 파일의 내용을 줄 단위로 읽기.
# with open('./file practice/hello.txt', 'r') as file:
#     for line in file:
#         print(line.strip('\n')*2)
# 파일의 한 줄씩 line 으로 들어간다.

# 파이썬 객체를 파일에 저장하고 가져오기.
'''
파이썬 객체를 파일에 저장 : 피클링(pickling)
읽어오기 : unpickling
피클링은 pickle 모듈의 dump 메서드를 사용한다.
'''
import pickle
# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean': 90, 'english': 95, 'mathmetics': 85, 'science': 82}

# 저장 : pickling
# with open('./file practice/james.p', 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)
# pickle.dump 로 객체나 값을 저장할 때에는 파일모드를 wb 로 지정해야 한다. b 는 binary로, 컴퓨터가
# 처리하는 파일 형식이다.

# 읽기 : unpickling
# with open('./file practice/james.p', 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     print('------------------------', name, age, address, scores, sep='\n')

'''
파일의 다른 모드들
--- 명시된 활용법으로만 활용 가능 ---
w : 쓰기
r : 읽기
a : 추가 - 파일의 내용 끝에 내용을 추가
x : 파일을 생성한다. 파일이 있으면 에러를 일으키고, 없으면 파일을 만든다.

--- 읽기/쓰기가 모두 가능하지만 부가 기능이 다름 ---
w+ : 파일의 기존 내용을 버린다.
r+ : 파일의 처음부터 쓰기 - 파일의 내용은 유지된다.
a+ : 파일의 끝부터 쓰기 - 파일의 내용은 유지된다.
x+ : 파일이 이미 존재하면 에러가 발생. 존재하지 않으면 생성한다.
'''


# 심사문제 특정 문자가 있는 단어를 출력
# words.txt 파일이 주어짐.

# with open('./file practice/words.txt', 'r') as file:
#     lines = file.readline().split(' ')
#     for line in lines:
#         if 'c' in line:
#             print(line.strip(',.'))

# 내용이 짧으므로 오늘은 한 유닛을 더 하기로 한다.

# unit 28 회문 판별하기 palindrome
# 회문 : 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장.

s = None
# 1. 반복문을 이용하기
# while s != 'stop':
#     s = ''.join(input('알아보고 싶은 문자열을 입력하세요. : ').split())
#     ispalindrome = True
#
#     # 1. 반복문 이용하기
#     # for i in range(len(s)//2):
#     #     # if s[i] != s[len(s)-i -1]: # 그새 잊었다. 파이썬은 -1을 인덱스로 입력하면 맨 끝이 된다.
#     #     if s[i] != s[-1 -i]:
#     #         ispalindrome = False
#
#     # 2. 슬라이스를 이용하기
#     # print(s == s[::-1])  # 전체를 반대로한 것과 원래의 것을 비교.
#     # if s!=s[::-1]:
#     #     ispalindrome = False
#
#     # 3. 리스트와 reversed 사용하기
#     # if list(s) != list(reversed(s)):
#     #     ispalindrome = False
#
#     # 4. join과 reversed 사용하기
#     if s != ''.join(reversed(s)):
#         ispalindrome = False
#
#     print(ispalindrome)

# N-gram : 문자열에서 N개의 연속된 요소를 추출하는 방법.

# zip은 두개의 요소를 튜플로 묶어주는 역할을 한다. 2-gram을 만드는 방법은 두 문자열은 zip 으로 묶는 것.
# zip 에 3개 이상의 요소를 넣고 싶다면, zip(요소1, 요소2) 가 아닌
# zip() 에 *[요소, ...] 를 넣어주면 된다.
# zip의 요소는 은 기본적으로 튜플이다.



# text = 'helloworld'
# num = int(input())
# grams = zip(*[text[i:] for i in range(num)])
#
# for i in grams:
#     print(type(i))
#     print(list(i))
'''
N-gram 은 특정 단어만 추출하여 단어의 빈도를 세는데 이용된다.
활용도가 매우 높다.
'''

# 심사문제 : words.txt 에서 회문인 단어를 각 줄에 출력하는 프로그램을 만들어라.
with open('./file practice/words2.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        ex = line.strip('\n')
        # if ex == ex[-1:-len(ex)]: ex[::] 처음은 무조건 증가하므로 맨 끝에서 -1을 써야한다.
        if ex == ex[::-1]:
            print(ex)

'''
정리
파일 열기, 쓰기, 읽기, 닫기
파일객체 = open('파일이름', '파일모드')
파일객체.write('문자열') 문자열만 넣을 수 있음
파일객체.writelines('리스트') 문자열 리스트를 넣을 수 있다.

line = 파일객체.read() 파일 전체
line = 파일객체.readlines() \n을 기준으로 하나씩 끊어서 리스트로 가져옴
line = 파일객체.readline() \n을 기준으로 한줄씩 가져온다. 반복해서 실행해야함.
파일객체.close()

자동으로 닫기
with open('파일이름', '파일모드') as 파일객체:
    실행할 코드

파이썬 객체를 저장, 읽기
import pickle
pickle.dump(객체, 파일객체) 객체를 파일객체에 저장
객체 = pickle.load(파일객체) 파일객체의 정보를 읽어온다.
'''

# 오늘의 파이썬 종료!

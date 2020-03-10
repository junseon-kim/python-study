# 2020.3.10. django를 책으로 공부해 보기로 했다. 일단 Django 한 그릇 뚝딱.

# 실전 예제 1
name = '김준선'
age = 24
school = '한국해양대학교'
job = '대학생'

letters = f"""안녕하세요! {name}입니다.
저는 {school}에 재학중이고, {age}살 입니다.
잘 부탁드립니다."""
print(letters)

# 실전 예제 2

def solution(num_str):
    nums = "0123456789"
    for i in num_str:
        if i in nums:
            nums = nums.replace(i, '')
    return nums


input_str1 = "012345678"
input_str2 = "4837500219"
input_str3 = "242810485760109726496"
print(f"{solution(input_str1)}, {solution(input_str2)}, {solution(input_str3)}")

# 실전 예제 3
import re
def solution2(input_str):
    output_str = ''

    for i in input_str:
        if re.match('[0-9]+', i) == None:
            output_str += i
    return output_str


input_str1 = 'H123e4l5l6o7, P8y9t1h2o3n.4'
input_str2 = '6L11if3e 4is 5to1o0 sh00or3t'
input_str3 = '7Y3o7u n456ee2d5 6pyt9h5on2'
print(f"{solution2(input_str1)}, {solution2(input_str2)}, {solution2(input_str3)}")

# 실전 예제 4
def solution3(input_str):
    inp = sorted(input_str)
    alpha_dict = {}
    for i in inp:
        if i not in alpha_dict.keys():
            alpha_dict[i] = 1
        else:
            alpha_dict[i] += 1
    return ''.join([f'{i}{j}' for i, j in alpha_dict.items()])


input_str1 = "aaabbccd"
input_str2 = "ffaafddde"
input_str3 = "aabcdadbbfweeaddfadf"
print(f"{solution3(input_str1)}, {solution3(input_str2)}, {solution3(input_str3)}")

# 실전 예제 5
# 이번 예제는 Data Frame을 배우면서 한다.
'''
df DataFrame에 먼저 avg칼럼을 추가, 행별 평균값을 구한다. 이후 avg_high 칼럼을 추가해 avgㄱ밧이 2.5
를 넘으면 True, 넘지 않으면 False 값으로 나타내라.
'''
import pandas as pd
def solution(df):
    # Write your code
    # 처음 보는 것이라 답지를 봤는데, 신기하게도 pandas는 열간의 연산이 가능한 것 같다.
    df['avg'] = (df['math']+df['science'])/2
    df['avg_high'] = df['avg']>2.5
    return df
    #
data = {"name": ["Moon", "choi", "Song", "Jang"],
"math": [4.0, 2.1, 4.7, 2.6],
"science": [3.8, 1.7, 0.7, 2.4]}
# 데이터 프레임에 들어갈 데이터 정의. 딕셔너리나 numpy의 array로 정의할 수 있다.

df = pd.DataFrame(data, columns=["name", "math", "science"])
# pd.DataFrame(데이터, columns=리스트, index=리스트)
# 컬럼은 가로 위, 인덱스는 세로 왼쪽이다.

print(solution(df))

'''
df.index
df.columns
df.values : 값 얻기
df.index.name = 문자열
df.columns.name = 문자열
'''
# print(df['name'])
# print(df.name)
# print(df[['name', 'math']])
#
# # 값 할당 : 만약 값이 하나만(ex - 5) 있다면 전부 그 값으로 채운다.
# df['science'] = [1, 2, 3, 4]
# print(df)
#
# # 새로운 열을 추가하기
# import numpy as np
# df['zeros'] = np.arange(4)
# print(df)
#
# # Series를 추가하기
# val = pd.Series([-1.2, -1.5, -1.7], index=[1, 2, 3])
# df['debt'] = val
# print(df)

''' 알게된 사실
Data Frame은 열간의 연산이 가능하고, 데이터 처리가 매우 쉽다.
'''
# Django 한 그릇 뚝딱 76p까지.
# 2020.3.4. 오늘의 파이썬 시작!

# unit 44. 모듈과 패키지 사용하기

'''
모듈 : 각종 변수, 함수, 클래스를 담고 있는 파일. 특정 기능을 .py 파일 단위로 작성한 것
패키지 : 여러 모듈을 묶은 것. 특정 기능과 관련된 여러 모듈을 묶은 것.
파이썬 표준 라이브러리 : 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를 묶어서
                      파이썬 표준 라이브러리(Python Standard Library, PSL)라 부른다.

import 로 모듈 가져오기
import 모듈
import 모듈1, 모듈2
모듈.변수
모듈.함수()
모듈.클래스()
'''

# math 사용하기
import math
print(math.sqrt(2))
print(math.sqrt(4))

# import as로 모듈 이름 지정하기
import math as ma

# from import 로 일부만 가져오기
from math import pi
print(pi)

# 가져올 모듈 해제하기, 다시 가져오기
del math
import importlib
import math
importlib.reload(math)

# import로 패키지 가져오기
'''
import 패키지.모듈
import 패키지.모듈1, 패키지.모듈2
패키지.모듈.변수
패키지.모듈.함수()
패키지.모듈.클래스()
'''

# import as 로 패키지 모듈 이름 지정하기
import urllib.request as r

# from import 로 패키지의 모듈에서 일부만 가져오기
'''
from 패키지.모듈 import 변수
from 패키지.모듈 import 함수
from 패키지.모듈 import 클래스
from 패키지.모듈 import 변수, 함수, 클래스
'''
# 파이썬 패키지 인덱스에서 패키지 설치하기
# 파이썬 패키지 인덱스(Python Package Index, PyPI)
# pip 설치하기 : Windows는 기본 탑재.

# pip로 패키지 설치하기 : pip install
# cmd에서 pip install 패키지 로 설치한 패키지는 import 패키지 로 불러올 수 있다.

'''
pip search 패키지 : 패키지 검색
pip install 패키지==버전 : 특정 버전의 패키지 설치
pip list 또는 freeze : 패키지 목록 출력
pip uninstall 패키지 : 패키지 삭제
'''

# 연습문제 : 소수점 이하 올림, 버림 구하기
# 올림 : math 모듈의 ceil(변수), 내림 : math 모듈의 floor(변수)

from math import ceil, floor
x = 1.5
print(ceil(x), floor(x))

# 심사문제 : 원의 넓이 구하기
radius = float(input())
from math import pow, pi
print(pow(radius, 2)*pi)


# 오늘의 파이썬 종료!

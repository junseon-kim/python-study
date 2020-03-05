# 2020.3.5. 오늘의 파이썬 시작.

# unit 45. 모듈과 패키지 만들기

import testmodule
print(testmodule.square(3))
print(testmodule.base)

from testmodule import base, square

print(base, square(3))

'''
모듈은 클래스도 만들어서 불러올 수 있다.
모듈은 기본적으로 현재 프로젝트의 폴더에 있는 것을 본다.
'''

print(__name__)

# 모듈에 print를 그냥 사용하면 import와 동시에 코드가 실행, print가 실행된다.
# 현재 직접 실행한 파일은 __name__이 __main__이고, import로 불러온 모듈같은 경우는 __모듈이름__이다.
# __name__이 __main__인 곳을 시작점이라고 한다.
if __name__ == '__main__':
    print('이것은 실행하는 곳이 현재 시작점인지 확인하는 코드.')
# 이것을 이용하면 테스트를 만들 수 있다.

# 패키지 만들기 : 프로젝트 폴더 안에 폴더를 만들고, __init__.py 파일을 안에 만들면 끝.
# __init__.py는 비워둘 수 있고, 이 폴더 안에 모듈을 만들면 된다.

# from testpack import operation
import testpack.operation
print(testpack.operation.add(3, 5))
print(testpack.operation.mul(3, 5))
# 패키지 모듈의 __name__은 패키지.모듈 이 된다.

# 패키지에서 from import 응용하기
'''
__init__.py 파일은 폴더가 패키지로 인식되도록 하는 역할도 하고, 이름 그대로 패키지를 초기화 한다.
그러므로
import 패키지
만 시작점에서 사용하고, __init__.py 에서
from . import 모듈1
from . import 모듈2
를 넣어둔다면 패키지를 import 한 즉시 __init__.py를 실행하여 모듈1과 모듈2를 import 한다.
. 은 현재 패키지라는 뜻.

패키지의 모든 변수, 함수, 클래스를 가져오려면 __init__.py 에
from .모듈 import 변수, 함수, 클래스
를 넣으면, 패키지를 import하자마자 전부 가져오게 된다. 혹은
from .모듈 import *
를 사용하여 모두 가져와도 된다. 하지만 이 때에는 패키지.함수() 의 형식으로 사용해야한다.

그러나 import * 를 사용하면, 공개하고 싶지 않은 것 까지도 공개할 수 있으므로
__init__.py 에서 __all__ 을 바꿔준다
__all__ = ['함수', '변수', ...]
공개해야할 것들을 넣어준다.
'''


# 모듈의 독스트링은 모듈 파일 첫 줄에 ''' ''' 또는 """ """ 를 사용하여 문자열을 넣을 수 있다.
# 패키지의 독스트링은 __init__.py 파일의 첫 줄에 넣을 수 있다.

# 심사문제
x = int(input())
# from testpack import operation#, geometry
import calcpkg.operation
import calcpkg.geometry
print(calcpkg.operation.squareroot(x), calcpkg.geometry.circle_area(x), sep='\n')
print(calcpkg.geometry.circle_area(x))
# print를 분리해서 적어넣어야 합격이라니.. 참

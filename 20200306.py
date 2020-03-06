# 2020.3.6. 오늘의 파이썬 시작.


# unit 46. 실전 예제 : 웹의 데이터로 그래프 그리기
# settings > project: 프로젝트 > interpreter injecter? > 검색 > 설치
import requests
from bs4 import BeautifulSoup

# requests.get : 웹페이지의 html을 가져온다.
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
# requests.get 에 url을 넣으면 응답 객체가 나온다.

# BeautifulSoup 객체로 만듦.
soup = BeautifulSoup(response.content, 'html.parser')  # html 문서의 내용을 가져옴
# BeautifulSoup 클래스에 응답 객체의 content 속성과 'html.parser'를 넣는다.
# content 속성에는 텍스트 형태의 html이 들어있고, 파이썬의 html.parser 모듈을 사용해서 파싱하도록
# 설정하는 것. : response.content(응답의 내용) 를 html.parser로 파싱하도록 설정한다.


# html 파싱 : 텍스트 형태의 html 코드를 분석해서 객체로 만든 뒤 검색하거나 편집할 수 있도록 만드는
#            작업. bs4는 BeautifulSoup 라이브러리이고 html 코드를 파싱하는데 사용한다.


table = soup.find('table', { 'class': 'table_develop3' })  # 테이블 안의 내용을 모두 가져옴.
# soup.find('태그', '클래스') 클래스를 넣을 때에는 딕셔너리로.

# print(table)  출력해보니 테이블 안의 모든 문자열을 가져온다. \t는 빼고.


# find('태그') : 태그를 찾아 안의 내용을 가져온다. 최초 검색된 것만.
# find_all('태그') : 태그를 모두 찾아 안의 내용을 리스트로 가져온다.
data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    # find_all 이나 find 로 찾은 것은 bs4.element.Tag 라는 클래스로, 한 덩어리의 기준은 <tag></tag>
    # 이다. 문자열이 아닌 다른 클래스라서 헷갈렸지만 이제 이해가 되었다.
    # 그래서 for td in tds 해도 문자열처럼 1글자씩 나오는 것이 아닌 한 태그로 묶여서 나오는 것
    # 이었다.

    for td in tds:  # 문자열에서 찾는 것이므로 특정 태그의 안에 있든 밖에 있든 td를 모두 찾아
        # 온 것이 tds
        # print(tds, td, type(td), type(tds), sep='\n')
        # raise Error
        if td.find('a'):  # 한 td태그 안에 a태그가 있으면 그 지점을 찾고 온도와 tds안에 5번째
            # 기온, 습도를 가져옴.
            point = td.find('a').text  # td 안의 a 태그의 내용을 가져온다.
            # 내용은 알 수 없는 url과 지역의 이름.
            temperature = tds[5].text
            humidity = tds[9].text
            # 중요 : .text 는 텍스트 자료만 가져온다.

            data.append([point, temperature, humidity])  # 데이터 리스트에 지점 이름, 온도, 습도
            # 넣기

# print(data)  # 실행해보면 각 도시의 이름과 온도, 습도가 모두 나온다.
# print(type(table)) 그냥 str이 아니라 따로 bs4.element.Tag 라는 클래스가 있다.
# print(table.find_all('tr'))

# 크롤링은 웹 페이지의 html 코드 등을 가져오는 것이기 때문에 모든 웹페이지마다 방식이 달라진다.
# >> 웹페이지마다 새로운 크롤링 코드를 짜야한다는 뜻. 개편이 되면 또 짜야한다.

with open('./20200306_weather/weather.csv', 'w') as file:
    # csv 로 저장할 때 ',' 로 구분하여 저장하면 ',' 가 1칸의 구분점이 된다.
    # \n 은 한 줄을 넘긴다. csv : Comma-separated values
    file.write('point,temperature,humidity\n')
    for i in data:
        file.write(f'{i[0]},{i[1]},{i[2]}\n')

# 데이터로 그래프 그리기
# visual studio 가 없는 관계로 visual c++ 14.0이 없다.
# 깔고있다.
import pandas as pd
# import matplotlib
# 여기서 matplotlib를 까는데 cp949 codec can't decode 0xe2 에러가 떴다.
# 이 오류를 해결하려면 open('파일경로.txt', 'rt', encoding='UTF8') 이렇게 열라고 한다.
# 파이썬 3.8 버전인데 matplotlib가 도저히 깔리지 않는다.
# 3.8은 아직 matplot을 사용하지 못하나보다.
# 그래서 파이참으로 하던 것을 아나콘다로 하기로 한다.
# 아나콘다도 3.8을 지원하지 않는다. 에라이

# 부득이하게 종료하게 되었다. 이제는 Django로 넘어간다.
# 물론 내일부터 ^^

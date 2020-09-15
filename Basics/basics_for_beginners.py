from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) urlopen 함수
   ㄴ GET 요청으로 https://www.example.com 의 HTML 코드 가져오기

2) BeautifulSoup 객체
   ㄴ BeautifulSoup 객체에서 특정 태그를 골라내기

3) 예외처리 1
   ㄴ 페이지를 찾을 수 없거나 URL 해석에서 에러가 생긴 경우 : HTTPError
   ㄴ 서버를 찾을 수 없는 경우 : URLError

4) 예외처리 2
   ㄴ None 객체에서 속성을 호출하려 할 때 : AttributeError
'''

url = 'https://www.example.com'
print()

## 1)
html = urlopen(url)
print(html.read())

print('\n' + '='*100 + '\n')

## 2)
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')  # html 대신에 html.read() 도 가능
print(bs.p)  # 여러 p 태그 중 첫번째 것을 출력

print('\n' + '='*100 + '\n')

## 3)
wrong_url = 'http://www.pythonscraping.com/pages/error.html'  # Raises HTTPError
# wrong_url = 'http://pythonscrapingthisurldoesnotexist.com'  # Raises HTTPError
try:
	html = urlopen(wrong_url)
except HTTPError as e:
	print(e)
except URLError as e:
	print('The server could not be found!')
	print(e)
else:
	print('It worked!')

print('\n' + '='*100 + '\n')

## 4)
def getTitle(url):
	try:
		html = urlopen(url)
	except:
		return None
	try:
		bs = BeautifulSoup(html.read(), 'html.parser')
		title = bs.body.h1
	except AttributeError as e:
		# body 태그가 없거나, 그 밖에 None 객체에서 내부 태그에 접근하려 할 때
		print(e)
		return None
	return title

title = getTitle(url)
if title == None:  # h1 태그가 없었을 때
	print('Title could not be found')
else:
	print(title)

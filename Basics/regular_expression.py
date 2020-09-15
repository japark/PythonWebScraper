import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) http://www.pythonscraping.com/pages/page3.html 에서 제품 이미지 태그만 골라내기
   ㄴ img 태그 중에는 제품 이외의 이미지도 있다.

2) 정규 표현식을 써서 정교하게 제품 이미지 태그만 골라낸다.
'''

url = 'http://www.pythonscraping.com/pages/page3.html'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('\.\./img/gifts/img.*\.jpg')})
for image in images:
	print(image['src'])  # image.attrs['src'] 도 가능

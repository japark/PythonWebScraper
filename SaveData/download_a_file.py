from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


# 네이버 홈페이지 로고 이미지 파일 다운로드
url = 'https://www.naver.com'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
imgLoc = bs.find('div', {'class':'logo_area'}).find('img')['src']

urlretrieve(imgLoc, 'logo.png')

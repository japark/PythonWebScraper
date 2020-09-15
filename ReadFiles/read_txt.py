from urllib.request import urlopen
from bs4 import BeautifulSoup


# 텍스트 읽기 - 영어
url = 'https://www.pythonscraping.com/pages/warandpeace/chapter1.txt'
textPage = urlopen(url)
print(textPage.read()[:1000])

print('='*100)

# 러시아어+프랑스어
url = 'https://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt'
textPage = urlopen(url)
print(str(textPage.read(), 'utf-8')[:1000])  # 명시적으로 인코딩 지정

print('='*100)

# BeautifulSoup 를 이용하는 경우, byte string 으로 전환 후 decode!
html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
content = bytes(content, 'UTF-8')
content = content.decode('UTF-8')
print(content[:1000])

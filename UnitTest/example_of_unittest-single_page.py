import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 위키피디아 페이지 하나에 대해서 제목과 내용을 확인
   ㄴ assertEqual, assertIsNotNone 메소드를 통해 assertion 시행

2) 정적 메소드(static method) setUpClass 이용
   ㄴ 전역 클래스 변수(여기서 bs)만 접근 가능, 인스턴스 변수 접근 불가능
   ㄴ 클래스를 시작할 때 한번만 실행 (불필요한 로딩 절약)
'''

class TestWikipedia(unittest.TestCase):
	bs = None

	def setUpClass():
		url = 'https://en.wikipedia.org/wiki/Monty_Python'
		TestWikipedia.bs = BeautifulSoup(urlopen(url), 'html.parser')

	def test_titleText(self):
		pageTitle = TestWikipedia.bs.find('h1').get_text()
		self.assertEqual('Monty Python', pageTitle);

	def test_contentExists(self):
		content = TestWikipedia.bs.find('div',{'id':'mw-content-text'})
		self.assertIsNotNone(content)


if __name__ == '__main__':
	unittest.main()
	## Jupyter Note 에선 위 한 줄짜리 대신 아래 두 줄을 실행
	# unittest.main(argv=[''], exit=False)
	# %reset

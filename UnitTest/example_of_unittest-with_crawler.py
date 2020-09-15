import re
import random
import unittest
from urllib.parse import unquote
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 위키피디아의 내부링크를 순회(crawl)하면서 단위 테스트 진행
   ㄴ https://en.wikipedia.org/wiki/Monty_Python 에서부터 항목페이지만을 따라 이동

2) 단위 테스트 자체는 test_PageProperties 에서 처리
   ㄴ assertEqual, assertTrue 메소드를 통해 assertion 시행
   ㄴ 보조함수들 : titleMatchesURL, contentExists, getNextLink
'''

class TestWikipedia(unittest.TestCase):

	def test_PageProperties(self):
		self.url = 'https://en.wikipedia.org/wiki/Monty_Python'
		# Test the first 10 pages we encounter
		for i in range(1, 10):
			self.bs = BeautifulSoup(urlopen(self.url), 'html.parser')
			titles = self.titleMatchesURL()
			self.assertEqual(titles[0], titles[1])
			self.assertTrue(self.contentExists())
			self.url = self.getNextLink()
		print('Done!')

	def titleMatchesURL(self):
		pageTitle = self.bs.find('h1').get_text()
		urlTitle = self.url[(self.url.index('/wiki/')+6):]
		urlTitle = urlTitle.replace('_', ' ')
		urlTitle = unquote(urlTitle)
		return [pageTitle.lower(), urlTitle.lower()]

	def contentExists(self):
		content = self.bs.find('div',{'id':'mw-content-text'})
		if content is not None:
			return True
		return False

	def getNextLink(self):
		# Returns random link on page
		links = self.bs.find('div', {'id':'bodyContent'}).find_all('a',
			href=re.compile('^(/wiki/)((?!:).)*$'))
		randomLink = random.SystemRandom().choice(links)
		return 'https://wikipedia.org{}'.format(randomLink.attrs['href'])


if __name__ == '__main__':
	unittest.main()
	## Jupyter Note 에선 위 한 줄짜리 대신 아래 두 줄을 실행
	# unittest.main(argv=[''], exit=False)
	# %reset

import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

'''
*** NOTE ***

1) unittest 와 selenium 의 결합
   ㄴ 드래그 앤 드롭이 제대로 시행되었는지 단위 테스트로 확인!

2) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

class TestDragAndDrop(unittest.TestCase):
	driver = None

	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		self.driver = webdriver.Chrome(
			executable_path='../../chromedriver/chromedriver',
			options=options)
		url = 'https://pythonscraping.com/pages/javascript/draggableDemo.html'
		self.driver.get(url)

	def tearDown(self):
		self.driver.quit()

	def test_drag(self):
		element = self.driver.find_element_by_id('draggable')
		target = self.driver.find_element_by_id('div2')
		actions = ActionChains(self.driver)
		actions.drag_and_drop(element, target).perform()
		self.assertEqual('You are definitely not a bot!',
			self.driver.find_element_by_id('message').text)


if __name__ == '__main__':
	unittest.main()
	## Jupyter Note 에선 위 한 줄짜리 대신 아래 두 줄을 실행
	# unittest.main(argv=[''], exit=False)
	# %reset

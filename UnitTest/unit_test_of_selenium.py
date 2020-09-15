from selenium import webdriver

'''
*** NOTE ***

1) Selenium 을 이용한 단위 테스트
   ㄴ Selenium 의 원래 목적은 웹사이트 테스트!
   ㄴ Javascript 에 대한 테스트 가능

2) 파이썬 단위 테스트(unittest)와의 차이!
   ㄴ class 불필요, 에러 발생시에만 메시지 출력, assertion 구문의 차이 등

3) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'https://en.wikipedia.org/wiki/Monty_Python'
driver.get(url)
# driver.title : 브라우저 탭 상의 웹사이트 제목
try:
	assert 'Monty Pthon' in driver.title
except AssertionError:
	print('Assertion Error!!!')
finally:
	driver.quit()

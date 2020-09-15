import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

'''
*** NOTE ***

1) 자바스크립트에 의한 클라이언트 측 리다이렉트 발생 확인
   ㄴ http://pythonscraping.com/pages/javascript/redirectDemo1.html 에서 테스트

2) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads

3) 루프와 명시적 대기(explicit wait)를 이용해 0.5초 간격으로 페이지를 체크, 총 10초 대기

4) div#content 요소가 사라지는 것으로 리다이렉트 발생 판단
'''

def waitForLoad(driver):
	count = 0
	while True:
		count += 1
		if count > 20:
			print('Timing out after 10 seconds and returning')
			return
		time.sleep(.5)
		try:
			elem = driver.find_element_by_tag_name("div")
		except NoSuchElementException:
			return


options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'http://pythonscraping.com/pages/javascript/redirectDemo1.html'
driver.get(url)
waitForLoad(driver)
print(driver.page_source)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

'''
*** NOTE ***

1) Ajax 가 적용된 페이지에서 implicit wait(묵시적 대기) 기능 활용
   ㄴ http://pythonscraping.com/pages/javascript/ajaxDemo.html 이용

2) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads

3) id#loadedButton 요소가 나타날 때까지 최대 10초 대기
   ㄴ 그때까지 나타나지 않으면, Timeout Exception!

4) By 와 함께 쓸 수 있는 위치 지정자
   ㄴ ID, CLASS_NAME, CSS_SELECTOR, LINK_TEXT,
      PARTIAL_LINK_TEXT, NAME, TAG_NAME, XPATH
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'https://pythonscraping.com/pages/javascript/ajaxDemo.html'
driver.get(url)
try:
	# id=loadedButton 인 요소를 서버에서 받아올 때까지 대기
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, 'loadedButton'))
	)
except TimeoutException:
	print('Cannot load button!')
finally:
	# print(driver.find_element(By.ID, 'content').text) 로도 가능
	print(driver.find_element_by_id('content').text)
	driver.quit()

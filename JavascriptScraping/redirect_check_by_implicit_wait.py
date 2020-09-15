from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

'''
*** NOTE ***

1) 자바스크립트에 의한 클라이언트 측 리다이렉트 발생 확인
   ㄴ http://pythonscraping.com/pages/javascript/redirectDemo1.html 에서 테스트

2) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads

3) 묵시적 대기(implicit wait)를 이용해 최대 15초까지 대기
   ㄴ 그때까지 목표한 요소가 나타나지 않으면, Timeout Exception!

4) body 태그가 특정문구를 포함할 경우, 리다이렉트가 완료된 것으로 판단
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver', 
	options=options)
url = 'http://pythonscraping.com/pages/javascript/redirectDemo1.html'
driver.get(url)
try:
	bodyElement = WebDriverWait(driver, 15).until(
		EC.presence_of_element_located(
			(By.XPATH, '//body[contains(text(), "This is the page you are looking for!")]')
		)
	)
	print(bodyElement.text)
except TimeoutException:
	print('Did not find the element')
finally:
	driver.quit()

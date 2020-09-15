import time
from selenium import webdriver

'''
*** NOTE ***

1) http://pythonscraping.com/pages/javascript/ajaxDemo.html 의 ajax 에 대해 테스트

2) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads

3) 태그 선택 방법들
   ㄴ find_element_by_id, find_element_by_name, find_element_by_tagname,
      find_element_by_css_selector, find_element
   ㄴ find_element 부분을 find_elements 로 하면, 조건에 맞는 모든 태그를 리스트로 반환
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'https://pythonscraping.com/pages/javascript/ajaxDemo.html'
driver.get(url)
time.sleep(3)  # Explicit Wait(명시적 대기)
print(driver.find_element_by_id('content').text)
driver.quit()

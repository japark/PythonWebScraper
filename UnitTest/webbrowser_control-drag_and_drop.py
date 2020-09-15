from selenium import webdriver
from selenium.webdriver import ActionChains

'''
*** NOTE ***

1) 웹브라우저상에서 다양한 조작 가능
   ㄴ 어떤 요소를 마우스 드래그 하여 목적지로 이동
   ㄴ drag_and_drop 메소드 이용

2) ActionChains 으로 웹브라우저에서 행할 여러 동작들을 묶어 한번에 실행 가능

3) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'https://pythonscraping.com/pages/javascript/draggableDemo.html'
driver.get(url)

element = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('div2')
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()

print(driver.find_element_by_id('message').text)
driver.quit()

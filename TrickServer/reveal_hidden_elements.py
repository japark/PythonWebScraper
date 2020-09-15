from selenium import webdriver

'''
*** NOTE ***

1) 페이지에서 보이지 않는 요소들을 색출

2) 스크레이퍼를 막기 위한 보안 요소(링크나 폼의 필드)를 숨기는 방식들:
   ㄴ CSS display:none 으로 설정된 요소들
   ㄴ <input type="hidden">
   ㄴ 보이는 화면 바깥으로 멀리 위치시킨 요소들

3) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'https://www.pythonscraping.com/pages/itsatrap.html'
driver.get(url)

links = driver.find_elements_by_tag_name('a')
for link in links:
	if not link.is_displayed():
		print('The link {} is a trap'.format(link.get_attribute('href')))

fields = driver.find_elements_by_tag_name('input')
for field in fields:
	if not field.is_displayed():
		print('Do not change value of {}'.format(field.get_attribute('name')))

driver.quit()

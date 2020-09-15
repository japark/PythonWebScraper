from pprint import pprint
from selenium import webdriver

'''
*** NOTE ***

1) 첫번째 브라우저의 쿠키를 두번째 브라우저에 복제

2) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver', 
	options=options)
driver.get('https://www.pythonscraping.com')
driver.implicitly_wait(1)
savedCookies = driver.get_cookies()

print('saved cookies:')
pprint(savedCookies)
print('\n\n')

driver2 = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
driver2.get('https://www.pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
	driver2.add_cookie(cookie)

print('After add:')
pprint(driver2.get_cookies())
print('\n\n')

driver2.get('https://www.pythonscraping.com')
driver2.implicitly_wait(1)

print('Final:')
print(driver2.get_cookies())

driver.quit()
driver2.quit()

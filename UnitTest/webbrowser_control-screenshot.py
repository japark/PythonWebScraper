from selenium import webdriver

'''
*** NOTE ***

1) 웹브라우저상에서 다양한 조작 가능
   ㄴ 웹페이지를 자동으로 스크린샷하여 이미지파일로 저장
   ㄴ get_screenshot_as_file 메소드 이용

2) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'https://www.google.co.kr'
driver.get(url)
driver.get_screenshot_as_file('./google_main.png')
driver.quit()

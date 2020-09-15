from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

'''
*** NOTE ***

1) 웹브라우저상에서 다양한 조작 가능
   ㄴ 보통 웹크롤링에서는 폼의 레이아웃만 가져와서 값을 대입하고 요청
   ㄴ Selenium 을 이용하면, 사람이 직접 폼에 값을 적고 입력버튼을 클릭하는 행동을 재현

2) 동작 관련 메소드:
   ㄴ send_keys : 대상 폼에 값을 입력 혹은 키보드 키를 누름
   ㄴ click : 대상을 마우스 클릭

3) ActionChains 으로 웹브라우저에서 행할 여러 동작들을 묶어 한번에 실행 가능

4) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    executable_path='../../chromedriver/chromedriver',
    options=options)
url = 'https://pythonscraping.com/pages/files/form.html'
driver.get(url)

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

### METHOD 1 혹은 METHOD 2 각각 시도해볼 것!!!

### METHOD 1 ###
firstnameField.send_keys('JEDI')
lastnameField.send_keys('MASTER')
submitButton.click()

### METHOD 2 ###
# actions = ActionChains(driver) \
# 	.click(firstnameField).send_keys('JEDI') \
# 	.click(lastnameField).send_keys('MASTER') \
# 	.send_keys(Keys.RETURN)
# actions.perform()

print(driver.find_element_by_tag_name('body').text)
driver.quit()

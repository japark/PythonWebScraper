import time
from urllib.request import urlretrieve
from PIL import Image
import pytesseract
from selenium import webdriver

'''
*** NOTE ***

1) 아마존 상품페이지에서 책 미리보기를 스크랩
   ㄴ 톨스토이 작품 <이반 일리치의 죽음>
   ㄴ 책 미리보기의 페이지 이미지를 내려받아 텍스트로 변환하고 파일로 저장

3) 적절한 크롬드라이버를 다운받고, 경로를 executable_path 에 입력할 것
   ㄴ https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(
	executable_path='../../chromedriver/chromedriver',
	options=options)
url = 'https://www.amazon.com/Death-Ivan-Ilyich-Nikolayevich-Tolstoy/dp/1427027277'
driver.get(url)
time.sleep(5)

# 책 미리보기 버튼 클릭
driver.find_element_by_id('imgBlkFront').click()
imageList = []
time.sleep(3)

result_txt = ''

# 'pointer' 가 style 속성에 있다면, 아직 마지막 페이지가 아님을 의미
while 'pointer' in driver.find_element_by_id(
	'sitbReaderRightPageTurner').get_attribute('style'):

	# 미리보기 페이지 넘기기
	driver.find_element_by_id('sitbReaderRightPageTurner').click()
	time.sleep(2)
	pages = driver.find_elements_by_xpath(
		'//div[@class=\'pageImage\']/div/img')

	if not len(pages):
		print('No pages found')

	for page in pages:
		image = page.get_attribute('src')
		print('Found image: {}'.format(image))
		# 중복된 페이지가 있을 수 있으므로, 중복 제거
		if image not in imageList:
			urlretrieve(image, 'page.jpg')
			imageList.append(image)
			# print(pytesseract.image_to_string(Image.open('page.jpg')))
			result_txt += pytesseract.image_to_string(Image.open('page.jpg'))

driver.quit()

# 텍스트로 변환된 책 내용을 파일로 저장
with open('result.txt', 'w', encoding='utf-8') as f:
	f.write(result_txt)

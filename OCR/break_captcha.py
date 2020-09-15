from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image, ImageOps

'''
*** NOTE ***

1) 코멘트를 작성하려면 CAPTCHA 를 통과해야 하는 웹사이트
   ㄴ https://www.pythonscraping.com/humans-only
   ㄴ 작성자, 제목, 내용, 기타 hidden input 에 값들을 넣어서 제출
   ㄴ 그러나 성공적인 제출을 위해서는 맨 아래의 CAPTCHA 테스트를 통과해야 함

2) CAPTCHA 이미지를 하드디스크에 내려받아 분석한뒤, 그 답을 폼으로 제출
   ㄴ CAPTCHA 테스트 통과 여부에 따라 다른 메시지가 출력됨
   ㄴ CAPTCHA 를 제대로 인식하지 못하는 경우가 있으므로 여러번 시도할 것!
'''

def cleanImage(imagePath):
	image = Image.open(imagePath)
	image = image.point(lambda x: 0 if x<143 else 255)
	borderImage = ImageOps.expand(image, border=20 ,fill='white')
	borderImage.save(imagePath)


url = 'https://www.pythonscraping.com/humans-only'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

# Gather prepopulated form values
imageLocation = bs.find('img', {'title': 'Image CAPTCHA'})['src']
formBuildId = bs.find('input', {'name':'form_build_id'})['value']
captchaSid = bs.find('input', {'name':'captcha_sid'})['value']
captchaToken = bs.find('input', {'name':'captcha_token'})['value']

captchaUrl = 'https://www.pythonscraping.com' + imageLocation
urlretrieve(captchaUrl, 'captcha.jpg')
cleanImage('captcha.jpg')
p = subprocess.Popen(['tesseract', 'captcha.jpg', 'captcha'],
	stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
f = open('captcha.txt', 'r')

# Clean any whitespace characters and a special character at the end
captchaResponse = f.read().replace(' ', '').replace('\n', '')[:-1]
print('Captcha solution attempt: ' + captchaResponse)

if len(captchaResponse) == 5:
	params = {'captcha_token': captchaToken, 'captcha_sid': captchaSid,
		'form_id': 'comment_node_page_form', 'form_build_id': formBuildId, 
		'captcha_response': captchaResponse, 'name': 'JEDI MASTER', 
		'subject': 'I come to seek the Grail', 
		'comment_body[und][0][value]': '...and I am definitely not a bot'}
	r = requests.post('https://www.pythonscraping.com/comment/reply/10', data=params)
	responseObj = BeautifulSoup(r.text, 'html.parser')
	if responseObj.find('div', {'class':'messages'}) is not None:
			print(responseObj.find('div', {'class':'messages'}).get_text())
else:
	print('There was a problem reading the CAPTCHA correctly!')

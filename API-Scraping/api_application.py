import json
import datetime
import random
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 위키피디아의 각 언어별 페이지들의 편집이 어느 나라에서 많이 이뤄졌는지 조사

2) https://ipstack.com/ 에서 제공하는 API를 응용!
   ㄴ IP주소에 대해 실제 주소를 반환하는 API
   ㄴ 유료지만, 한달 1만회 이하의 사용량에 대해서는 무료

3) 위 사이트에서 API 키를 발급받아서 ACCESS_KEY 변수에 저장할 것!

4) 위 API는 한달에 1만회 무료 요청횟수 제한이 있으니 너무 오래 실행하지 말 것!!!
'''

def getLinks(articleUrl):
	html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
	bs = BeautifulSoup(html, 'html.parser')
	return bs.find('div', {'id':'bodyContent'}).find_all('a', 
		href=re.compile('^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
	# 위키피디아 개정 히스토리 페이지의 URL 형식은 다음과 같다:
	# http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
	pageUrl = pageUrl.replace('/wiki/', '')
	historyUrl = 'https://en.wikipedia.org/w/index.php?title='
	historyUrl += pageUrl + '&action=history'
	print('history url is: {}'.format(historyUrl))
	html = urlopen(historyUrl)
	bs = BeautifulSoup(html, 'html.parser')
	# 로그인 안한 편집자의 경우 a.mw-anonuserlink 태그에 IP 주소가 컨텐츠로 담겨있다.
	ipAddresses = bs.find_all('a', {'class':'mw-anonuserlink'})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList


def getCountry(ipAddress):
	try:
		url = 'http://api.ipstack.com/' + ipAddress
		url += '?access_key={}&format=1'.format(ACCESS_KEY)
		response = urlopen(url).read().decode('utf-8')
	except HTTPError:
		return None
	responseJson = json.loads(response)
	return responseJson.get('country_code')


ACCESS_KEY = '<API KEY>'

random.seed(datetime.datetime.now())

links = getLinks('/wiki/Python_(programming_language)')
while(len(links) > 0):
	for link in links:
		print('-'*20) 
		historyIPs = getHistoryIPs(link.attrs['href'])
		for historyIP in historyIPs:
			country = getCountry(historyIP)
			if country is not None:
				print('{} is from {}'.format(historyIP, country))
	newLink = links[random.randint(0, len(links)-1)].attrs['href']
	links = getLinks(newLink)

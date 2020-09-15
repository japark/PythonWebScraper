import re
import random
import datetime
from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 재귀(recursion)를 활용한 크롤러 예시
   ㄴ 예시 1 : 외부링크만을 무작위로 따라가며 링크주소 출력
   ㄴ 예시 2 : 어떤 도메인에서 내부링크만을 따라가며 모든 외부링크를 추출

2) 재귀호출가능횟수에는 제한이 있음을 항상 명심!!!
'''

random.seed(datetime.datetime.now())

# Retrieves a list of all Internal links found on a page.
def getInternalLinks(bs, includeUrl):
	internalLinks = []
	# Finds all links that begin with a "/".
	for link in bs.find_all('a', href=re.compile('^(/|'+includeUrl+')')):
		if link.attrs['href'] not in internalLinks:
			if(link.attrs['href'].startswith('/')):
				internalLinks.append(includeUrl+link.attrs['href'])
			else:
				internalLinks.append(link.attrs['href'])
	return internalLinks


# Retrieves a list of all external links found on a page.
def getExternalLinks(bs, excludeUrl):
	externalLinks = []
	# Finds all links that start with "http" that
	# do not contain the current URL.
	for link in bs.find_all('a', href=re.compile('^(http)((?!'+excludeUrl+').)*$')):
		if link.attrs['href'] not in externalLinks:
			externalLinks.append(link.attrs['href'])
	return externalLinks


def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bs = BeautifulSoup(html, 'html.parser')
	externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
	if len(externalLinks) == 0:
		print('No external links, looking around the site for one.')
		domain = '{}://{}'.format(
			urlparse(startingPage).scheme,
			urlparse(startingPage).netloc
		)
		internalLinks = getInternalLinks(bs, domain)
		if len(internalLinks) == 0:
			print('No internal links, either.')
			return False
		else: return getRandomExternalLink(internalLinks[random.randint(0,
			len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	if externalLink:
		print('Random external link is: {}'.format(externalLink))
		followExternalOnly(externalLink)


def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl)
	domain = '{}://{}'.format(urlparse(siteUrl).scheme,
							  urlparse(siteUrl).netloc)
	bs = BeautifulSoup(html, 'html.parser')
	internalLinks = getInternalLinks(bs, domain)
	externalLinks = getExternalLinks(bs, urlparse(siteUrl).netloc)
	
	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			print('Message : crawling through internals...')
			allIntLinks.add(link)
			getAllExternalLinks(link)


startUrl = 'https://www.naver.com'

'''
1)followExternalOnly 와 2)getAllExternalLinks 를 한번에 하나씩만 실행할 것!
'''

## 1) 외부링크만을 무작위로 따라가며 링크주소 출력
followExternalOnly(startUrl)

## 2) 어떤 도메인(startUrl)에서 내부링크만을 따라가며 모든 외부링크를 추출
allExtLinks = set()
allIntLinks = set()
allIntLinks.add(startUrl)
# getAllExternalLinks(startUrl)

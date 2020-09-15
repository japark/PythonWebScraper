import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) http://pythonscraping.com 홈페이지에서
   src 속성이 있는 태그에 연결된 내부파일을 전부 다운로드

2) URL 경로대로 디렉토리 구조를 만들어서 파일 저장
'''

def getAbsoluteURL(baseUrl, source):
	if source.startswith('http://www.'):
		url = 'http://{}'.format(source[11:])
	elif source.startswith('http://'):
		url = source
	elif source.startswith('www.'):
		url = source[4:]
		url = 'http://{}'.format(url)
	else:
		if source.startswith('https://'):
			url = source
		else:
			url = '{}{}'.format(baseUrl, source)

	if baseUrl not in url:
		return None

	return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
	path = absoluteUrl.replace(baseUrl, '')
	path = downloadDirectory + path
	queryStartIdx = path.find('?')
	if queryStartIdx != -1: path = path[:queryStartIdx]
	directory = os.path.dirname(path)

	if not os.path.exists(directory):
		os.makedirs(directory)

	return path


downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

html = urlopen(baseUrl)
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.find_all(src=True)

for download in downloadList:
	fileUrl = getAbsoluteURL(baseUrl, download['src'])
	if fileUrl is not None:
		urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))

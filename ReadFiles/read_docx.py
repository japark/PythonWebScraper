from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup


# http://pythonscraping.com/pages/AWordDocument.docx 내용을
# 로컬파일로 다운로드 받지 않고 읽기
url = 'http://pythonscraping.com/pages/AWordDocument.docx'
wordFile = urlopen(url).read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'html.parser')
# print(wordObj.prettify())
textStrings = wordObj.find_all('w:t')
# print(textStrings)

for textElem in textStrings:
	text = textElem.text
	try:
		style = textElem.parent.previous_sibling.find('w:pstyle')
		if style is not None and style['w:val'] == 'Title':
			text = '<h1>' + text + '</h1>'
	except AttributeError:
		pass
	print(text)

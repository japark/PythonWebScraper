import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 다양한 웹 브라우저들을 비교한 HTML 테이블을 csv 파일로 저장
url = 'https://en.wikipedia.org/wiki/Comparison_of_web_browsers'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

# The main comparison table is currently the first table on the page
table = bs.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

csvFile = open('webbrowsers.csv', 'wt+', encoding='utf-8', newline='')
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
		for cell in row.find_all(['td', 'th']):
			csvRow.append(cell.get_text().strip())
		writer.writerow(csvRow)
finally:
	csvFile.close()

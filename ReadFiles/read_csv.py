import csv
from urllib.request import urlopen
from io import StringIO


# http://pythonscraping.com/files/MontyPythonAlbums.csv 내용을
# 로컬파일로 다운로드 받지 않고 읽기
url = 'http://pythonscraping.com/files/MontyPythonAlbums.csv'
data = urlopen(url).read().decode('ascii', 'ignore')

dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
for i, row in enumerate(csvReader):
	if i != 0:
		print('The album "{}" was released in {}'.format(row[0], str(row[1])))
	else:
		print(row[0], row[1])

print('='*100)

# DictReader 활용
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
	# row 는 OrderedDict 형식
	print('The album "{}" was released in {}'.format(row['Name'], str(row['Year'])))

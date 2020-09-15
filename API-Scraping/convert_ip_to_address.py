import json
from urllib.request import urlopen

'''
*** NOTE ***

1) https://ipstack.com 에서 IP주소에 대한 실제 주소를 알려주는 API를 제공
   ㄴ 유료지만, 한달 1만회 이하의 사용량에 대해서는 무료!

2) 위 사이트에서 API 키를 발급받아서 ACCESS_KEY 변수에 저장할 것!
'''

def getCountry(ipAddress):
	url = 'http://api.ipstack.com/' + ipAddress
	url += '?access_key={}&format=1'.format(ACCESS_KEY)
	response = urlopen(url).read().decode('utf-8')
	responseJson = json.loads(response)
	return responseJson.get('country_code')


ACCESS_KEY = '<API KEY>'

print(getCountry('50.78.253.38'))

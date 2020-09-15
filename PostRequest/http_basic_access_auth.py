import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth


# http://pythonscraping.com/pages/auth/login.php 에서
# HTTP 기본 접근 인증 방식(basic access authentication) 처리하기
# 아이디와 비밀번호는 아무거나 입력가능!
auth = HTTPBasicAuth('TestUser', 'password')
url = 'http://pythonscraping.com/pages/auth/login.php'
r = requests.post(url=url, auth=auth)
print(r.text)

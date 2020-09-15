import requests


# https://pythonscraping.com/pages/form.html 페이지에서
# 로그인 폼에 대한 POST 요청 테스트
params = {'firstname':'Jedi', 'lastname':'Master'}
url = 'https://pythonscraping.com/pages/processing.php'
r = requests.post(url, data=params)
print(r.text)

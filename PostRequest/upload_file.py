import requests


# http://pythonscraping.com/pages/form2.html 페이지에서
# 파일 업로드를 위한 POST 요청 테스트
files = {'uploadFile': open('img.jpg', 'rb')}
url = 'http://pythonscraping.com/pages/processing2.php'
r = requests.post(url, files=files)
print(r.text)

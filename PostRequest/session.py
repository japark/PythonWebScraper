import requests

'''
*** NOTE ***

1) https://pythonscraping.com/pages/cookies/login.html 에서 세션 테스트
2) username 은 아무거나, password 는 password 로 입력
3) 세션 객체가 쿠키, 헤더 등을 세션 정보로 관리
'''

session = requests.Session()

params = {'username': 'TestUser', 'password': 'password'}
welcome_page = 'https://pythonscraping.com/pages/cookies/welcome.php'
s = session.post(welcome_page, params)

print("Cookie is set to:")
print(s.cookies.get_dict())
print('Going to profile page...')

profile_page = 'https://pythonscraping.com/pages/cookies/profile.php'
s = session.get(profile_page)
print(s.text)

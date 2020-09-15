import requests


# https://pythonscraping.com/pages/cookies/login.html 에서 쿠키 테스트
# username 은 아무거나, password 는 password 로 입력
params = {'username': 'TestUser', 'password': 'password'}
welcome_page = 'https://pythonscraping.com/pages/cookies/welcome.php'
r = requests.post(welcome_page, params)

print('Cookie is set to:')
print(r.cookies.get_dict())
print('Going to profile page...')

profile_page = 'https://pythonscraping.com/pages/cookies/profile.php'
r = requests.get(profile_page, cookies=r.cookies)
print(r.text)

import smtplib
from email.mime.text import MIMEText

'''
*** NOTE ***

1) Google 의 SMTP 서버를 이용해서 이메일을 보내는 예제

2) https://goo.gl/eSHJxu 의 Okwii, radtek 두 유저의 답변 참조

3) Google 계정의 보안수준 조정이 필요
   - https://www.google.com/settings/security/lesssecureapps

4) email 패키지의 MIMEText 는 본 예제에서는 안쓰였지만, 쓰이는 경우가 있다.
'''

def send_email(user, pwd, recipient, subject, body, port):
	'''
	- user, pwd -> Google 계정주소, 비밀번호
	- recipient -> 수신메일주소
	- subject, body -> title and content of an email
	- port -> 587 or 465 택일
	'''
	FROM = user
	TO = recipient if isinstance(recipient, list) else [recipient]
	SUBJECT = subject
	TEXT = body

	# Prepare actual message
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	
	try:
		if port == 587:
			server = smtplib.SMTP("smtp.gmail.com", port)
			server.starttls()
		elif port == 465:
			server = smtplib.SMTP_SSL("smtp.gmail.com", port)
			# ssl server doesn't support or need tls, so don't call server.starttls()
		server.login(user, pwd)  
		server.sendmail(FROM, TO, message)
		print('successfully sent the mail')
	except:
		print("failed to send mail")
	finally:
		if port in [587, 465]:
			print('quit the connection')
			server.quit()
		else:
			print('Tried wrong port, please check the port again.')


send_email(
	user='',
	pwd='',
	recipient='',
	subject='TITLE HERE',
	body='CONTENT HERE',
	port=587
)

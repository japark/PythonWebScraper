import pymysql

'''
*** NOTE ***

1) 로컬 서버에서 PyMySQL 패키지의 기본적인 사용

2) 사용자 입력 사항
   - <database name> : 데이터베이스 이름을 입력
   - <table name> : 선택된 데이터베이스 안의 테이블 이름을 입력
   - passwd 속성에 로컬 서버 비밀번호 입력
'''

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='mysql')
cur = conn.cursor()
cur.execute('USE <database name>')
cur.execute('SELECT * FROM <table name> WHERE id = 1')
print(cur.fetchone())
cur.close()
conn.close()

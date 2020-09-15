import pymysql

'''
*** NOTE ***

1) SaveData/kevin_bacon_game_1.py 에서 수집한 데이터를 이용

2) 너비 우선 탐색(breadth-first search)
   ㄴ 방향성 그래프에서 가장 짧은 경로를 찾음

3) 사용자 입력 사항
   - passwd : 로컬 서버 비밀번호 입력
'''

def getUrl(pageId):
	cur.execute('SELECT url FROM pages WHERE id = %s', (int(pageId)))
	return cur.fetchone()[0]

def getLinks(fromPageId):
	cur.execute('SELECT toPageId FROM links WHERE fromPageId = %s', (int(fromPageId)))
	if cur.rowcount == 0:
		return []
	return [x[0] for x in cur.fetchall()]

def searchBreadth(targetPageId, paths=[[1]]):
	newPaths = []
	for path in paths:
		links = getLinks(path[-1])
		for link in links:
			if link == targetPageId:
				return path + [link]
			else:
				newPaths.append(path+[link])
	return searchBreadth(targetPageId, newPaths)


conn = pymysql.connect(host='127.0.0.1',
					   user='root',
					   passwd='',
					   db='mysql')
cur = conn.cursor()
cur.execute('USE wikipedia')

# targetPageId = 30825  # /wiki/Belly_Chain -> 6
# targetPageId = 18866  # /wiki/Eric_Idle -> 6
# targetPageId = 61944  # /wiki/Orlando_Bloom -> 6
targetPageId = 57968  # /wiki/Morgan_Freeman -> 6
pageIds = searchBreadth(targetPageId)
for pageId in pageIds:
	print(getUrl(pageId))

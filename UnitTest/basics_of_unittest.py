import unittest

'''
*** NOTE ***

1) 파이썬 단위 테스트 모듈 unittest 의 기본

2) unittest.TestCase 를 상속받아 테스트 클래스 작성하면 다음 기능들을 이용가능:
   ㄴ setUp, tearDown 은 매 단위 테스트의 시작과 끝에서 한번씩 실행
   ㄴ 테스트가 성공 또는 실패하게 하는 여러 타입의 assertion 문
   ㄴ text_ 로 시작하는 모든 함수를 단위 테스트로 실행, 그렇지 않은 함수는 무시
'''

class TestAddition(unittest.TestCase):

	def setUp(self):
		print('Setting up the test')

	def tearDown(self):
		print('Tearing down the test')

	def test_twoPlusTwo(self):
		total = 2+2
		self.assertEqual(4, total);


if __name__ == '__main__':
	unittest.main()
	## Jupyter Note 에선 위 한 줄짜리 대신 아래 두 줄을 실행
	# unittest.main(argv=[''], exit=False)
	# %reset

from PIL import Image
import pytesseract
from pytesseract import Output

'''
*** NOTE ***

1) Tesseract 라이브러리 설치할 것!
   ㄴ https://github.com/UB-Mannheim/tesseract/wiki 에서 인스톨러를 받아 설치
   ㄴ 명령프롬프트(window)나 터미널(linux, mac)에서 'tesseract' 명령어가 작동되는지 확인
   ㄴ 작동안될 경우, PATH 환경변수에 tesseract 설치위치를 수동으로 추가해줄 것 

2) Pytesseract : Tesseract 에 대한 파이썬 래퍼 라이브러리
   ㄴ 즉, 파이썬으로 tesseract 를 이용할 수 있게 해주는 라이브러리

3) 이미지에 담긴 글자를 인식하여 텍스트로 변환
   ㄴ 함수들의 출력형식이 주로 문자열(string)이지만, 딕셔너리나 바이트 등 다른 형식도 가능
'''

## Image to Text
print('\n'+'='*20, 'Image to Text', '='*20+'\n')
print(pytesseract.image_to_string(Image.open('./scenetext.PNG')))
print('\n*** In Byte Type ***\n')
print(pytesseract.image_to_string(Image.open('./scenetext.PNG'),
	output_type=Output.BYTES))

## Bounding Box for Each Charactor
print('\n'+'='*20, 'Bounding Box for Each Charactor', '='*20+'\n')
print(pytesseract.image_to_boxes(Image.open('./scenetext.PNG')))
print('\n*** In Python Dictionary Type ***\n')
print(pytesseract.image_to_boxes(Image.open('./scenetext.PNG'),
	output_type=Output.DICT))

## Various Data
print('\n'+'='*20, 'Various Data', '='*20+'\n')
print(pytesseract.image_to_data(Image.open('./scenetext.PNG')))
print('\n*** In Python Dictionary Type ***\n')
print(pytesseract.image_to_data(Image.open('./scenetext.PNG'),
	output_type=Output.DICT))

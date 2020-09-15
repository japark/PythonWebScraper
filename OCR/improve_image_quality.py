from PIL import Image
import pytesseract

'''
*** NOTE ***

1) 이미지 전처리를 통해 이미지 품질 향상
   ㄴ 임계점 필터를 이용하여 흐릿한 이미지를 더욱 선명하게 변환
   ㄴ 필터의 임계값은 최적화가 필요, 여기서는 수차례의 시도를 통해 216 정도로 채택
   ㄴ 임계값 최적화는 optimization_of_threshold_filter.py 파일 참조

2) 처음엔 글자인식이 전혀 안됐지만, 필터 처리 후 매우 정확하게 글자 인식!
   ㄴ badquality.PNG 에 담긴 글 : Blurred Text-Shadow in IE9 Without JavaScript
'''

def cleanFile(filePath, newFilePath):
	image = Image.open(filePath)
	image = image.point(lambda x: 0 if x<216 else 255)
	image.save(newFilePath)
	return image


img_path = './badquality.PNG'
new_path = './improvedquality.PNG'

## 필터처리 이전
image = Image.open(img_path)
print('1) Before preprocess :\n')
print(pytesseract.image_to_string(image))

print()

## 필터처리 이후
image = cleanFile(img_path, new_path)
print('2) After preprocess :\n')
print(pytesseract.image_to_string(image))

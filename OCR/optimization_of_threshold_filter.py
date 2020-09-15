import numpy as np
from PIL import Image
import pytesseract
from pytesseract import Output

'''
*** NOTE ***

1) 임계점 필터 임계값의 최적화
   ㄴ 임계값을 순차적으로 변화하며 인식정확도(confidence)를 평가

2) 임계값 215 정도에서 confidence 가 90 으로 최대!!!
   ㄴ improve_image_quality.py 에서 경험적으로 결정했던 216 이 괜찮은 값임을 증명
'''

def cleanFile(filePath, threshold):
	image = Image.open(filePath)
	# Set a threshold value for the image, and save
	image = image.point(lambda x: 0 if x<threshold else 255)
	return image


def getConfidence(image):
	data = pytesseract.image_to_data(image, output_type=Output.DICT)
	text = data['text']
	confidences = []
	numChars = []
	for i in range(len(text)):
		if int(data['conf'][i]) > -1:  # 공백문자의 경우 인식정확도가 '-1'
			confidences.append(data['conf'][i])
			numChars.append(len(text[i]))
	try:
		return np.average(confidences, weights=numChars), sum(numChars)
	except ZeroDivisionError:
		# 인식된 글자가 하나도 없을 때는 np.average 부분에서
		# ZeroDivisionError 발생하므로, 이를 예외처리해 줄 것!
		return 0, 0


filePath = './badquality.PNG'

start = 200
step = 5
end = 250

for threshold in range(start, end, step):
	image = cleanFile(filePath, threshold)
	scores = getConfidence(image)
	print('threshold: {}, confidence: {}, numChars {}'.format(
		threshold, int(scores[0]), scores[1]))

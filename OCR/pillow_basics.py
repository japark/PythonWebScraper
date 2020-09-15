from PIL import Image, ImageFilter


# PILLOW 라이브러리를 이용한 이미지 필터링
kitten = Image.open('./kitten.jpg')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('./kitten_blurred.jpg')
blurryKitten.show()

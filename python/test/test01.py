# PIL - 파이썬 이미지 처리 라이브러리

# 이미지 읽기, 저장, 화면 출력

from PIL import Image, ImageFilter
import numpy as np

# im = Image.open("cat2.jpg") # static method(팩토리 함수)
#
# print(im.size)
#
# im.save("python.jpg")

# im.show()

# 이미지 색상 변경

#im = Image.open("python.jpg").convert("L") # 메소드 체이닝, convert : "L" (gray), "RGB", "RGBA", "CMYK"

# im = Image.open("python.jpg")
# im = im.convert("L")
#
# im.show()

# 썸네일 만들기

# im = Image.open("python.jpg")
#
# # Thumbnail 이미지 생성
#
# size = (64, 64)
# im.thumbnail(size)
#
# im.save("python-thumb.jpg")
# im.show()
#
# print(im.size)

# 이미지 부분 잘라내기

# im = Image.open("python.jpg")
# cropImage = im.crop((100, 100, 150, 150)) # 좌 상 우 하
# cropImage.save("python-crop.jpg")
# cropImage.show()

# def center_crop(im):
#     crop_size = min(im.size)
#
#     left = (im.size[0] - crop_size)//2
#     top = (im.size[1] - crop_size)//2
#     right = (im.size[0] + crop_size)//2
#     bottom = (im.size[1] + crop_size)//2
#
#     return im.crop((left, top, right, bottom))
#
# im = Image.open("python.jpg")
# cropImage = center_crop(im)
# cropImage.save("python-crop.jpg")
# im2 = Image.open("python-crop.jpg")
# im2.thumbnail(im2.size)
# im2.show()

# im = Image.open("python.jpg")
#
# im2 = im.resize((600,600))
# im2.save("python-600.jpg")
# im2.show()
#
# im3 = im.rotate(90)
# im3.save("python-rotate.jpg")
# im3.show()

# im = Image.open("python.jpg")
# blurImage = im.filter(ImageFilter.BLUR)
#
# blurImage.save("python-blur.jpg")
# blurImage.show()

im = Image.open("python.jpg")

# Image = numpy array
im2arr =np.array(im) # im2arr.shape: height x width x channel
print(im2arr.shape)

# numpy array --> Image
arr2im = Image.fromarray(im2arr)
arr2im.show()
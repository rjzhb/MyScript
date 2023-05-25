import cv2
import numpy as np
import pytesseract

# 读取图片
img = cv2.imread('1.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 膨胀操作
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=1)

# 识别公式
text = pytesseract.image_to_string(dilation, lang='eng', config='--psm 6')

# 输出LaTeX代码
print(text)
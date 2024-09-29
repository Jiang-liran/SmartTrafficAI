# 导入opencv库
import cv2
# 导入numpy库
import numpy as np

# 读取图片，转换为灰度图
gray = cv2.imread('opencv_logo.jpg', cv2.IMREAD_GRAYSCALE)

# 将灰度图转换为二值图像，像素值大于200的变为0，小于等于200的变为255
ret, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
# 创建一个5x5的核
kernel = np.ones((5, 5), np.uint8)

# 使用腐蚀算法对二值图像进行处理
erosion = cv2.erode(binary, kernel, iterations=1)
# 使用膨胀算法对二值图像进行处理
dilation = cv2.dilate(binary, kernel, iterations=1)

# 显示原始灰度图
cv2.imshow('gray', gray)
# 显示二值图像
cv2.imshow('binary', binary)
# 显示腐蚀后的图像
cv2.imshow('erosion', erosion)
# 显示膨胀后的图像
cv2.imshow('dilation', dilation)

# 等待按键
cv2.waitKey(0)
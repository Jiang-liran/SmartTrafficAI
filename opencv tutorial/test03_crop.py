# 导入cv2库
import cv2

# 读取名为opencv_logo.jpg的图片
image = cv2.imread('opencv_logo.jpg')

# 裁剪图片，保留图片的第10行到第170行，第40列到第180列的像素
crop = image[10:170, 40:180]

# 显示裁剪后的图片
cv2.imshow('crop', crop)

# 等待键盘输入，0表示无限等待
cv2.waitKey(0)

import cv2 

print(cv2.getVersionString()) # 打印版本号

image = cv2.imread('opencv_logo.jpg') # 读取图片
print(image.shape) # 打印图片尺寸

cv2.imshow('image', image) # 显示图片
cv2.waitKey(0) # 等待按键
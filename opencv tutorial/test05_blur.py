import cv2  # 导入OpenCV库

image = cv2.imread('plane.jpg')  # 读取图像

gauss = cv2.GaussianBlur(image, (5, 5), 0)  # 高斯模糊
median = cv2.medianBlur(image, 5)  # 中值滤波

cv2.imshow('Original', image)  # 显示原图像
cv2.imshow('Gaussian', gauss)  # 显示高斯模糊图像
cv2.imshow('Median', median)  # 显示中值滤波图像

cv2.waitKey(0)  # 等待按键，0表示无限等待
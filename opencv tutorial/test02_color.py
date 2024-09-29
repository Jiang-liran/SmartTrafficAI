import cv2

# 读取图片
image = cv2.imread('opencv_logo.jpg') # BGR

# 显示蓝色通道
cv2.imshow("blue", image[:,:,0])
# 显示绿色通道
cv2.imshow("green", image[:,:,1])
# 显示红色通道
cv2.imshow("red", image[:,:,2])

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 显示灰度图像
cv2.imshow("gray", gray)

# 等待按键
cv2.waitKey(0)
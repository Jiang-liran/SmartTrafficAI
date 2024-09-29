# 导入cv2库
import cv2

# 使用cv2.imread()函数读取图片，参数1是图片的路径，参数2是图片的读取方式，这里是灰度读取
gray = cv2.imread('opencv_logo.jpg', cv2.IMREAD_GRAYSCALE)

# 使用cv2.Laplacian()函数进行Laplacian边缘检测，参数1是读取的图片，参数2是数据类型，这里是64位浮点型
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
# 使用cv2.Canny()函数进行Canny边缘检测，参数1是读取的图片，参数2和参数3是阈值
canny = cv2.Canny(gray, 100, 200)

# 使用cv2.imshow()函数显示图片，参数1是窗口名称，参数2是显示的图片
cv2.imshow('Original', gray)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny)

# 使用cv2.waitKey()函数等待按键，参数是等待的时间，这里是无限等待
cv2.waitKey(0)
# 使用cv2.destroyAllWindows()函数关闭所有窗口
cv2.destroyAllWindows()
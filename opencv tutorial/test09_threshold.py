import cv2

# 以灰度模式读取图像
gray = cv2.imread('hongbao.jpg', cv2.IMREAD_GRAYSCALE)

# 使用固定阈值处理，将灰度值大于10的像素设置为255，其他设置为0
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# 使用自适应高斯阈值处理，计算每个区域的阈值
# 115为区域大小，1为常数，用于调整阈值
binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY, 115, 1)

# 使用Otsu方法自动计算最佳阈值，将图像转换为二值图像
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 显示原始灰度图像
cv2.imshow('gray', gray)

# 显示固定阈值处理后的二值图像
cv2.imshow('binary', binary)

# 显示自适应阈值处理后的二值图像
cv2.imshow('binary_adaptive', binary_adaptive)

# 显示Otsu阈值处理后的二值图像
cv2.imshow('binary_otsu', binary_otsu)

# 等待按键并关闭所有打开的窗口
cv2.waitKey()
cv2.destroyAllWindows()

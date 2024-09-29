import cv2
import numpy as np

# 读取图片
image = cv2.imread("poker.jpg")
# 将图片转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 提取模板
template = gray[75:105, 235:265]

# 模板匹配
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
# 设置阈值
locations = np.where(match >= 0.9)

# 获取模板的宽度和高度
w, h = template.shape[0:2]

# 遍历匹配到的位置
for p in zip(*locations[::-1]):
    # 获取矩形的左上角坐标
    x1, y1 = p[0], p[1]
    # 获取矩形的右下角坐标
    x2, y2 = x1 + w, y1 + h
    # 在原图上绘制矩形
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 显示原图
cv2.imshow("image", image)
# 等待按键
cv2.waitKey(0)
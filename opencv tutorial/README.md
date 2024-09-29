# OpenCV 学习之旅

这个仓库包含了我在学习 OpenCV 时编写的一些 Python 脚本。每个脚本对应一个 OpenCV 中的具体概念或功能，帮助我更好地掌握计算机视觉的基础。

## 文件说明

### 1. `test00_hello.py`
**知识点**：基础 OpenCV 环境配置 
该脚本演示了如何安装和配置 OpenCV，并通过 `imshow()` 函数加载和显示一张图片。

### 2. `test02_color.py`
**知识点**：颜色处理 
该脚本展示了如何读取图像、转换图像颜色空间（如从 BGR 转换为灰度图），以及操作不同的颜色通道。

### 3. `test03_crop.py`
**知识点**：图像裁剪 
该脚本展示了如何通过 NumPy 数组切片对图像进行裁剪，选取图像的特定区域。

### 4. `test04_draw.py`
**知识点**：在图像上绘制形状 
该脚本演示了如何使用 OpenCV 绘制矩形、圆形和直线等几何图形。

### 5. `test05_blur.py`
**知识点**：图像模糊 
此脚本重点展示了如何应用不同类型的模糊（如高斯模糊、中值模糊和均值模糊）来减少图像噪声。

### 6. `test06_corner.py`
**知识点**：角点检测 
该脚本展示了使用 Harris 角点检测算法进行图像特征检测，这是计算机视觉中的一种基本技术。

### 7. `test07_match.py`
**知识点**：模板匹配 
在这个脚本中，我学习了模板匹配技术，通过查找模板图像的位置来检测目标图像中的特定部分。

### 8. `test08_gradient.py`
**知识点**：图像梯度与边缘检测 
该脚本介绍了如何使用 Sobel 和拉普拉斯算子计算图像梯度，以实现图像中的边缘检测。

### 9. `test09_threshold.py`
**知识点**：图像阈值化 
此脚本展示了阈值化处理的概念，包括二值化、自适应阈值化和 Otsu 阈值化，用于将图像分割为前景和背景。

### 10. `test10_morphology.py`
**知识点**：形态学变换 
该脚本展示了如何应用形态学操作（如腐蚀、膨胀、开运算和闭运算）来优化图像结构，去除噪声。

### 11. `test11_camera.py`
**知识点**：摄像头视频捕捉 
该脚本通过调用摄像头捕捉实时视频，并在视频流上实时应用图像处理操作，如将视频转换为灰度图。

## 学习目标

通过这些练习，我掌握了以下 OpenCV 函数和概念：
- 基础的图像读写操作 (`imshow`, `imread`, `imwrite`)
- 颜色空间转换 (`cvtColor`)
- 使用 NumPy 进行图像操作
- 在图像上绘制和标注
- 图像平滑和模糊处理技术
- 特征检测（如角点检测、模板匹配）
- 基于梯度的边缘检测
- 图像阈值化处理
- 形态学变换操作用于去噪
- 使用摄像头进行实时图像处理
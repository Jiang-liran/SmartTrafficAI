import cv2
from deepface import DeepFace

# 创建 VideoCapture 对象
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # 检测表情
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        cv2.putText(frame, f'Emotion: {emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    except Exception as e:
        print(f"Error in emotion detection: {e}")

    # 显示图像
    cv2.imshow('camera', frame)

    key = cv2.waitKey(1)
    # 按 's' 保存快照，按 'q' 退出
    if key == ord('s'):
        cv2.imwrite('snapshot.png', frame)
        print("Snapshot saved!")
    elif key == ord('q'):
        break

# 释放资源
capture.release()
cv2.destroyAllWindows()
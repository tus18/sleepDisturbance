import cv2

eye_cascade_path = './haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

src = cv2.imread('./fase.jpg')
src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#目の検出
eyes = eye_cascade.detectMultiScale(src_gray)

for x, y, w, h in eyes:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0),2)

#保存
cv2.imwrite('./sample_after.png',src)

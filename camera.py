import cv2

cap = cv2.VideoCapture(0)
#鼻や口を目と認識してしまうのでopenCV以外を検討
eye_cascade_path = './haarcascade_eye_tree_eyeglasses.xml'
face_cascade_path = './haarcascade_frontalface_default.xml'
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
face_cascade = cv2.CascadeClassifier(face_cascade_path)

while True:
    ret, frame = cap.read()

    #文字の追加
    #edframe = frame
    #cv2.putText(edframe, 'hogehoge', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3, cv2.LINE_AA)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    faces = face_cascade.detectMultiScale(gray)

    print(len(faces))

    #顔の輪郭の書き出し
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = frame[y: y + h, x: x + w]
        face_gray = gray[y: y + h, x: x + w]

    #目の輪郭の描きだし
    for x, y, w, h in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('camera_after', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
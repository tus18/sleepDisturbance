import cv2

cap = cv2.VideoCapture(0)

eye_cascade_path = './haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

while True:
    ret, frame = cap.read()

    #frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))

    cv2.imshow('Raw Frame', frame)

    edframe = frame
    cv2.putText(edframe, 'hogehoge', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('Edited Frame', edframe)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    for x, y, w, h in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('camera_after', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
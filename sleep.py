from operator import truediv
import cv2 as cv
import dlib
from imutils import face_utils
from scipy.spatial import distance
import random
from msvcrt import getch
import subprocess

face_detector = dlib.get_frontal_face_detector()

cap = cv.VideoCapture(0)#カメラの取得
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")#分類器
face_parts_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")#ポイント位置を出力するツール

EYE_AR_THRESH = 0.2
count = 0
name='music'#音のファイル名
cmd = "python sub.py "+str(name)#サブプロセスの呼び出しコマンド


def calc_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    eye_ear = (A + B) / (2.0 * C)
    return eye_ear


def face_landmark_find(img):
    eye = 10
    # 顔検出
    img_gry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_detector(img_gry, 1)

    for face in faces:
        # 顔のランドマーク検出
        landmark = face_parts_detector(img_gry, face)
        # 処理高速化のためランドマーク群をNumPy配列に変換(必須)
        landmark = face_utils.shape_to_np(landmark)

        # ランドマーク描画
        for (x, y) in landmark:
            cv.circle(img, (x, y), 1, (0, 255, 0), -1)

        left_eye_ear = calc_ear(landmark[42:48])
        right_eye_ear = calc_ear(landmark[36:42])
        eye = (left_eye_ear + right_eye_ear) / 2.0

    return img,eye


while True:
    ret,rgb = cap.read()
    gray = cv.cvtColor(rgb,cv.COLOR_RGB2GRAY)
    rgb,eye = face_landmark_find(rgb)

    if eye < EYE_AR_THRESH:
        cv.putText(rgb,"sleepy",(10,180),cv.FONT_HERSHEY_PLAIN,3,(0,0,255),3,1)
        count = count + 1
    else:
        count = 0

    cv.imshow("frame",rgb)

    #音楽を流す処理ここから
    if count > 40:
        a=random.randint(-100,100)
        b=random.randint(-50,50)
        c=random.randint(-20,20)
        ans=a*b-c
        print('問題：',a,'*',b,'-',c)
        pro = subprocess.Popen(cmd)#音を流すプログラムを実行
        while True:
            key=int(input())
            if key == ans:#正解したら再生を終了する
                break
        pro.terminate()

    
    if cv.waitKey(1) == 27:#Escで終了
        break

cap.release()
cv.destroyAllWindows()
import cv2

img = cv2.imread('opencv.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #グレイにしたものをgrayに入れる

cv2.imshow('opencv',gray) #この3行をセットで表示機能として使う
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('save.png',img) #imgを保存
cv2.imwrite('save_gray.png',gray) #grayを保存

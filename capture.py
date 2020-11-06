import cv2
x = cv2.VideoCapture(0)
true , photo = x.read()
cv2.imwrite('/root/Desktop/vivek1.png' , photo)
x.release()

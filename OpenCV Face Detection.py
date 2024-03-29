import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("Face2.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#These arent normal parameters but for the image sample used i had to play around.
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.20, minNeighbors=8)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()


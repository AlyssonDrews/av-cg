import cv2

car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")
image = cv2.imread("")
height, width, c = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
objeto = car_cascade.detectMultiScale(gray, 1.2, 5)
print(objeto)
for (x,y,w,h) in objeto:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Image:', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

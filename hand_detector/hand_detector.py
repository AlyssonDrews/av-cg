import cv2

video  = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")

while True:
    (_, image) = video.read()
    image = cv2.flip(image, 1)
    height, width, c = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    objeto = car_cascade.detectMultiScale(gray, 1.2, 5)
    print(objeto)
    for (x, y, w, h) in objeto:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('Image:', image)
    k = cv2.waitKey(60)
    if k == 27:
        break

    video.release()
    cv2.destroyAllWindows()
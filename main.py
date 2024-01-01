import cv2

face_cascade= cv2.CascadeClassifier(r'C:\Users\sarthak maini\Dropbox\My PC (DESKTOP-AIDJQ7D)\Downloads\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX

while True:
    _, img = cap.read()

   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)


    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        area=w*h
        distance =int(45.7452-(0.000125993*(area)))
        s1="Please maintain distance from screen"
        S = 'Distance: ' + str(distance) + ' cm'
        cv2.putText(img, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        if distance<30:
            cv2.putText(img,s1,(5,100),font,1,(255, 0, 0), 2, cv2.LINE_AA)

    
    cv2.imshow('img', img)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()

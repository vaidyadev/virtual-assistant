import cv2
cam=cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,200)
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_id=input("Enter a number used ID here:")
print("Taking samples look at camera")
count=0
while True:
    ret,img =cam.read()
    con=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(con,1.3, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 2)
        count +=1
        cv2.imwrite('samples/face.'+str(face_id) + '.' + str(count) + '.jpg',con[y:y+h,x:x+w])
        cv2.imshow('image',img)
    k=cv2.waitKey(100) & 0xFF
    if k ==27: 
        break
    elif count>100:
        break
print("Samples are taken now closing the programme")
cam.release()
cv2.destroyAllWindows()
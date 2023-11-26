import cv2,os
from PIL import Image
import numpy as np
path='samples'
recog=cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def Image_and_label(path):
    impaths=[os.path.join(path,f)for f in os.listdir(path)]
    facesam=[]
    ids =[]
    for impath in impaths:
        gray_img=Image.open(impath).convert('L')
        img_arr=np.array(gray_img,'uint8')
        #print(img_arr)
        id=int(os.path.split(impath)[-1].split('.')[1])
        faces=detector.detectMultiScale(img_arr)
        for(x,y,w,h)in faces:
            facesam.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return facesam,ids
print("Training Faces. It will take a few seconds. wait...")
faces,ids=Image_and_label(path)
recog.train(faces,np.array(ids))
recog.write('trainer/trainer.yml')
print('Model trained, Now we can recognize your faces.')

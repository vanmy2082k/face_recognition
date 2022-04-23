''''
Real Time Face Recogition
	==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc                       
	==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18  

'''
import cv2
import numpy as np
import os 
from tong_hop_tieng_noi import tonghop
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:/Users/Van My/OpenCV-Face-Recognition-master/FacialRecognition/train/trainer.yml')
cascadePath = "C:/Users/Van My/OpenCV-Face-Recognition-master/FacialRecognition/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Chao Thay Huy', '2','Đỗ Trọng Tấn','Dương Văn Nam',
'Dương Minh Chiến',
'Trần Việt Dũng',
'Trần Văn Ngoan',
'Dương Hồng Khiêm',
'Nguyen Van My',
'Phạm Thị Hồng Hạnh',
'Nguyễn Thị Diễm My',
'Đinh Hoàng Hiệp',
'Đào Thái Sơn',
'Nguyễn Minh Hiếu',
'Nguyễn Xuân Hiệp',
'Trần Anh Tuấn',
'Lê Trung Tiến',
'Nguyễn Thị Nhường',
'Nguyễn Tá Anh',
'Vi Anh Tuấn',
'Lương Ngọc Đông',
'Đoàn Mỹ Hạnh',
'Nguyễn Thị Mai Trang',
'Trần Thị Duyên',
'Nguyễn Văn Tú',
'Vũ Thái Sơn',
'Lê Thuý Ngà',
'Nguyễn Lương Bằng',
'Dương Văn Huân',
'Nguyễn Thanh Hải',
'Vương Thu Hoài',
'Ngô Quang Thọ',
'Hà Thế Toản',
'Trần Quang Hào',
'Phạm Minh Thắng'
]
 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "Unknow"
            confidence = "  {0}%".format(round(100 - confidence))
        #tonghop(str(id))
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

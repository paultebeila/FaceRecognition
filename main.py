import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-known-default-rtdb.firebaseio.com/",
    'storageBucket':"face-known.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

#importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
    
    
# print(len(imgModeList))

#Load the encoding file
print("Loading encoded file.....")
file = open('encodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()

encodeListKnown, studentId = encodeListKnownWithIds

# print(studentId)
print("Encoded file loaded")

count = 0
modeType= 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)
    encodingCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    
    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgModeList[modeType]
    
    for encodeFace, faceLoc in zip(encodingCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print("matches: ", matches)
        # print("Face Distance: ", faceDis)
        
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            # print(studentId[matchIndex], " was detected")
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox = 55+x1, 162+y1, x2-x1, y2-y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
            id = studentId[matchIndex]
            
            if count == 0:
                count = 1
                modeType=1
                
    if count != 0:
        if count == 1:
            
            # get the data from realtime firebase 
            studentInfo = db.reference(f'Students/{id}').get()
            print(studentInfo)
            # get the image from the storage 
            blob = bucket.get_blob(f'Images/{id}.jpg')
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            imgStudent =cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
            # update data of attendance
            datetimeObject = datetime.strptime(studentInfo['last_attendance'], "%Y-%m-%d %H:%M:%S")
            secondPassed = (datetime.now() - datetimeObject).total_seconds()
            
            if secondPassed > 30:
                ref = db.reference(f'Images/{id}.jpg')
                studentInfo['total_attendance']+=1
                ref.child('total_attendance').set(studentInfo['total_attendance'])
                ref.child('last_attendance').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                modeType = 3
                count = 0
                imgBackground[44:44+633, 808:808+414] = imgModeList[modeType]
                
        if modeType != 3:  
            if 10 < count < 20:
                imgBackground[44:44+633, 808:808+414] = imgModeList[2]
                
            if count <= 10:    
                cv2.putText(imgBackground,str(studentInfo['total_attendance']), (861,125), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                cv2.putText(imgBackground,str(studentInfo['major']), (1006,554), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                cv2.putText(imgBackground,str(id), (1006,493), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                cv2.putText(imgBackground,str(studentInfo['standing']), (910,625), cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                cv2.putText(imgBackground,str(studentInfo['year']), (1025,625), cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                cv2.putText(imgBackground,str(studentInfo['starting_year']), (1125,625), cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                
            
            (w, h),_ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX,1,1)
            offset = (414-w)//2
            cv2.putText(imgBackground,str(studentInfo['name']), (808+offset,445), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50),1)
            
            # work on your measurements to display picture
            
            imgBackground[175:175+216, 909:909+216]=imgStudent
                
        count+=1
        
        if count >= 20:
            count = 0
            modeType= 0
            id = -1
            imgStudent = []
            studentInfo=[]
            imgStudent=[]
            imgBackground[44:44+633, 808:808+414] = imgModeList[modeType]
            
    
    # cv2.imshow("Face Attendance", img)
    cv2.imshow("Background", imgBackground)
    cv2.waitKey(1)

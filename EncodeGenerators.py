import cv2
import face_recognition
import pickle
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-known-default-rtdb.firebaseio.com/",
    'storageBucket':"face-known.appspot.com"
})


#importing the mode images into a list
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentId =[]

# print(pathList)

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # name = os.path.splitext(path)[0]
    studentId.append(os.path.splitext(path)[0])
    
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    
    
    
print(studentId)

def findEncoding(imageList):
    encodeList = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converting the color from BGR to RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding started.....")
encodeListKnown = findEncoding(imgList)
print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown, studentId]
print("Encoding complete")

file = open("encodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()

print("File Saved")
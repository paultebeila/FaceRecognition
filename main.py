import cv2
import os
import pickle
import face_recognition
import numpy as np

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
print("Loading encoded file")
file = open('encodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()

encodeListKnown, studentId = encodeListKnownWithIds

# print(studentId)
print("Encoded file loaded")

while True:
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)
    encodingCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    
    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgModeList[3]
    
    for encodeFace, faceLoc in zip(encodingCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print("matches: ", matches)
        # print("Face Distance: ", faceDis)
        
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            print(studentId[matchIndex], " was detected")
    
    # cv2.imshow("Face Attendance", img)
    cv2.imshow("Background", imgBackground)
    cv2.waitKey(1)

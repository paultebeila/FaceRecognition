import cv2
import face_recognition
import pickle
import os


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
print("Encoding complete")
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:26:35 2019

@author: rishi
"""
import cv2
import numpy as np
from os import listdir
from os . path import isfile , join
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def Detect(img):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImg, 1.02, 10, 0 | cv2.CASCADE_SCALE_IMAGE, (30, 30))
    detected = 0
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = grayImg[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.15, 15, 0 | cv2.CASCADE_SCALE_IMAGE, (10, 20))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        if len(eyes) == 1:
            detected += 1
            cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
        
    cv2.imshow("Image", img)
    return detected

def RunOnVideo():
    videoCapture = cv2.VideoCapture(0)
    if not videoCapture.isOpened():
        print("Can't open default video camera")
        exit()
        
    #windowName = "Live Video"
    showLive = True
    while(showLive):
        ret, frame = videoCapture.read()
        if not ret:
            print("Can't capture frame")
            exit()
        Detect(frame)
        #cv2.imshow(windowName, frame)
        if cv2.waitKey(30) >=0:
            showLive = False
    
    videoCapture.release()
    cv2.destroyAllWindows()

def RunOnFolder(folder):
    if (folder[-1] != "/"):
        folder = folder + "/"
    files = [join(folder,f) for f in listdir(folder) if isfile(join(folder,f))]
    windowName = None
    totalCount = 0
    for f in files:
        img = cv2.imread(f)
        #image = cv2.resize(img, (300, int(img.shape[0] * 300. / img.shape[1])), interpolation=cv2.INTER_AREA)
        if type(img) is np.ndarray:
            #grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            lCnt = Detect(img)
            totalCount += lCnt
            if windowName != None:
                cv2.destroyWindow(windowName)
            windowName = f
            #cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
            #cv2.imshow(windowName, img)
            cv2.waitKey(0)
    return totalCount

if __name__ == "__main__":
     # check command line arguments: nothing or a folderpath
    if len(sys.argv) != 1 and len(sys.argv) != 2:
        print(sys.argv[0] + ": got " + len(sys.argv) - 1
              + "arguments. Expecting 0 or 1:[image-folder]")
        exit()

    if(len(sys.argv) == 2): # one argument
        folderName = sys.argv[1]
        detections = RunOnFolder(folderName)
        print("Total of ", detections, "detections")
    else: # no arguments
        RunOnVideo()
    
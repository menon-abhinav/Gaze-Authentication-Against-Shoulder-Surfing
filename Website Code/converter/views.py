from django.http import HttpResponse
from django.shortcuts import render,redirect
import cv2

# Create your views here.
def homepage(request):
    scale_factor = 1.2
    min_neighbors = 3
    min_size = (50, 50)
    webcam=True #if working with video file then make it 'False'

    face_classifier = cv2.CascadeClassifier('converter/haarcascade_frontalface_default.xml')
    eye_classifier = cv2.CascadeClassifier('converter/haarcascade_eye.xml')
    if webcam:
        video_cap = cv2.VideoCapture(0)  # use 0,1,2..depanding on your webcam
        print("Check ",video_cap)
    
    # else:
    #     video_cap = cv2.VideoCapture("videoFile.mp4")
    while True:
        # Capture frame-by-frame
        ret, img = video_cap.read()


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.05, 3)
        # When no faces detected, face_classifier returns and empty tuple
        if faces is ():
            print("No Face Found")
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,255),2)
            cv2.imshow('img',img)
            # cv2.waitKey(0)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_classifier.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
            cv2.imshow('img',img)
            # cv2.waitKey(0)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.destroyAllWindows()
            return HttpResponse("Thanks for using VAMS")
            break

    video_cap.release()
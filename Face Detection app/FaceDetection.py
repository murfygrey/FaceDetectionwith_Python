from tkinter import Frame
import cv2  #for image processing
from random import randrange



#load some trained data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Choose face to detect
#img = cv2.imread('el.jpg')
webcam = cv2.VideoCapture(0)

while True:
#read the current frame
 successful_frame_read,frame = webcam.read()

  #converting to greyscale
 grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
 #detect faces
 face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw a rectangle around faces
 for(x,y,w,h) in face_cordinates:
  cv2.rectangle(frame, (x, y), (x+w, h+y), (randrange(256),randrange(256),randrange(256)),2 )

 #show imge in seperate window
 cv2.imshow("window_name",frame)

 #waiting until key press
 key = cv2.waitKey(1)

 #Quit
 if key==81 or key==113 :
    break
#release th video capture variable
webcam.release()

#print("Code completed")

#print coodinates of rectangle
#print(face_cordinates)

import cv2
import numpy as np
import sys
import datetime

cascPath = 'C:\\Users\\dsoto\\Google Drive\\Personales\\Proyectos\\CV2Project\\haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:

    # set file name with datetime
    filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".jpg"
    print filename

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imwrite(filename, frame)


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
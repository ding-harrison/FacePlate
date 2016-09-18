import cv2
import urllib
import os
import time
import math
import pyupm_servo as servo 

FACIAL_XML = "harrcascade_face.xml"
IMAGE_DIR = "/home/root/FacePlate/images/"
DEST_IMG = "results/facial.jpg"
urllib.urlretrieve(FACIAL_XML)
WIDTH_CENTER = 320
CURR_ANGLE = 90
PERSON_LOC = WIDTH_CENTER

# Reset the servo to 90
# Create the servo object using D3
"""
gServo = servo.ES08A(3)
gServo.setAngle(CURR_ANGLE)
while(True):
    angle_input = int(raw_input())
    gServo.setAngle(angle_input)
# Delete the servo object
del gServo 
"""
while(True):
    os.system("wget -O /home/root/FacePlate/images/image.jpg http://localhost:9000/?action=snapshot")
    time.sleep(1)
    urllib.urlretrieve(IMAGE_DIR + "image.jpg", "image.jpg")
    #urllib.urlretrieve("https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml",FACIAL_XML)

    # Open with opencv
    img = cv2.imread("image.jpg")
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create the classifier and run the algo
    faceCascade = cv2.CascadeClassifier(FACIAL_XML)

    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

    # For each face found in the image, draw a box around it
    for (x, y, w, h) in faces:
        print("Face found at x: {} y: {} w: {} h: {}".format(x,y, w, h))
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        PERSON_LOC = int(x+w/2)
    cv2.imwrite(DEST_IMG, img)

        Move person to center of the screen. Depth will be a slight problem; however, 
        we can use trial and error to find a good ratio based on the width and height
    difference = PERSON_LOC - WIDTH_CENTER
    CURR_ANGLE -= int(math.ceil(difference/2))
    print ("CURRENT ANGLE IS {}".format(CURR_ANGLE))
    if(CURR_ANGLE < 0):
        CURR_ANGLE = 0
    elif(CURR_ANGLE >= 150):
        CURR_ANGLE =150 
    # Create the servo object using D3
    gServo = servo.ES08A(3)
    gServo.setAngle(CURR_ANGLE)
    # Delete the servo object
    del gServo 
    
    time.sleep(3)

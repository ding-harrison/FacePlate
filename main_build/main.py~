import cv2
import urllib
import os
import time
import pyupm_servo as servo 

FACIAL_XML = "harrcascade_face.xml"
IMAGE_DIR = "/home/root/FacePlate/images/"
DEST_IMG = "results/facial.jpg"
os.system("wget -O /home/root/FacePlate/images/image.jpg http://localhost:9000/?action=snapshot")
time.sleep(3)

urllib.urlretrieve(IMAGE_DIR + "image.jpg", "image.jpg")
urllib.urlretrieve("https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml",FACIAL_XML)

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
cv2.imwrite(DEST_IMG, img)


# Create the servo object using D5
gServo = servo.ES08A(5)

for i in range(0,10): 
    # Set the servo arm to 0 degrees
    gServo.setAngle(0)
    print 'Set angle to 0'
    time.sleep(1)

    # Set the servo arm to 90 degrees
    gServo.setAngle(90)
    print 'Set angle to 90'
    time.sleep(1)

    # Set the servo arm to 180 degrees
    gServo.setAngle(180)
    print 'Set angle to 180'
    time.sleep(1)

# Delete the servo object
del gServo 


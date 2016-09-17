import cv2
import urllib
import os
import time
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


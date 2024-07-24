import cv2
import imutils
import os

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Path to the image
image_path = "E:\photos\ped1.jpeg"  

# Escaped backslashes

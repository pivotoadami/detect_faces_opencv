#Import the opencv library
import cv2

# Load the Haar cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the image
image = cv2.imread('ronaldinho_ronaldo.jpg')

# Detect faces in the image
faces = cascade.detectMultiScale(image, 1.1, 4)

# Draw a white rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 3)

# Display the images detected
cv2.imshow('Faces Detected', image)
cv2.waitKey()

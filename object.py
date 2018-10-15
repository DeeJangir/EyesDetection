# Deepak Jangir
import cv2
eye_cascade = cv2.CascadeClassifier('eye.xml')
video = cv2.VideoCapture(0)
#print(video.isOpened())
while video.isOpened():
	success, image = video.read()
	gra =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	eye = eye_cascade.detectMultiScale(gra, 1.2, 4)
	for (x,y,w,h) in eye:
		cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0), 2)
	cv2.imshow('De', image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
video.release()
cv2.destroyAllWindows()
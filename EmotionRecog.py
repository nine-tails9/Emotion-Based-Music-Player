import cv2 as cv
import numpy as np
import os
import random
import MusicPlayer as mp
face_recognizer = cv.face.FisherFaceRecognizer_create()
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]

face_cascade = cv.CascadeClassifier('haarcascade_frontalcatface.xml')
face_cascade2 = cv.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
face_cascade3 = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
face_cascade4 = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

def getFace(grey, cnt):
	print("extracting face ... " + cnt)
	grey = cv.cvtColor(grey, cv.COLOR_BGR2GRAY)
	grey = cv.GaussianBlur(grey, (5,5), 1)
	face = face_cascade.detectMultiScale(grey, 1.1, 5)
	if len(face) > 0:
		x, y, w, h = face[0]
		grey = grey[y:y+w, x:x+h]
		cv.equalizeHist(grey, grey)
		return (grey, face)
	face = face_cascade2.detectMultiScale(grey, 1.1, 5)
	if len(face) > 0:
		x, y, w, h = face[0]
		grey = grey[y:y+w, x:x+h]
		cv.equalizeHist(grey, grey)
		return (grey, face)

	face = face_cascade3.detectMultiScale(grey, 1.1, 5)
	if len(face) > 0:
		x, y, w, h = face[0]
		grey = grey[y:y+w, x:x+h]
		cv.equalizeHist(grey, grey)
		return (grey, face)
	face = face_cascade4.detectMultiScale(grey, 1.1, 5)
	if len(face) > 0:
		x, y, w, h = face[0]
		grey = grey[y:y+w, x:x+h]
		cv.equalizeHist(grey, grey)
		return (grey, face)
	cv.equalizeHist(grey, grey)
	return (grey, [[0, 0, 0, 0]])

def train(path_to_train):
    db = os.listdir(path_to_train)
    faces = []
    for fol in db:
    	ids = emotions.index(fol)
    	raw_img = os.listdir(path_to_train + '/' + fol)
    	for face in raw_img:
    		img = cv.imread(path_to_train + '/' + fol + '/' + face)
    		faces.append((img, ids))
    random.shuffle(faces)
    labels = []
    fin_faces = []
    cnt = 0
    epochs = len(faces) - 700
    for face, lab in faces[:epochs]:
    	fin_faces.append(cv.resize(getFace(face, str(cnt))[0], (64, 64)))
    	labels.append(lab)
    	cnt += 1
    labels = np.array(labels)
    face_recognizer.train(fin_faces, labels)
    print('Training done ... ')
    # test(faces, epochs)
def test(faces, epochs):

    cnt = 0
    for face, lab in faces[epochs:]:
    	grey = getFace(face, str(cnt))[0]
    	label = face_recognizer.predict(cv.resize(grey, (64, 64)))
    	print(label)
    	if lab == label[0]:
    		cnt += 1
    cnt = cnt/(len(faces) - epochs)
    print("accuracy = " + str(cnt) + "%")
def predict(path):
    img = cv.imread(path)
    grey = getFace(img, "2")[0]
    label = face_recognizer.predict(cv.resize(grey, (64,64)))
    return label

train('Sorted')

# cap = cv.VideoCapture(0)

# while  True:

# 	ret, frame = cap.read()
# 	grey = cv.resize(frame, None, fx = 0.5, fy = 0.5)
# 	grey = getFace(grey, '1')
# 	# print(grey[1])

# 	lab = face_recognizer.predict(cv.resize(grey[0], (64, 64)))

# 	cv.putText(frame, emotions[lab[0]], (150, 100), cv.FONT_HERSHEY_DUPLEX , 1.5, (0, 0, 0))

# 	for x, y, w, h in grey[1]:
# 		cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 	cv.imshow("ger", frame)
# 	if cv.waitKey(1) == 76:
# 		mp.playSongLocal(emotions[lab[0]])
# 		break
# 	if cv.waitKey(1) == 79:
# 		mp.playSongOnline(emotions[lab[0]])
# 		break
# 	if cv.waitKey(1) == 13:
# 		break

cv.destroyAllWindows()

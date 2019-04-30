import cv2 as cv
import numpy as np
import os
from shutil import copy2
root = 'cohn-kanade-images'
label = 'Emotion'
Image_dir = os.listdir(root)
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
for sub in Image_dir:
	parti = os.listdir(label + '/' + sub)
	for emotion_img in parti:
		if emotion_img.startswith("."):
			continue
		final_lvl = os.listdir(label + '/' + sub + '/' + emotion_img)
		if len(final_lvl) > 0:
			file = open(label + '/' + sub + '/' + emotion_img + '/' + final_lvl[0], 'r')
			emotion = int(float(file.readline()))
			final_lvl = os.listdir(root + '/' + sub + '/' + emotion_img)
			neutral = final_lvl[0]
			im_emotion = final_lvl[-1]	
			copy2(root + '/' + sub + '/' + emotion_img + '/' + final_lvl[0], "Sorted" + '/' + emotions[0])
			copy2(root + '/' + sub + '/' + emotion_img + '/' + final_lvl[-1], "Sorted" + '/' + emotions[emotion])

		
	

import glob
import os
import numpy as np
from scipy import misc
from keras.layers import Input, Convolution2D, MaxPooling2D, Flatten, Activation, Dense, Dropout
from keras.models import Model
from keras.utils.np_utils import to_categorical
from keras.utils.visualize_util import plot
import sys
from keras.models import model_from_json

img_size = (3L, 160L, 60L)
model = model = model_from_json(open(str(sys.argv[1])).read())
model.load_weights(str(sys.argv[2]))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
#plot(model, to_file='../model.png',show_shapes=True)


def ocr(filename):
	img = misc.imresize(misc.imread(filename), img_size[::-1]).T
	img = np.array([1 - img.astype(float)/255])
	return ''.join(chr(i.argmax()+ord('0')) for i in model.predict(img))
	
root = './'
truelen = 0.0
files = 0
for i in os.listdir(root):
	if os.path.isfile(os.path.join(root,i)):
		strcode = i.replace(".jpg","")
		if(strcode == ocr(i)):
			truelen += 1 
			print (i + ":" + ocr(i) + " TRUE")
		else:
			print (i + ":" + ocr(i) + " FALSE")
		files += 1
print("Test Sample:" + str(files))
print("Accuracy:" + str(truelen/files*100) + "%")

#in test sample dir 
#python ../ocrvercode.py ../test.jpg ../yanzheng_cnn_2d.model
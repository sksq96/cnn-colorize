# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2016-12-05 06:11:54
# @Last Modified by:   shubham
# @Last Modified time: 2016-12-05 07:20:22

import cv2
import pylab
import tensorflow as tf
import skimage.transform
from skimage import img_as_ubyte

def load_image(img):
	# img = imread(path)
	# crop image from center
	short_edge = min(img.shape[:2])
	yy = int((img.shape[0] - short_edge) / 2)
	xx = int((img.shape[1] - short_edge) / 2)
	crop_img = img[yy : yy + short_edge, xx : xx + short_edge]
	# resize to 224, 224
	img = skimage.transform.resize(crop_img, (224, 224))
	# desaturate image
	return (img[:,:,0] + img[:,:,1] + img[:,:,2]) / 3.0


with open("model/colorize.tfmodel", mode='rb') as f:
	fileContent = f.read()

graph_def = tf.GraphDef()
graph_def.ParseFromString(fileContent)
grayscale = tf.placeholder(tf.float32, [1, 224, 224, 1])
inferred_rgb, = tf.import_graph_def(graph_def, 
	input_map={"grayscale": grayscale},
	return_elements=["inferred_rgb:0"])

with tf.Session() as sess:
	cap = cv2.VideoCapture(0)
	idx = 0
	
	while True:
		running, frame = cap.read()
		if not running:
			break
		
		idx += 1
		if idx%1 != 0:
			continue
		
		shark_gray = load_image(frame).reshape(1, 224, 224, 1)
		inferred_batch = sess.run(inferred_rgb, feed_dict={grayscale: shark_gray})
		# print(inferred_batch[0])
		
		cv2.imshow('Video', img_as_ubyte(inferred_batch[0]))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break


# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2016-12-05 06:11:54
# @Last Modified by:   shubham
# @Last Modified time: 2017-01-07 01:26:19

import sys
import cv2
import numpy as np
import tensorflow as tf

from skimage.io import imsave, imread
from skimage.transform import resize
from skimage import img_as_ubyte
from matplotlib import pyplot as plt


def load_image(path):
	img = imread(path)
	# crop image from center
	short_edge = min(img.shape[:2])
	yy = int((img.shape[0] - short_edge) / 2)
	xx = int((img.shape[1] - short_edge) / 2)
	crop_img = img[yy : yy + short_edge, xx : xx + short_edge]
	# resize to 224, 224
	img = resize(crop_img, (224, 224))
	# desaturate image
	return (img[:,:,0] + img[:,:,1] + img[:,:,2]) / 3.0

def model():
	with open("model/colorize.tfmodel", mode='rb') as f:
		model = f.read()
	return model

def plot(img1, img2):
	fig = plt.figure()
	gs = plt.GridSpec(2, 2)
	ax1 = fig.add_subplot(gs[0, 0])
	ax2 = fig.add_subplot(gs[0, 1])
	ax3 = fig.add_subplot(gs[1, 0])
	ax4 = fig.add_subplot(gs[1, 1])
	
	ax1.imshow(img1, cmap='gray')
	ax2.hist(img1.ravel(), bins=256)
	ax3.imshow(img2, cmap='gray')
	ax4.hist(img2.ravel(), bins=256)
	
	fig.show()
	input()


def main():
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(model())
	grayscale = tf.placeholder(tf.float32, [1, 224, 224, 1])
	inferred_rgb, = tf.import_graph_def(graph_def,
		input_map={"grayscale": grayscale},
		return_elements=["inferred_rgb:0"])
	
	imgs = sys.argv[1:]
	with tf.Session() as sess:
		for imgPath in imgs:
			in_img = load_image(imgPath)
			input_vector = in_img.reshape(1, 224, 224, 1)
			inferred_batch = sess.run(inferred_rgb, feed_dict={grayscale: input_vector})
			
			in_img = img_as_ubyte(in_img)
			out_img = img_as_ubyte(inferred_batch[0])
			plot(in_img, out_img)
			# imsave('output/'+imgPath.split('/')[1], out_img)
			# print(out_img)

if __name__ == '__main__':
	main()


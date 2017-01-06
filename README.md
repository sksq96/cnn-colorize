# CNN approach to Colorize Grayscale Images

Colorization of grayscale images using the model and architecure proposed by [Ryan Dahl](http://tinyclouds.org/colorize/).

## Overview
This repository contains:
- (1) a test time demonstration using a pre-trained colorization network
- (2) pre-trained [VGG16 model](https://gist.github.com/ksimonyan/211839e770f7b538e2d8), using Hypercolumns to colorize

## Requirements

- Python
- Numpy
- Tensorflow
- Scikit-image

## Usage

```
./colorize.py [path-to-input]
```

## Results

![test_1](https://github.com/cameronfabbri/Colorful-Image-Colorization/blob/master/images/resized/testing/test_3.png?raw=true)
![test_1](https://github.com/cameronfabbri/Colorful-Image-Colorization/blob/master/images/resized/output/test_3_output.png?raw=true)


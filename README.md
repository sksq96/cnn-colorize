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

Voila ! The model seems to have learned and developed patterns for some primitive objects. It has learned to color:
- grass: green, 
- sky: blue, 
- skin: brown, 
- water: blue.

![](results/black-and-white-africa-animals-wilderness-in.jpg?raw=true)
![](results/black-and-white-africa-animals-wilderness-out.jpg?raw=true)

![](results/black-and-white-city-bird-people-in.jpg?raw=true)
![](results/black-and-white-city-bird-people-out.jpg?raw=true)

![](results/pexels-photo-12087-in.jpeg?raw=true)
![](results/pexels-photo-12087-out.jpeg?raw=true)

![](results/pexels-photo-23966-in.jpg?raw=true)
![](results/pexels-photo-23966-out.jpg?raw=true)

![](results/pexels-photo-26434-in.jpg?raw=true)
![](results/pexels-photo-26434-out.jpg?raw=true)

Sources
-------
- [Automatic Colorization](http://tinyclouds.org/colorize/)
- [Hypercolumns for Object Segmentation and Fine-grained Localization](http://arxiv.org/pdf/1411.5752v2.pdf)


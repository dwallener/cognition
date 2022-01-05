#!/Users/damir00/miniconda3/bin/python3

# keep it simple at first, all memories start at T0

# create set of base images, representing the initial memory
# loop through with delay
# each time through, degrade the images
# display the array of images

# A placeholder approach for now. Take the image, make a copy.
# One copy, guassian blur. Second copy, edge detecd.
# Adjust edge detect to have "right" colors, based on original.
# Add the two images together.

# Add paramter for edge detect sensitivity.
# Scale 0-100 (100 being most sensitive).
# Start with sensitivity 10.
# With each refresh in a time interval Tint < Threshold_refresh, bump the detect sensitivity by +5.
# With each lack of refresh in a time interval > Threshold_Remember, decrease the sensitivity by -5.

import logging
logging.basicConfig(filename='memory-degradation.log', encoding='utf-8', level=logging.DEBUG)
logging.warning("REBOOT HAPPENED HERE ===============================================")

from PIL import Image, ImageFilter
import glob

import numpy
# import cv2 let's try and avoid this dependency

# Load an array of images

image_list = []
for filename in glob.glob('../datasets/tufts_td_cs/*./jpg'):
    im = Image.open(filename)
    image_list.append(im)
logging.info("Imported a directory of images")

# perform guassian blur on each image
blurred_image_list = []
for i in image_list:
    # do the blur - opencv
    # dst = cv2.GaussianBlur(i, (5,5), cv2.BORDER_DEFAULT)
    i2 = i.filter(ImageFilter.GaussianBlur(radius=2))
    logging.info("Blurred an image")
    blurred_image_list.append(i2)
logging.info("Blurred a list of images")

# perform edge detect on each image

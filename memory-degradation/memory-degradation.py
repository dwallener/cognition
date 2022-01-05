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
import os, os.path

import numpy
# import cv2 let's try and avoid this dependency

# Load an array of images
path = "/Users/damir00/github/cognition/datasets/tufts_td_cs"
valid_images = [".jpg"]
image_list = []
for f in os.listdir(path):
    ext =  os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        logging.info("Bad image file")
    image_list.append(Image.open(os.path.join(path,f)))

# let's debug with a shortened list
short_image_list = image_list[:3]

logging.info("Imported a directory of %s images", len(image_list))
edged_list = []
blurred_list = []
# combine blur and edge generation in one loop
for i in short_image_list:
    i2 = i.filter(ImageFilter.GaussianBlur(radius=2))
    logging.info("Blurred image")
    i3 = i.filter(ImageFilter.FIND_EDGES)
    logging.info("Edged image")
    edged_list.append(i3)
    blurred_list.append(i2)

# support function to convert between image classes
# PIL to cv2
def pil2cv(image_name):
     pilimage = image_name.convert('RGB')
     open_cv_image = numpy.array(pil_image)
     # this ridiculouseness flips RGB to BGR
     open_cv_image = open_cv_image[:, :, ::-1].copy()
     return open_cv_image

# let's see what detecting facial features can give us
import cv2
import dlib

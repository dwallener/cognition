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

from PIL import Image
import glob

# Load an array of images

image_list = []
for filename in glob.glob('../datasets/tufts_td_cs/*./jpg'):
    im = Image.open(filename)
    image_list.append(im)


# perform guassian blur on each image

# perform edge detect on each image

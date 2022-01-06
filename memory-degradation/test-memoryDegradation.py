#!/Users/damir00/miniconda3/bin/python3

import memoryDegradation

image_list = memoryDegradation.loadImages("/Users/damir00/github/cognition/datasets/tufts_td_cs", ".jpg")
short_image_list = image_list[:3]
degraded_image_list = memoryDegradation.blurAndEdgeImages(short_image_list)
features_image_list = memoryDegradation.facialFeatures(short_image_list)

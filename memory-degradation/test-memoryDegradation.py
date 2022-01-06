#!/Users/damir00/miniconda3/bin/python3

import memoryDegradation
from PIL import Image, ImageFilter, ImageEnhance

# basic funtionality testing

image_list = memoryDegradation.loadImages("/Users/damir00/github/cognition/datasets/tufts_td_cs", ".jpg")
short_image_list = image_list[:1]
# degraded_image_list = memoryDegradation.blurAndEdgeImages(short_image_list)
# features_image_list = memoryDegradation.facialFeatures(short_image_list)

# now lets do something more interesting
# let's degrade for multiple generations

timeClicks = 10
time_series_degraded = []
time_series_features = []
single_image = image_list[0]
for i in range(timeClicks):
    degraded_image = memoryDegradation.blurAndEdgeImage(single_image, "NO")
    features_image = memoryDegradation.facialFeature(single_image, "NO")
    time_series_degraded.append(degraded_image)
    time_series_features.append(features_image)
    # start next iteration with results from last one, using the merged image
    single_image = degraded_image

grid = memoryDegradation.image_grid(time_series_degraded, 2, 5)
grid.show()

grid = memoryDegradation.image_grid(time_series_features, 2, 5)
grid.show()

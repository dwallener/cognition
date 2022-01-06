

from PIL import Image, ImageFilter, ImageEnhance
import logging
import os, os.path
import numpy
import cv2
import dlib

# support function to convert between image classes
# PIL to cv2
def pil2cv(image_name):
     pil_image = image_name.convert('RGB')
     open_cv_image = numpy.array(pil_image)
     # this ridiculouseness flips RGB to BGR
     open_cv_image = open_cv_image[:, :, ::-1].copy()
     return open_cv_image

def cv2pil(image_name):
    cv_image = cv2.cvtColor(image_name, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(cv_image)
    return im_pil


def loadImages(path, image_type):
    # Load an array of images
    #path = "/Users/damir00/github/cognition/datasets/tufts_td_cs"
    path = path
    #valid_images = [".jpg"]
    valid_images = image_type
    image_list = []
    for f in os.listdir(path):
        ext =  os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            logging.info("Bad image file")
        image_list.append(Image.open(os.path.join(path,f)))
    return image_list

# single image
def blurAndEdgeImage(image, show):
    i2 = image.filter(ImageFilter.GaussianBlur(radius=2))
    logging.info("Blurred image")
    i3 = image.filter(ImageFilter.FIND_EDGES)
    logging.info("Edged image")
    # 0.5 very quickly allows the edged image to dominate
    # will need some work to figure out what we actually want here
    # at 0.2 it skews towards the blurred image
    i_merged = Image.blend(i2, i3, 0.2)
    # as image degrades, it darkens, because edge lines are black
    # until we change the edge lines to be closer to the color of the original
    # pixels, let's brighten the images
    enhancer = ImageEnhance.Brightness(i_merged)
    factor = 1.1
    i_merged = enhancer.enhance(factor)
    if show == "YES":
        i_merged.show()
    return i_merged

# multiple images
def blurAndEdgeImages(images):
    return_list = []
    for i in images:
        i2 = i.filter(ImageFilter.GaussianBlur(radius=2))
        logging.info("Blurred image")
        i3 = i.filter(ImageFilter.FIND_EDGES)
        logging.info("Edged image")
        return_list.append(i3)
        return_list.append(i2)
        i_merged = Image.blend(i2, i3, 0.5)
        i_merged.show()
        return_list.append(i_merged)
    return return_list


def facialFeature(image, show):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    img = pil2cv(image)
    faces = detector(img)
    return_list = []
    for face in faces:
        x1 = face.left() # left point
        y1 = face.top() # top point
        x2 = face.right() # right point
        y2 = face.bottom() # bottom point
        # Create landmark object
        landmarks = predictor(image=img, box=face)
        # Loop through all the points
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            # Draw a circle
            cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)
    return_image = cv2pil(img)
    return return_image
    if show == "YES":
        # show the image
        cv2.imshow(winname="Face", mat=img)
        # Wait for a key press to exit
        cv2.waitKey(delay=0)
        # Close all windows
        cv2.destroyAllWindows()

def facialFeatures(images):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    for i in images:
        img = pil2cv(i)
        faces = detector(img)
        return_list = []
        for face in faces:
            x1 = face.left() # left point
            y1 = face.top() # top point
            x2 = face.right() # right point
            y2 = face.bottom() # bottom point
            # Create landmark object
            landmarks = predictor(image=img, box=face)
            # Loop through all the points
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                # Draw a circle
                cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)
        return_image = cv2pil(img)
        return_list.append(return_img)
        # show the image
        cv2.imshow(winname="Face", mat=img)\
        # Wait for a key press to exit
        cv2.waitKey(delay=0)
        # Close all windows
        cv2.destroyAllWindows()

# for displaying time series, assumes PIL format
def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

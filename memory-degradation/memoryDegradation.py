

from PIL import Image, ImageFilter
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
        return_list.append(img)
        # show the image
        cv2.imshow(winname="Face", mat=img)\
        # Wait for a key press to exit
        cv2.waitKey(delay=0)
        # Close all windows
        cv2.destroyAllWindows()

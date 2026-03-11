import cv2
import numpy as np

def sink_image(image, h):
    if image.dtype != np.uint8:
        raise TypeError("image must be uint8")
        return None

    kernel = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ], np.uint8)

    kernel2 = np.array([
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ], dtype=np.uint8)

    mask = cv2.erode(image, kernel, iterations=1) == 0
    #helper2 = cv2.erode(image, kernel2, iterations=1)
    #o1 = cv2.dilate(helper1, kernel, iterations=1)
    #o2 = cv2.dilate(helper2, kernel2, iterations=1)

    #mask1 = (image[1:-1, 1:-1] - o1[1:-1, 1:-1]) > 0
    #mask2 = (image[1:-1, 1:-1] - o2[1:-1, 1:-1]) > h
    #result = image.copy()
    result = np.where(mask, image, 0)

    return result
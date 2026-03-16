#! /usr/bin/python
# -*- coding: utf-8 -*- 
#  
# This software is licensed under  
# CeCILL FREE SOFTWARE LICENSE AGREEMENT 
 
# This software comes in hope that it will be useful but  
# without any warranty to the extent permitted by applicable law. 
   
# (C) UjoImro <ujoimro@gmail.com>, 2012 
# ProCarPlan s.r.o. 



import os
os.add_dll_directory(r"C:\Users\Koladik\Desktop\Skeleton\msys2\ucrt64\bin")
import pink
from pathlib import Path
from matplotlib import pyplot as plt
from pink import numpy_conv
import numpy as np
import cv2

from skeletonize.matcher import Matcher

def main():
    # image_path = Path("./test/cercle11.pgm")
    # image_path = Path("./test/rectangle_rips.pgm")
    image_path = Path("C:/Users/Koladik/Desktop/Skeleton/pink2/images/test_2.pgm")
    # image_path = Path("test/square_hole.pgm")

    image = pink.cpp.readimage(str(image_path))
    image_numpy_start = numpy_conv.pink2numpy(image).copy()

    image = pink.cpp.lhthinpar_test(image, 10000)
    image = pink.cpp.lhthinpar_asymmetric_test(image, -1)
    image = pink.cpp.crestrestoration(image, -1, 4)

    #image_numpy_skel1 = numpy_conv.pink2numpy(image).copy()

    # image = pink.cpp.lambdaskel(image, 4, 100)
    image_numpy_skel1 = numpy_conv.pink2numpy(image).copy()

    #image = pink.cpp.segmentlines(image, 4, 100,255)

    image_numpy_skel2 = numpy_conv.pink2numpy(image).copy()
    image_numpy = image_numpy_skel2.copy()
    wells = Matcher(image_numpy)
    wells.run()


    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.imshow(image_numpy_start)
    ax1.set_title('Было')
    ax1.axis('off')

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.imshow(image_numpy_skel1)
    ax2.set_title('Стало')
    ax2.axis('off')
    ax2.sharex(ax1)
    ax2.sharey(ax1)

    ax3 = fig.add_subplot(1, 3, 3)
    ax3.imshow(image_numpy)
    ax3.set_title('Стало')
    ax3.axis('off')
    ax3.sharex(ax1)
    ax3.sharey(ax1)

    # ax4 = fig.add_subplot(2, 3, 4)
    # ax4.imshow(image_numpy_skel3)
    # ax4.set_title('Стало')
    # ax4.axis('off')
    # ax4.sharex(ax1)
    # ax4.sharey(ax1)

    # ax5 = fig.add_subplot(2, 3, 5)
    # ax5.imshow(image_numpy_skel4)
    # ax5.set_title('Стало')
    # ax5.axis('off')
    # ax5.sharex(ax1)
    # ax5.sharey(ax1)

    # ax6 = fig.add_subplot(2, 3, 6)
    # ax6.imshow(image_numpy_skel4)
    # ax6.set_title('Стало')
    # ax6.axis('off')
    # ax6.sharex(ax1)
    # ax6.sharey(ax1)

    plt.tight_layout()
    plt.show()


if "__main__" == __name__:
    main()
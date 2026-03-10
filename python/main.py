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


def main():
    # image_path = Path("./test/cercle11.pgm")
    # image_path = Path("./test/rectangle_rips.pgm")
    image_path = Path("test/gel.pgm")
    # image_path = Path("test/square_hole.pgm")


    print(str(image_path))
    image = pink.cpp.readimage(str(image_path))
    print(image)
    #exit()
    # image_numpy = numpy_conv.pink2numpy(image)
    # #image = pink.cpp.dilatball_test(image, 1)
    # plt.imshow(image_numpy)
    # plt.show()

    image2 = pink.cpp.lhthinpar_test(image, 10000)

    image_numpy = numpy_conv.pink2numpy(image2)
    print(image_numpy)

    plt.imshow(image_numpy)
    plt.show()


if "__main__" == __name__:
    main()
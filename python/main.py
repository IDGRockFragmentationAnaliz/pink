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
    image_path = Path("./test/cercle11.pgm")
    print(str(image_path))
    image = pink.cpp.readimage(str(image_path))
    print(image.get_pixels())
    #image = numpy_conv.pink2numpy(image)
    pink.cpp.print_image(image)
    image = pink.cpp.dilatball(image, 5, 3)
    pink.cpp.print_image(image)

    #plt.imshow(pink.numpy_conv.pink2numpy(image), cmap=mpl.cm.gray, interpolation='none')

    #pink.cpp.exp(5)

   # kernel = pink.cpp.readimage(IMAGES + '/2dbyte/gray/g2fish1.pgm')
    #result = pink.cpp.dilation(image,kernel)


if "__main__" == __name__:
    main()
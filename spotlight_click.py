#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt

# -- use interactive matplotlib
plt.ion() 


# -- read in an image with scipy.ndimage
dpath  = "images"
fname  = "city_image.jpg"
infile = os.path.join(dpath, fname)
img    = nd.imread(infile)


# -- display it using matplotlib
ysize = 5.
xsize = ysize * float(img.shape[1]) / float(img.shape[0])

fig_sp, ax_sp = plt.subplots(num=0, figsize=[xsize, ysize])
fig_sp.subplots_adjust(0, 0, 1, 1)
ax_sp.axis("off")
im_sp = ax_sp.imshow(img)
fig_sp.canvas.draw()

# -- mask the whole image so it is all black
nrow, ncol = img.shape[:2]
npix = nrow * ncol
rind = np.arange(npix).reshape(nrow, ncol) // ncol
cind = np.arange(npix).reshape(nrow, ncol) % ncol
mask = np.zeros(img.shape, dtype=np.uint8)

im_sp.set_data(img * mask)
fig_sp.canvas.draw()

# -- grab a point off of the image using ginput
cpos, rpos = [int(round(i)) for i in fig_sp.ginput()[0]]

# -- set the mask pixels within some aperature to 1
rad  = 100
dist = np.sqrt((rind - rpos)**2 + (cind - cpos)**2)
mask[dist <= rad] = [1, 1, 1]

# -- redisplay the masked image
im_sp.set_data(img * mask)
fig_sp.canvas.draw()

# -- loop through clicks
rflag = True
while rflag:
    try:
        cpos, rpos = [int(round(i)) for i in fig_sp.ginput()[0]]
        dist = np.sqrt((rind - rpos)**2 + (cind - cpos)**2)
        mask[dist <= rad] = [1, 1, 1]
        im_sp.set_data(img * mask)
        fig_sp.canvas.draw()
    except:
        rflag = False

plt.close("all")




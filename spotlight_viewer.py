#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd

def spotlight(event):
    """
    Shine a spotlight on the image at the cursor position.
    """

    # -- reset the mask
    mask[...] = False

    # -- define spotlight radius
    rad = 100

    # -- get the cursor location and square distance
    rpos  = int(round(event.ydata))
    cpos  = int(round(event.xdata))
    dist2 = (rind - rpos)**2 + (cind - cpos)**2

    # -- open the spotlight
    mask[dist2 <= rad * rad] = [True, True, True]

    # -- reset the image data
    im0.set_data(img * mask)
    fig0.canvas.draw()

    return


if __name__ == "__main__":

    # -- read the image
    dpath = "images"
    fname = "city_image.jpg"
    img   = nd.imread(os.path.join(dpath, fname))
    nrow  = img.shape[0]
    ncol  = img.shape[1]
    
    # -- set the mask and indices
    rind = np.arange(nrow * ncol).reshape(nrow, ncol) // ncol
    cind = np.arange(nrow * ncol).reshape(nrow, ncol) % ncol
    mask = np.zeros(img.shape, dtype=bool)
    
    # -- display the image
    xs = 10.
    ys = xs * float(nrow) / float(ncol)
    fig0, ax0 = plt.subplots(num=0, figsize=(xs, ys))
    fig0.subplots_adjust(0, 0, 1, 1)
    ax0.axis("off")
    im0 = ax0.imshow(img * mask)
    fig0.canvas.draw()

    # -- connect to the spotlight function
    dum = fig0.canvas.mpl_connect("motion_notify_event", spotlight)

    # -- run the viewer
    plt.show()

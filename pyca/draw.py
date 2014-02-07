# pyca.draw
# Draws a frame or grid world
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Feb 07 15:12:47 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: draw.py [] benjamin@bengfort.com $

"""
Draws a frame or grid world
"""

##########################################################################
## Imports
##########################################################################

import matplotlib
matplotlib.use('TKAgg')    # This is a MacOSX fix

import matplotlib.cm as cm
import matplotlib.pyplot as plt

##########################################################################
## Drawing functions
##########################################################################

def draw_grid(grid, cmap=cm.gray_r, save=None):
    fig, axe = plt.subplots()
    axe.axis('off')
    mat = axe.matshow(grid, cmap=cmap)
    if save is None:
        plt.show()
    else:
        plt.savefig(save)

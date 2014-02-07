# pyca.square
# Generates a grid with a hollow square in it
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Feb 07 14:32:02 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: square.py [] benjamin@bengfort.com $

"""
Generates a grid with a hollow square in it
"""

##########################################################################
## Imports
##########################################################################

import numpy as np

##########################################################################
## Helper methods
##########################################################################

def odd_parity(bits):
    """
    Determines if the array has even or odd parity.
    Returns True if odd, False if even.

    Note: this is an extremely inefficient computation, fix later.
    """
    count = sum(1 for x in bits if x==1)
    return count % 2

def square_world(square=20, width=100, height=100):
    """
    Returns an array that is initiated with a hollow square in the middle.
    """
    grid = np.zeros(shape=(height, width))

    center = (height/2, width/2)
    topcrn = (center[0]-square/2, center[1]-square/2)
    btmcrn = (center[0]+square/2, center[1]+square/2)

    for i in xrange(square+1):
        for j in xrange(square+1):
            grid[topcrn[0], topcrn[1]+i] = 1
            grid[topcrn[0]+j, topcrn[1]] = 1
            grid[btmcrn[0], btmcrn[1]-i] = 1
            grid[btmcrn[0]-j, btmcrn[1]] = 1

    return grid

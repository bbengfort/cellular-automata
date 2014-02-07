# pyca.world
# Two dimensional Cellular Automata
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Feb 06 16:20:44 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: world.py [] benjamin@bengfort.com $

"""
Space animations for two dimensional cellular automata.
"""

##########################################################################
## Imports
##########################################################################

import numpy as np
from square import *

##########################################################################
## Automata
##########################################################################

class Automata(object):

    def __init__(self, width=100, height=100, randstart=True):
        self.width  = width
        self.height = height
        self.time   = 0
        self.init_world(randstart)

    @property
    def shape(self):
        return (self.height, self.width)

    def init_world(self, randstart=False):
        if randstart:
            self.world = np.random.choice((1,0), len(self), p=(0.2, 0.8)).reshape(self.shape)
        else:
            self.world = square_world(20, self.width, self.height)

        self.state = np.zeros(shape=self.shape)
        return self.world

    def neighborhood(self, idx, jdx):
        """
        Returns the neighborhood as an array
        """
        return [
            self.state[idx, jdx],
            self.state[(idx-1)%self.height,jdx],
            self.state[idx,(jdx+1)%self.width],
            self.state[(idx+1)%self.height, jdx],
            self.state[idx,(jdx-1)%self.width],
        ]

    def __len__(self):
        return self.width*self.height

    def __iter__(self):
        return self

    def __next__(self):
        self.time += 1

        # Halting condition
        if self.time >= self.height:
            raise StopIteration()

        # Save the current world state
        self.state = np.copy(self.world)
        for row in xrange(self.height):
            for col in xrange(self.width):
                if odd_parity(self.neighborhood(row, col)):
                    self.world[row, col] = 1
                else:
                    self.world[row, col] = 0

        return self.world
    next = __next__

if __name__ == '__main__':
    from animation import AutomataAnimation
    from draw import draw_grid
    automata  = Automata(width=100, height=100, randstart=False)
    #automata.next()
    animation = AutomataAnimation(automata, interval=300)
    #draw_grid(automata.world)
    #animation.show()
    animation.save('odd_parity.mp4')

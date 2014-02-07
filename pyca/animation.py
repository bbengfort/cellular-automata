# pyca.animation
# Wraps matplotlib to provide animation
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jan 31 09:41:31 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: animation.py [] benjamin@bengfort.com $

"""
Wraps matplotlib to provide animation
"""

##########################################################################
## Imports
##########################################################################

import matplotlib
matplotlib.use('TKAgg')    # This is a MacOSX fix

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

##########################################################################
## Module Constants
##########################################################################

ON   = 255.0
OFF  = 0.0
VALS = (ON, OFF)

##########################################################################
## Animation Wrappers
##########################################################################

class GridAnimation(object):
    """
    Handles the animation of a Grid using matshow.
    """

    def __init__(self, **kwargs):
        """
        Initialize the grid and any other required properties
        """
        # Gather Properties
        self.width    = kwargs.pop('width', 100)
        self.height   = kwargs.pop('height', 100)
        self.cmap     = kwargs.pop('cmap', cm.gray_r)
        self.frames   = kwargs.pop('frames', self.height-1)
        self.interval = kwargs.pop('interval', 60)
        self.repeat   = kwargs.pop('repeat', False)
        self.numsaves = kwargs.pop('save_count', 50)

        # Initialize Animation
        self.init_grid()
        self.init_plot()
        self.init_anim()

    def __call__(self, data):
        self.update(data)
        self.mat.set_data(self.grid)
        return self.mat

    def __len__(self):
        return self.width*self.height

    @property
    def shape(self):
        return (self.height, self.width)

    def init_grid(self):
        self.grid = np.zeros(shape=self.shape)
        return self.grid

    def init_plot(self):
        self.fig, self.axe = plt.subplots()
        self.axe.axis('off')

    def init_anim(self):
        self.mat = self.axe.matshow(self.grid, cmap=self.cmap)
        self.ani = animation.FuncAnimation(self.fig, self, frames=self.frames, interval=self.interval, repeat=self.repeat, save_count=self.numsaves)

    def update(self, data):
        """
        Subclasses are expected to call and update the grid.
        """
        raise NotImplementedError("Subclasses must implement.")

    def save(self, path):
        self.ani.save(path, writer='ffmpeg', fps=15)

    def show(self):
        plt.show()

##########################################################################
## Animation Wrapper for an Automata - animates the world.
##########################################################################

class AutomataAnimation(GridAnimation):

    def __init__(self, automata, **kwargs):
        self.automata    = automata
        kwargs['width']  = automata.width
        kwargs['height'] = automata.height
        super(AutomataAnimation, self).__init__(**kwargs)

    def init_grid(self):
        self.grid = self.automata.world
        return self.grid

    def update(self, data):
        try:
            self.automata.next()
        except StopIteration:
            pass
        return self.init_grid()

##########################################################################
## Random animation to test grid animation.
##########################################################################

class RandomGridAnimation(GridAnimation):

    def init_grid(self):
        self.grid = np.random.choice(VALS, len(self),
                        p=(0.2, 0.8)).reshape(self.shape)
        return self.grid

    def update(self, data):
        return self.init_grid()

if __name__ == '__main__':
    grid = RandomGridAnimation()
    grid.show()
    #grid.save('rule90.mp4')

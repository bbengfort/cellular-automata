# pyca.simple
# One dimensional Cellular Automata
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jan 31 10:49:41 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: simple.py [] benjamin@bengfort.com $

"""
Space-Time animation for one dimensional cellular automata.
"""

##########################################################################
## Imports
##########################################################################

import numpy as np

##########################################################################
## Automata
##########################################################################

class Automata(object):

    def __init__(self, rule, width=100, height=100, randstart=False):
        self.width  = width
        self.height = height
        self.rule   = rule
        self.time   = 0
        self.init_world(randstart)

    @property
    def rule(self):
        return self._rule

    @rule.setter
    def rule(self, rule):
        if isinstance(rule, basestring):
            rule = int(rule)
        if isinstance(rule, int):
            self._rule = [(rule/pow(2,i) % 2) for i in range(8)]
        else:
            self._rule = rule

    @property
    def shape(self):
        return (self.height, self.width)

    def init_world(self, randstart=False):
        self.world = np.zeros(shape=self.shape)
        if randstart:
            self.world[0] = np.random.choice((0,1), self.width, p=(0.2, 0.8))
        else:
            self.world[0,self.width/2] = 1

        return self.world

    def compute_states(self, state):
        N = self.width
        for j in range(N):
            left  = state[(j-1)%N]
            cell  = state[j]
            right = state[(j+1)%N]
            yield self.rule[int(4 * left + 2*cell + right )]

    def __len__(self):
        return self.width*self.height

    def __iter__(self):
        return self

    def __next__(self):

        # Get state at current time, then increment time
        state = self.world[self.time]
        self.time += 1

        # Halting condition
        if self.time >= self.height:
            raise StopIteration()

        # Calculate the world at this timestep
        self.world[self.time] = np.array(list(self.compute_states(state)))
        return self.world[self.time]
    next = __next__



if __name__ == '__main__':
    from animation import AutomataAnimation
    #automata  = Automata(110, width=1280, height=720, randstart=False)
    automata  = Automata(110, width=100, height=100, randstart=True)
    animation = AutomataAnimation(automata)
    animation.show()

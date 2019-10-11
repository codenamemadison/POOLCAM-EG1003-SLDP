# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:35:12 2019

@author: Kobe Minnick
"""

import numpy as np

def callPoints():
    """Collects the necessary points for the ball to travel)
    
    Returns:
        a - 3-dimensional numpy array
            cue point
            ball point
            hole point
    """
    cuepoint = (0.5,0.7)
    ballpoint = (1.0,2.0)
    holepoint = (1.37,2.75)
    return np.array([cuepoint,ballpoint,holepoint])


def hitPoint(hole,eight,radius):
    """Finds point cueball needs to hit in order to send eight ball to hole.
    
    Inputs
    ---------
    hole - 2D Numpy Array
    eight - 2D Numpy Array
    radius - float
    
    Returns
    ----------
    hitpoint - 2D numpy Array

    """
    holetoeight = hole - eight
    disthte = (holetoeight[0]**2+holetoeight[1]**2)**(0.5)
    similartriangle = disthte+radius
    scalefactor = similartriangle/disthte
    hitpoint = holetoeight*scalefactor
    return hole-hitpoint


a = callPoints()
print(hitPoint(a[2],a[1],0.05715))
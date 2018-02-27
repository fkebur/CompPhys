"""
This module implements the effective force model for the Lorenz equations
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.2"
__date__ ="Feb 24 2016"

from v3 import V3
import cpforces

class LorenzEffectiveForce(cpforces.BasicForce):
    """The effective force for the Lorenz equations"""
    def __init__(self, sigma, r, b):
        self.sigma = sigma
        self.r = r
        self.b = b
    def __call__(self, t, x, v):
        ax = self.sigma*(v.y - v.x)
        ay = -v.x*v.z + self.r*v.x - v.y
        az = v.x*v.y - self.b*v.z
        return V3(ax, ay, az)

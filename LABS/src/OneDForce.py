import cpforces
import numpy as np

class OneDForce(cpforces.BasicForce):
    "One dimensional force model"
    def __init__(self, springConstant, x0, p):
        self.springConstant = springConstant
        self.x0 = x0
        self.p  = p
    def __call__(self, t, x, v):
       return -self.springConstant*(abs(x)**(self.p-1))*(np.sign(x))


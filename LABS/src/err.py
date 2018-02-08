
def RelEneErr(self, springConstant, v, p, E):
    self.p = p
    self.E = E
    return ((v**2/2 + self.springConstant*(abs(x)**(self.p)/p) - E)/ E)

def AvgAbsErr(self, x, x1):
    self.x = x
    self.x1 = x1
    return (x1 - x)


import cpode

class RK2(cpode.OdeSolver):

    _name = "2nd order Runge-Kutta"

    def _setup(self):
        self._f = lambda t, x, v: (v, self.Force(t, x, v)/self.mass)
    def _step(self, dt, t, x, v):
        halfstep = dt/2.0
        k1x, k1v = self._f(t, x, v)
        k2x, k2v = self._f(t + halfstep, x + halfstep*k1x, v + halfstep*k1v)
        dx = k2x*dt
        dv = k2v*dt
        return dx, dv


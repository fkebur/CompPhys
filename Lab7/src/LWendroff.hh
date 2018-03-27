#ifndef LWENDROFF_HH_
#define LWENDROFF_HH_

//========================================================================
// LWendroff.hh
//
// Class for solving advection equation in 1-d using finite differences
//
// Constructor arguments are:
//   nSpatialPoints -- number of points in the spatial grid
//   c              -- wave speed
//   dt             -- time step
//   dx             -- space step
//   boundaryType   -- boundary condition type: 0 - fixed ends,
//                     1 - periodic boundary, 2 - free ends
//
//========================================================================

#include "CPInitialValueSolver.hh"

class LWendroff : public CPInitialValueSolver
{
public:
    LWendroff(unsigned nSpatialPoints, double c,
                         double dt, double dx, int boundaryType=1);
    inline virtual ~LWendroff() {}

private:
    const double c_;
    const double dt_;
    const double dx_;
    const int boundaryType_;

    virtual void propagate(double* next, const double** previous);
};

#endif // LWENDROFF_HH_

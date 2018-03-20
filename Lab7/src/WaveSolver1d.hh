#ifndef WAVESOLVER1D_HH_
#define WAVESOLVER1D_HH_

//========================================================================
// WaveSolver1d.hh
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

class WaveSolver1d : public CPInitialValueSolver
{
public:
    WaveSolver1d(unsigned nSpatialPoints, double c,
                         double dt, double dx, int boundaryType=1);
    inline virtual ~WaveSolver1d() {}

private:
    const double c_;
    const double dt_;
    const double dx_;
    const int boundaryType_;

    virtual void propagate(double* next, const double** previous);
};

#endif // WAVESOLVER1D_HH_

// SWIG interface file for the "SOR" class
%module SOR

// Include the .i file from the parent class
%include Arr2d.i

// Use of 2-d numpy arrays as arguments
%apply (double* IN_ARRAY2, int DIM1, int DIM2) {(const double* data, unsigned nrows, unsigned ncols)};

// Finally, wrap the SOR class
%{
#include "SOR.hh"
%}

%include "SOR.hh"

// Clear replacements of data, nrows, ncols.
// This can be useful if we have more files to wrap.
%clear (const double* data, unsigned nrows, unsigned ncols);

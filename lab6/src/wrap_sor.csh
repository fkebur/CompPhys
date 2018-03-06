swig -python -py3 -c++ SOR.i
set python_inc = /usr/local/anaconda3/include/python3.6m
set numpy_inc = `python3 -c "import numpy; print(numpy.get_include())"`
g++ -W -Wall -fPIC -O -c -I{$python_inc} -I{$numpy_inc} SOR.cc Arr2d.cc SOR_wrap.cxx
g++ -shared -o _SOR.so Arr2d.o SOR.o SOR_wrap.o

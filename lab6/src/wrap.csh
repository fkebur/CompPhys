swig -python -py3 -c++ Arr2d.i
set python_inc = /usr/local/anaconda3/include/python3.6m
set numpy_inc = `python3 -c "import numpy; print(numpy.get_include())"`
g++ -W -Wall -fPIC -O -c -I{$python_inc} -I{$numpy_inc} Arr2d.cc Arr2d_wrap.cxx
g++ -shared -o _Arr2d.so Arr2d.o Arr2d_wrap.o

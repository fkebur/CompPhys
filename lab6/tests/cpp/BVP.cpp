#include <iostream>
#include <fstream>
#include <math.h>
#include <cstdlib> 
#include <iomanip>
using namespace std;

// for rand() on archer. 
// for setw() in cout, using namespace std;

int main()
{
    int nmax=100;   // 100 x 100 grid
    double V[nmax][nmax];
    int niter=200;
    
    // set boundary condition
    for(int y=0; y<nmax; y++){
        for(int x=0; x<nmax; x++) {
            V[x][y]=0.0;
            if(x==0) V[x][y]=100.0; // 100 volts at x=0.
        }
    }
    
    for(int iter=0; iter<niter; iter++) {
    
    // loop over grid points except for boundaries...
    // x, y are integer index of grid point.
        
        for(int x=1; x<(nmax-1); x++) {
            for(int y=1; y<(nmax-1); y++) {
                V[x][y]=0.25*(V[x+1][y] + V[x-1][y] + V[x][y-1] + V[x][y+1]);
            } //endofyloop
        } //endofxloop
    } // end of iter loop
    
    ofstream outfile;
    outfile.open("potential.txt");
    for(int x=0; x<nmax; x++){
    for(int y=0; y<nmax; y++){
        outfile<<" "<<x<<" "<<y<<" "<<V[x][y]<<endl; }
    }
    
    outfile.close();
    return 0;
}


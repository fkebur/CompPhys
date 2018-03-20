
ofstream outfile;

outfile.open("potential.txt");

for(int x=0; x<nmax; x++){
for(int y=0; y<nmax; y++){
    outfile<<" "<<x<<" "<<y<<" "<<V[x][y]<<endl; }
}

outfile.close();
return 0;
}

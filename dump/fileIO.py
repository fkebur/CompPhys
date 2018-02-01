import numpy as np
import matplotlib.pyplot as plt

csv_file_name = "population.csv" 
data_set = np.loadtxt(csv_file_name, delimiter=',') 
print(data_set)


x = data_set[:,0]   # [:,0] selects the first column of a 2-d array. 
y = data_set[:,1]   # See the numpy tutorial for array indexing details. 
return figure()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

from Functions import read_SDRG    

# Open the file for reading
file_path = 'Data/SDRG.txt'  # Replace with the path to your file
Numerical_SRDG = read_SDRG(file_path)
# Calculate the sum of all elements
Numerical_SRDG = -3*Numerical_SRDG / (8*len(Numerical_SRDG))
# Create an array and fill it with the function values
position_array = np.arange(1, len(Numerical_SRDG) + 1)
result_array = -(1/4) * (1 / position_array**2)
# Print the result array
plt.scatter(position_array, Numerical_SRDG/result_array - 1, color="purple", s=4)
plt.plot(position_array, Numerical_SRDG/result_array - 1, linestyle='--', linewidth=0.5, color="purple")
plt.axhline(0, color="black", linestyle="--")
plt.ylabel(r"$\delta(l)$")
plt.xlabel("$l$")
plt.xscale('log')
plt.ylim(-1,1)
plt.savefig("./Images/SDRG_"+str(len(Numerical_SRDG))+".png", dpi=300, bbox_inches="tight")
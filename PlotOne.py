import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def read_parameters(file_path):
    parameters = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into key and value
            key, value = line.strip().split('=')
            # Remove leading/trailing whitespace
            key = key.strip()
            value = value.strip()
            # Store the parameters in a dictionary
            parameters[key] = value
    return parameters

# Read parameters 
file_path = sys.argv[1]
parameters = read_parameters("./Parameters/"+file_path)
J_min = parameters.get('J_min', None)
Model = parameters.get('distribution', None)
if Model == "1":
    distribution = "Box_Hamiltonian"
else:
    distribution = "Binary_Hamiltonian"
# Read correlation results
data_path = distribution+"-"+str(J_min)+".csv"
df = pd.read_csv("./Data/"+data_path)
R = df['R'].to_numpy()
C_zz = df['C_zz'].to_numpy()
C_xx = df['C_xx'].to_numpy()
Var_C_zz = df['Var_C_zz'].to_numpy()
Var_C_xx = df['Var_C_xx'].to_numpy()
SeriesZ = -R**2 * C_zz;         ErrorZ  = R**2 * np.sqrt(Var_C_zz)
SeriesX = R**2 * np.abs(C_xx);  ErrorX  = R**2 * np.sqrt(Var_C_xx)

# Plotting C_zz
plt.figure(figsize=(5, 5))
plt.scatter(R, SeriesZ, label="Box distribution, J_min = 0", color="blue", s=2.2)
plt.errorbar(R, SeriesZ, yerr=ErrorZ, fmt='o', color="blue", markersize=2.2, capsize=2)
plt.plot(R, SeriesZ, linestyle='--', linewidth=0.5, color='blue')
plt.axhline(1/np.pi**2, color="orange", linestyle="--", label="$1/π^2$")
plt.axhline(1/12, color="black", linestyle="--", label="1/12")
plt.xscale('log')
plt.xlabel("$l$")
plt.ylabel("$-l^2C_{zz}(l)$")
plt.ylim(0, 0.3)
plt.legend(loc="upper left")
plt.savefig("./Images/Czz"+distribution+"-"+str(J_min)+".png", dpi=300, bbox_inches="tight")

# Plotting C_xx
x = np.arange(1, 201, 2); f = lambda x: 0.14709 * x**(3/2); y = f(x) #Clean system
plt.figure(figsize=(5, 5))
plt.scatter(R, SeriesX, label="Box distribution, J_min = 0", color="blue", s=2.2)
plt.errorbar(R, SeriesX, yerr=ErrorX, fmt='o', color="blue", markersize=2.2, capsize=2)
plt.plot(R, SeriesX, linestyle='--', linewidth=0.5, color='blue')
plt.plot(x, y, label="Clean system", color="orange")
plt.axhline(1/12, color="black", linestyle="--", label="1/12")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$l$")
plt.ylabel("$l^2|C_{xx}(l)|$")
plt.ylim(0.05, 300)
plt.legend(loc="upper left")
plt.savefig("./Images/Cxx"+distribution+"-"+str(J_min)+".png", dpi=300, bbox_inches="tight")
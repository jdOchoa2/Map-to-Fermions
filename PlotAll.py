import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def read_parameters(n):
    file_path = sys.argv[n]
    parameters = {}
    with open("./Parameters/"+file_path, 'r') as file:
        for line in file:
            # Split the line into key and value
            key, value = line.strip().split('=')
            # Remove leading/trailing whitespace
            key = key.strip()
            value = value.strip()
            # Store the parameters in a dictionary
            parameters[key] = value
    J_min = parameters.get('J_min', None)
    Model = parameters.get('distribution', None)
    distribution = Which_Model(Model)
    return [J_min,distribution]

def read_correlation(J_min, distribution):
    data_path = distribution+"-"+str(J_min)+".csv"
    df = pd.read_csv("./Data/"+data_path)
    R = df['R'].to_numpy()
    C_zz = df['C_zz'].to_numpy()
    C_xx = df['C_xx'].to_numpy()
    Var_C_zz = df['Var_C_zz'].to_numpy()
    Var_C_xx = df['Var_C_xx'].to_numpy()
    C_xxpp = df['C_xxpp'].to_numpy()
    Var_C_xxpp = df['Var_C_xxpp'].to_numpy()
    return [-R**2 * C_zz,R**2 * np.sqrt(Var_C_zz),R**2 * np.abs(C_xx),R**2 * np.sqrt(Var_C_xx),np.abs(C_xx + C_xxpp),R]

def Which_Model(Model):
    if Model == "1":
        return "Box_Hamiltonian"
    else:
        return "Binary_Hamiltonian"

"""---------------MAIN-----------------"""

SeriesX = [None,None,None]; ErrorX = [None,None,None]; SeriesXpp = [None,None,None]
SeriesZ = [None,None,None]; ErrorZ = [None,None,None]

J_min = [None,None,None]  ; distribution = [None,None,None]; R = []

for n in range(3):
    J_min[n], distribution[n] = read_parameters(n+1)
    SeriesZ[n], ErrorZ[n], SeriesX[n], ErrorX[n], SeriesXpp[n], R = read_correlation(J_min[n], distribution[n])

# Plotting C_zz
plt.figure(figsize=(5, 5))
plt.scatter(R, SeriesZ[0], label=distribution[0]+"-$J_{min}=$"+str(J_min[0]), color="red", s=4)
plt.plot(R,    SeriesZ[0], linestyle='--', linewidth=0.5, color='red')
plt.scatter(R, SeriesZ[1], label=distribution[1]+"-$J_{min}=$"+str(J_min[1]), color="green", s=4)
plt.plot(R,    SeriesZ[1], linestyle='--', linewidth=0.5, color='green')
plt.scatter(R, SeriesZ[2], label=distribution[2]+"-$J_{min}=$"+str(J_min[2]), color="blue", s=4)
plt.plot(R,    SeriesZ[2], linestyle='--', linewidth=0.5, color='blue')
plt.axhline(1/np.pi**2, color="orange", linestyle="--", label="$1/π^2$")
plt.axhline(1/12, color="black", linestyle="--", label="1/12")
plt.xscale('log')
plt.xlabel("$l$")
plt.ylabel("$-l^2C_{zz}(l)$")
plt.ylim(0, 0.25)
plt.legend(loc="upper left")
plt.savefig("./Images/Czz.png", dpi=300, bbox_inches="tight")

# Plotting C_xx
x = np.arange(1, 201, 2); f = lambda x: 0.14709 * x**(3/2); y = f(x) #Clean system
plt.figure(figsize=(5, 5))
plt.scatter(R, SeriesX[0], label=distribution[0]+"-$J_{min}=$"+str(J_min[0]), color="red", s=4)
plt.plot(R,    SeriesX[0], linestyle='--', linewidth=0.5, color='red')
plt.scatter(R, SeriesX[1], label=distribution[1]+"-$J_{min}=$"+str(J_min[1]), color="green", s=4)
plt.plot(R,    SeriesX[1], linestyle='--', linewidth=0.5, color='green')
plt.scatter(R, SeriesX[2], label=distribution[2]+"-$J_{min}=$"+str(J_min[2]), color="blue", s=4)
plt.plot(R,    SeriesX[2], linestyle='--', linewidth=0.5, color='blue')
plt.plot(x, y, label="Clean system", color="orange")
plt.axhline(1/12, color="black", linestyle="--", label="1/12")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$l$")
plt.ylabel("$l^2|C_{xx}(l)|$")
plt.ylim(0.05, 300)
plt.legend(loc="upper left")
plt.savefig("./Images/Cxx.png", dpi=300, bbox_inches="tight")

#Plotting C_xx + C_xx+1
x = np.arange(1, 201, 2); f = lambda x: 1/(12*x**(2)); y = f(x) #Universallity prediction
plt.figure(figsize=(5, 5))
plt.scatter(R, SeriesXpp[0], label=distribution[0]+"-$J_{min}=$"+str(J_min[0]), color="red", s=4)
plt.plot(R,    SeriesXpp[0], linestyle='--', linewidth=0.5, color='red')
plt.scatter(R, SeriesXpp[1], label=distribution[1]+"-$J_{min}=$"+str(J_min[1]), color="green", s=4)
plt.plot(R,    SeriesXpp[1], linestyle='--', linewidth=0.5, color='green')
plt.scatter(R, SeriesXpp[2], label=distribution[2]+"-$J_{min}=$"+str(J_min[2]), color="blue", s=4)
plt.plot(R,    SeriesXpp[2], linestyle='--', linewidth=0.5, color='blue')
plt.plot(x, y, label="$1/(12l^2)$", color="orange")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$l$")
plt.ylabel("$|C_{xx}(l)+C_{xx}(l+1)|$")
plt.ylim(10e-8,.1)
plt.legend(loc="lower left")
plt.savefig("./Images/Cxxpp.png", dpi=300, bbox_inches="tight")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

from Functions import read_parameters, read_correlation, Which_Model

def read_pair(J_min, distribution):
    data_path = "Pair-"+distribution+"-"+str(J_min)+".csv"
    df = pd.read_csv("./Data/"+data_path)
    R = df['R'].to_numpy()
    Corr_z = df['Corr_z'].to_numpy()
    Corr_x = df['Corr_x'].to_numpy()
    return [Corr_z, Corr_x, R]

J_min, distribution = read_parameters(sys.argv[1])
Corr_z,Corr_x,R = read_pair(J_min, distribution)

# Plotting correlations
plt.figure(figsize=(5, 5))
plt.scatter(R, np.abs(Corr_z), label="C_{zz}", color="red", s=4)
plt.plot(R,    np.abs(Corr_z), linestyle='--', linewidth=0.5, color='red')
plt.scatter(R, np.abs(Corr_x), label="C_{xx}", color="black", s=4)
plt.plot(R,    np.abs(Corr_x), linestyle='--', linewidth=0.5, color='black')
plt.xlabel("$l$")
plt.legend(loc="upper left")
plt.savefig("./Images/Pair"+distribution+"-"+J_min+".png", dpi=300, bbox_inches="tight")
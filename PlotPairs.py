import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

from Functions import read_parameters, read_pair

J_min, distribution = read_parameters(sys.argv[1])
Corr_x_p, Corr_x, Corr_x_m, Corr_z_p, Corr_z, Corr_z_m, R = read_pair(J_min, distribution)

# Plotting correlations XX
plt.figure(figsize=(5, 5))
plt.scatter(R, np.abs(Corr_x_p), label="$S_{+1}$", color="blue", s=4)
plt.plot(R,    np.abs(Corr_x_p), linestyle='--', linewidth=0.5, color='blue')
plt.scatter(R, np.abs(Corr_x), label="$S_{0}$", color="black", s=4)
plt.plot(R,    np.abs(Corr_x), linestyle='--', linewidth=0.5, color='black')
plt.scatter(R, np.abs(Corr_x_m), label="$S_{-1}$", color="red", s=4)
plt.plot(R,    np.abs(Corr_x_m), linestyle='--', linewidth=0.5, color='red')
plt.xlabel("$j$")
plt.ylabel(r"$|\langle S_i^xS_j^x\rangle$|")
plt.ylim(0,0.13)
plt.xlim(0,125)
plt.legend(loc="upper left")
plt.savefig("./Images/XX"+distribution+"-"+J_min+".png", dpi=300, bbox_inches="tight")

# Plotting correlations ZZ
plt.figure(figsize=(5, 5))
plt.scatter(R, np.abs(Corr_z_p), label="$S_{+2}$", color="blue", s=4)
plt.plot(R,    np.abs(Corr_z_p), linestyle='--', linewidth=0.5, color='blue')
plt.scatter(R, np.abs(Corr_z), label="$S_{0}$", color="black", s=4)
plt.plot(R,    np.abs(Corr_z), linestyle='--', linewidth=0.5, color='black')
plt.scatter(R, np.abs(Corr_z_m), label="$S_{-2}$", color="red", s=4)
plt.plot(R,    np.abs(Corr_z_m), linestyle='--', linewidth=0.5, color='red')
plt.xlabel("$j$")
plt.ylabel(r"$|\langle S_i^zS_j^z\rangle|$")
plt.ylim(0,0.06)
plt.xlim(0,125)
plt.legend(loc="upper left")
plt.savefig("./Images/ZZ"+distribution+"-"+J_min+".png", dpi=300, bbox_inches="tight")
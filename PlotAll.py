import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

from Functions import read_parameters, read_correlation, Which_Model

"""---------------MAIN-----------------"""

SeriesX = [None,None,None]; SeriesZ = [None,None,None]; SeriesXpp = [None,None,None]
ErrorX  = [None,None,None];  ErrorZ = [None,None,None];  ErrorXpp = [None,None,None]

J_min = [None,None,None]  ; distribution = [None,None,None]; R = []

for n in range(3):
    J_min[n], distribution[n] = read_parameters(sys.argv[n+1])
    SeriesZ[n], ErrorZ[n], SeriesX[n], ErrorX[n], SeriesXpp[n], ErrorXpp[n], R = read_correlation(J_min[n], distribution[n])

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

# Plotting DesvEsta C_zz
plt.figure(figsize=(5, 1))
plt.scatter(R, ErrorZ[0], color="red", s=4)
plt.plot(R,    ErrorZ[0], linestyle='--', linewidth=0.5, color='red')
plt.scatter(R, ErrorZ[1], color="green", s=4)
plt.plot(R,    ErrorZ[1], linestyle='--', linewidth=0.5, color='green')
plt.scatter(R, ErrorZ[2], color="blue", s=4)
plt.plot(R,    ErrorZ[2], linestyle='--', linewidth=0.5, color='blue')
plt.xscale('log')
plt.xlabel("$l$")
plt.ylabel("$l^2\sigma$")
plt.savefig("./Images/Errorzz.png", dpi=300, bbox_inches="tight")

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

# Plotting DesvEsta C_xx
plt.figure(figsize=(5, 1))
plt.scatter(R, ErrorX[0], color="red", s=4)
plt.plot(R,    ErrorX[0], linestyle='--', linewidth=0.5, color='red')
plt.scatter(R, ErrorX[1], color="green", s=4)
plt.plot(R,    ErrorX[1], linestyle='--', linewidth=0.5, color='green')
plt.scatter(R, ErrorX[2], color="blue", s=4)
plt.plot(R,    ErrorX[2], linestyle='--', linewidth=0.5, color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$l$")
plt.ylabel("$l^2\sigma$")
plt.savefig("./Images/Errorxx.png", dpi=300, bbox_inches="tight")

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

# Plotting DesvEsta C_xx + C_xx+1
plt.figure(figsize=(5, 1))
plt.scatter(R, ErrorXpp[0], color="red", s=4)
plt.plot(R,    ErrorXpp[0], linestyle='--', linewidth=0.5, color='red')
plt.scatter(R, ErrorXpp[1], color="green", s=4)
plt.plot(R,    ErrorXpp[1], linestyle='--', linewidth=0.5, color='green')
plt.scatter(R, ErrorXpp[2], color="blue", s=4)
plt.plot(R,    ErrorXpp[2], linestyle='--', linewidth=0.5, color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$l$")
plt.ylabel("$\sigma$")
plt.savefig("./Images/Errorxxpp.png", dpi=300, bbox_inches="tight")
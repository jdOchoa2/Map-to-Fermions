# Mapping to Free Fermions
This repository contains code to solve a spin-1/2 random antiferromagnetic XX chains using mapping to free fermions and exact diagonalization.

## Running the simulation

To run the main part of the code, specify the number of processess to be used and the file which contains the parameters of the chain:

```bash
mpiexecjl -n ${proccesses} julia main.jl ${Parameters}
```
This will produce .csv files with the disorder-averaged correlation functions.

## Plotting

To reproduce the three curves, run the following with the correct parameter files:

```bash
python3 PlotAll.py ${Parameters_1} ${Parameters_2} ${Parameters_3}
```

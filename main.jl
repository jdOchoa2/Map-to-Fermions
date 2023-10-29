
using Pkg
Pkg.activate("./demo/Project.toml");

include("./Functions.jl")
using CSV, DataFrames
using LinearAlgebra
using Random

#Read parameters
file_path = "./Parameters/"*ARGS[1]
parameters = read_parameters(file_path)
N       = get(parameters, "N", nothing)
J_min   = get(parameters, "J_min", nothing)
Omega   = get(parameters, "Omega", nothing)
samples = get(parameters, "samples", nothing)
ID      = get(parameters, "distribution", nothing)
seed    = get(parameters, "seed", nothing)
if ID == 1
    distribution = Box_Hamiltonian
else
    distribution = Binary_Hamiltonian
end
#Set random seed for reproducibility 
Random.seed!(seed)
#Define domain of separation lengths
R = vcat([r for r in 1:2:10],[trunc(Int,10^r) + (trunc(Int,10^r)+ 1) %2  for r in 1:0.06:2.3]); Domain = length(R)
#Find correlation functions
C_zz, C_xx, Var_C_zz, Var_C_xx = Correlation_Function(R, Domain, N, samples, distribution, J_min, Omega)
# Save data to csv file
file_path = "./Data/"*string(distribution)*"-"*string(J_min)*".csv"
Data = hcat(R,C_zz, C_xx, Var_C_zz, Var_C_xx)
CSV.write(file_path, DataFrame(Data, ["R","C_zz","C_xx","Var_C_zz","Var_C_xx"]))

println("Data saved as $file_path\n")
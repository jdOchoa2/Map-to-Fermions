using Pkg
Pkg.activate("./demo/Project.toml");

include("./Functions.jl")
using CSV, DataFrames
using LinearAlgebra
using Random

#Read parameters
file_path = "./Parameters/"*ARGS[1]
parameters = read_parameters(file_path)
N = Int(get(parameters, "N", nothing))
J_min = get(parameters, "J_min", nothing)
Omega = get(parameters, "Omega", nothing)
samples = Int(get(parameters, "samples", nothing))
ID = Int(get(parameters, "distribution", nothing))
seed = Int(get(parameters, "seed", nothing))
if ID == 1
    distribution = Box_Hamiltonian
else
    distribution = Binary_Hamiltonian
end   
Random.seed!(seed)    
N = 1000            
#Pair correlations
H = Hamiltonian(N,distribution,J_min,Omega)
U = eigen(H).vectors
Corr_Matrix = Correlation_Matrix(U,N)
R = [r for r in 1:N-1]; Domain = length(R)
Corr_z = zeros(Float64, Domain, 1); Corr_x = zeros(Float64, Domain, 1)
i = rand(1:Domain)
for r in 1:Domain
    Corr_z[r] = Pair_Longitudinal_Correlation(i,r,N,Corr_Matrix)
    Corr_x[r] = Pair_Transverse_Correlation(i,r,N,Corr_Matrix)
end
# Save data to csv file
file_path = "./Data/Pair-"*string(distribution)*"-"*string(J_min)*".csv"
Data = hcat(R,Corr_z,Corr_x)
CSV.write(file_path, DataFrame(Data, ["R","Corr_z","Corr_x"]))
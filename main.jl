
using Pkg
Pkg.activate("./demo/Project.toml");

include("./Functions.jl")
using CSV, DataFrames
using LinearAlgebra
using Random
using MPI

#Initialize MPI
MPI.Init()
const comm = MPI.COMM_WORLD
const root = 0
#Read parameters
if MPI.Comm_rank(comm) == root
    file_path = "./Parameters/"*ARGS[1]
    parameters = read_parameters(file_path)
    Get_Parameters = [get(parameters, "N", nothing),get(parameters, "J_min", nothing),get(parameters, "Omega", nothing),
            get(parameters, "samples", nothing),get(parameters, "distribution", nothing),get(parameters, "seed", nothing)]
else
    Get_Parameters = nothing
end
Get_Parameters = MPI.bcast(Get_Parameters, root, comm)
N = Int(Get_Parameters[1]); J_min = Get_Parameters[2]; Omega = Get_Parameters[3]
samples = Int(Get_Parameters[4])÷MPI.Comm_size(comm); ID = Int(Get_Parameters[5]); seed = Int(Get_Parameters[6])
if ID == 1
    distribution = Box_Hamiltonian
else
    distribution = Binary_Hamiltonian
end
#Set random seed for reproducibility (if same number of proccesses)
Random.seed!(seed*MPI.Comm_rank(comm))
#Define domain of separation lengths
R = vcat([r for r in 1:2:10],[trunc(Int,10^r) + (trunc(Int,10^r)+ 1) %2  for r in 1.06:0.06:2.3]); Domain = length(R); Rpp = R .+ 1
print(Rpp)
"""
#Find correlation functions
c_zz, c_xx, c_zz_2, c_xx_2, c_xxpp, c_xxpp_2 = Correlation_Function(R, Rpp, Domain, N, samples, distribution, J_min, Omega)
Summary = vcat(c_zz, c_xx, c_zz_2, c_xx_2, c_xxpp, c_xxpp_2); T_samples = samples*MPI.Comm_size(comm)
recAll = MPI.Reduce(Summary, Add, root, comm)
if MPI.Comm_rank(comm) == root
    #Average over all samples
    print("\nThe total number of samples was ", T_samples,"\n"); recAll /= T_samples
    C_zz = recAll[1:Domain]; C_xx = recAll[Domain+1:2*Domain]; C_xxpp =  recAll[4*Domain+1:5*Domain]
    Var_C_zz = recAll[2*Domain+1:3*Domain] - C_zz.^2; Var_C_xx = recAll[3*Domain+1:4*Domain] - C_xx.^2
    Var_C_xxpp =  recAll[5*Domain+1:6*Domain] - C_xxpp.^2
    # Save data to csv file
    file_path = "./Data/"*string(distribution)*"-"*string(J_min)*".csv"
    Data = hcat(R,C_zz, C_xx, Var_C_zz, Var_C_xx, C_xxpp, Var_C_xxpp)
    CSV.write(file_path, DataFrame(Data, ["R","C_zz","C_xx","Var_C_zz","Var_C_xx","C_xxpp","Var_C_xxpp"]))
end"""
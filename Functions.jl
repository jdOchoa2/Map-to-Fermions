"""Dioganilazation of free fermion's hamiltonian for finding 
correlation functions in a random antiferromagnetic spin chain"""

function Hamiltonian(N,distribution,J_min,Omega)
    """Returns the hamiltonian of the system as a NxN matrix 
    with coupling constants according to given distribution"""
    couplings = distribution(N,J_min,Omega)
    H = zeros(Float64, N, N)
    for ii in 1:N-1
        H[ii,ii+1] = couplings[ii]; H[ii+1,ii] = couplings[ii]
    end
    H[1,N] = (-1)^(N+1)*couplings[N]; H[N,1] = (-1)^(N+1)*couplings[N]
    return H
end

function Box_Hamiltonian(N,J_min,Omega)
    """Coupling Box Distribution with two parameters"""
    return [rand() * (Omega - J_min) + J_min for ii in 1:N]
end

function Binary_Hamiltonian(N,J_min,Omega)
    """Coupling Binary Distribution with two parameters"""
    return [rand([J_min, Omega]) for ii in 1:N]
end

function Delta(x)
    """Dirac delta function"""
    if abs(x) < 1e-15
        return 1
    else 
        return 0
    end
end

function Correlation_Fermion(i,j,U,N)
    """Expectetion value of fermion operators up to Fermi level"""
    C = 0.; k_F = Integer(N/2)
    for k in 1:k_F
        C += U[i,k]*U[j,k]
    end
    return C
end
        
function Correlation_Element(i,j,U)
    """Wicks theorem's elements"""
    return Delta(i-j) - 2*Correlation_Fermion(i,j,U,N)
end

function Correlation_Matrix(U,N)
    """Wicks theorem's matrix"""
    Corr_Matrix = zeros(Float64,N,N)
    for i in 1:N
        for j in 1:i
            Symm_ij =  Correlation_Element(i,j,U)
            Corr_Matrix[i,j] = Symm_ij
            Corr_Matrix[j,i] = Symm_ij
        end
    end
    return Corr_Matrix
end

function Longitudinal_Correlation(r,N,Corr_Matrix)
    """Correlation function along Z spin direction"""
    Corr_z = 0.
    for i in 1:N
        j = (i+r-1)%N+1 
        Corr_z += Corr_Matrix[j,j]*Corr_Matrix[i,i] - Corr_Matrix[i,j]^2
    end
    return Corr_z/(4*N)
end

function Transversal_Correlation(r,N,Corr_Matrix)
    """Correlation function along X spin direction"""
    Corr_x = 0.
    A = zeros(Float64, r, r)
    for i in 1:N
        for column in 1:r
            for row in 1:r
                ii = (i+column-1)%N+1%N; jj = (i+row-2)%N+1%N
                A[column,row] = Corr_Matrix[ii,jj]
            end
        end
        Corr_x += det(A)
    end
    return -1^r*Corr_x/(4*N)
end

function Correlation_Function(R, Domain, N, samples, distribution, J_min, Omega=1)
    """Finds the average of the correlation function for a separation length domain
    R, averaging over a given number of samples in a spin chain of length N"""
    C_zz = zeros(Float64, Domain, 1); C_xx = zeros(Float64, Domain, 1)
    C_zz_2 = zeros(Float64, Domain, 1); C_xx_2 = zeros(Float64, Domain, 1)
    for t in 1:samples
        H = Hamiltonian(N,distribution,J_min,Omega)
        U = eigen(H).vectors
        Corr_Matrix = Correlation_Matrix(U,N)
        for r in 1:Domain
            Z = Longitudinal_Correlation(R[r],N,Corr_Matrix) 
            X = Transversal_Correlation(R[r],N,Corr_Matrix)
            C_zz[r] += Z
            C_xx[r] += X
            C_zz_2[r] += Z.^2
            C_xx_2[r] += X.^2
        end
    end
    C_zz /= samples; C_xx /= samples; C_zz_2 /= samples; C_xx_2 /= samples
    return C_zz, C_xx, C_zz_2 - C_zz.^2, C_xx_2 - C_xx.^2
end

function read_parameters(file_path)
    """Reads parameters given the file name"""
    parameters = Dict{String, Any}()
    open(file_path, "r") do file
        for line in eachline(file)
            # Split the line into key and value
            key, value = split(line, "=")
            # Remove leading/trailing whitespaces
            key = strip(key)
            value = strip(value)         
            # Check if the value is an integer or float
            if occursin(".", value)
                value = parse(Float64, value)
            else
                value = parse(Int, value)
            end
            # Store the parsed values in the dictionary
            parameters[key] = value
        end
    end
    return parameters
end
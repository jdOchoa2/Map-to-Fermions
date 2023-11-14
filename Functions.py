import pandas as pd
import numpy as np

def read_parameters(file_path):
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
    return [-R**2 * C_zz,R**2 * np.sqrt(Var_C_zz),R**2 * np.abs(C_xx),
            R**2 * np.sqrt(Var_C_xx), (R+1)**2 * np.abs(C_xxpp), (R+1)**2 * np.sqrt(Var_C_xxpp), np.abs(C_xx + C_xxpp), np.sqrt(Var_C_xxpp)+np.sqrt(Var_C_xx), R]

def read_pair(J_min, distribution):
    data_path = "Pair-"+distribution+"-"+str(J_min)+".csv"
    df = pd.read_csv("./Data/"+data_path)
    R = df['R'].to_numpy()
    Corr_x_p = df['Corr_x_p'].to_numpy()
    Corr_x = df['Corr_x'].to_numpy()
    Corr_x_m = df['Corr_x_m'].to_numpy()
    Corr_z_p = df['Corr_z_p'].to_numpy()
    Corr_z = df['Corr_z'].to_numpy()
    Corr_z_m = df['Corr_z_m'].to_numpy()
    return [Corr_x_p, Corr_x, Corr_x_m, Corr_z_p, Corr_z, Corr_z_m, R]

def Which_Model(Model):
    if Model == "1":
        return "Box_Hamiltonian"
    else:
        return "Binary_Hamiltonian"
    
def read_SDRG(file_path):
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Split the content into a list of strings
        numbers_as_strings = content.split()
        # Convert each string to an integer
        numbers = [int(num) for num in numbers_as_strings]
        # Print the list of integers
        return np.array(numbers)
#include <iostream>
#include <random>
#include <vector>
#include <algorithm>
#include <fstream>

int main() {
    //--------------------------------Create Hamiltonian-----------------------------------//
    //std::seed_seq seed{42};
    //std::mt19937 gen(seed);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> uniform_distribution(0.5, 1.0);
    const int No = 2e6+1;
    int N = 2e6+1;
    std::vector<double> Hamiltonian;
    std::vector<int> Lengths;
    std::vector<int> Distribution(N/2+1, 0);
    Hamiltonian.reserve(N);
    Lengths.reserve(N);
    
    for (int i = 0; i < N; ++i) {
        double randomValue = uniform_distribution(gen);
        Hamiltonian.push_back(randomValue);
        Lengths.push_back(1);
    }
    //-----------------------------------SDRG Main loop-----------------------------------//
    for(int i = 0; i<No/2;++i){
        auto maxElement = std::max_element(Hamiltonian.begin(), Hamiltonian.end());
        int maxIndex = std::distance(Hamiltonian.begin(), maxElement);
        Distribution[(Lengths[maxIndex]-1)/2] += 1;
        Lengths[(maxIndex-1+N)%N] +=  Lengths[maxIndex] + Lengths[(maxIndex+1)%N];
        Hamiltonian[(maxIndex-1+N)%N] =  Hamiltonian[(maxIndex-1+N)%N]*Hamiltonian[(maxIndex+1)%N];
        // Remove the greatest element from the vector
        Hamiltonian.erase(Hamiltonian.begin() + maxIndex); 
        Lengths.erase(Lengths.begin() + maxIndex); 
        N -= 1;
        Hamiltonian.erase(Hamiltonian.begin() + (maxIndex)%N);
        Lengths.erase(Lengths.begin() + (maxIndex)%N); 
        N -= 1;
        if (i % 1000 == 0) {
            std::cout << "Progress: " << i << std::endl;
        }
    }
    Distribution[(Lengths[0]-1)/2] += 1;
    //-----------------------------------Save to file-----------------------------------//
    std::ofstream outputFile("Data/SDRG.txt");
    if (outputFile.is_open()) {
        for (const int& value : Distribution) {
            outputFile << value << " ";
        }
        // Close the file
        outputFile.close();
        std::cout << "Distribution has been saved to 'SDRG.txt'" << std::endl;
    } else {
        std::cerr << "Error opening the file." << std::endl;
    }
    return 0;
}


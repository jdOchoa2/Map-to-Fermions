Parameters_1 = "Box0.txt"
Parameters_2 = "Box4.txt"
Parameters_3 = "Bin10.txt"
proccesses   = 8 

all: MapToFermions

MapToFermions: main.jl Functions.jl PlotAll.py Functions.py
	mpiexecjl -n ${proccesses} julia main.jl ${Parameters_1};\
	mpiexecjl -n ${proccesses} julia main.jl ${Parameters_2};\
	mpiexecjl -n ${proccesses} julia main.jl ${Parameters_3};\
	python3 PlotAll.py ${Parameters_1} ${Parameters_2} ${Parameters_3}

PairCorrelations: Pair.jl PlotPairs.py Functions.py
	julia Pair.jl ${Parameters_1};\
	python3 PlotPairs.py ${Parameters_1}

clean_Images:
	find ./Images -type f -name "*.png" -exec rm -f {} \;

clean_Data:
	find ./Data -type f -name "*.csv" -exec rm -f {} \;

Parameters_1 = "Box0.txt"
Parameters_2 = "Box4.txt"
Parameters_3 = "Bin10.txt"
proccesses   = 2

all: MapToFermions

MapToFermions: main.jl Functions.jl PlotOne.py
	mpiexecjl -n ${proccesses} julia main.jl ${Parameters_1};\
	mpiexecjl -n ${proccesses} julia main.jl ${Parameters_2};\
	mpiexecjl -n ${proccesses} julia main.jl ${Parameters_3};\
	python3 PlotOne.py ${Parameters_1};\
	python3 PlotOne.py ${Parameters_2};\
	python3 PlotOne.py ${Parameters_3};\

clean_Images:
	find ./Images -type f -name "*.png" -exec rm -f {} \;

clean_Data:
	find ./Data -type f -name "*.csv" -exec rm -f {} \;

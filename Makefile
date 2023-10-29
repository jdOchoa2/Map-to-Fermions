Parameters_1 = "Box4.txt"

all: MapToFermions

MapToFermions: main.jl Functions.jl PlotOne.py
	JULIA $< ${Parameters_1};\
	python3 PlotOne.py ${Parameters_1}

clean_Images:
	find ./Images -type f -name "*.png" -exec rm -f {} \;

clean_Data:
	find ./Data -type f -name "*.csv" -exec rm -f {} \;

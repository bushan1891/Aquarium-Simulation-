CS558 FALL 2015: COMPUTER SIMULATION:
Assignment 2 :
Done By :  Saurabh Goyal  , Nagendra Bushan

Aquarium:

System of Differential equation is solved in Python using Simpy and Numpy libraries:

The differential equations are:

dm/dt	=	2m - ams, m(0)	=	m0
ds/dt	=	-s + ams, s(0)	=	s0


1)These equations are solved in file shark_mackerel_solver.py, if you run this file it will generate three files:

shark_mackerel_case1.txt
shark_mackerel_case2.txt
shark_mackerel_case3.txt

these three files contains the data of population of shark(s) and mackerel(m) from time 0 to 60 minutes:
shark_mackerel_case1.txt : contains the case where m0 = 300 and s0 = 150
shark_mackerel_case2.txt : contains the case where m0 = 15 and s0 = 22
shark_mackerel_case3.txt : contains the case where m0 = s0

2)The file shark_mackerel_plot plots the value contained in the three text files, it will generate three graphs

CASE1.png
CASE2.png
CASE3.png

There are the three graphs for three cases.

3)The file data_caculator calculates the metrics data that is the average/max/min life of a	mackerel,average/max/min
life of a shark,average/max/min	interval between fish eaten	by a shark and save it to file

Data_Metrics.txt








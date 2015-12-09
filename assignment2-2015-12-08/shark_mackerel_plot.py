
from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
plt.ion()
# Ploting the graph for case 1

t0,m0,s0 = loadtxt('shark_mackerel_case1.txt', unpack = True )

plt.figure()
plt.plot(t0, m0, label='MACKEREL')
plt.plot(t0, s0, label='SHARK')
plt.xlabel('TIME')
plt.ylabel('POPULATION')
plt.title('M0 = 300 , S0 = 150')
plt.legend(loc=0)
savefig('CASE1.png', dpi=100)


# ploting the graph for case 2

t1,m1,s1 = loadtxt('shark_mackerel_case2.txt', unpack = True )

plt.figure()
plt.plot(t1, m1, label='MACKEREL')
plt.plot(t1, s1, label='SHARK')
plt.xlabel('TIME')
plt.ylabel('POPULATION')
plt.title('M0 = 15 , S0 = 22')
plt.legend(loc=0)
savefig('CASE2.png', dpi=100)


# ploting the graph for case 3

t2,m2,s2 = loadtxt('shark_mackerel_case3.txt', unpack = True )

plt.figure()
plt.plot(t2, m2, label='MACKEREL')
plt.plot(t2, s2, label='SHARK')
plt.xlabel('TIME')
plt.ylabel('POPULATION')
plt.title('M0 =  S0')
plt.legend(loc=0)
savefig('CASE3.png', dpi=100)
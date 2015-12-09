from scipy.integrate import odeint
from pylab import *
from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from matplotlib.font_manager import FontProperties



# Defining a Vector Field for two diffrential equations for Mackerel and Shark
def vectorfield(w, t, p):

 m, s = w
 a = p
 f = [2*m - a*m*s, a*m*s - s]

 return f

# Case 1 where Mackerel = 300 and Sharks = 150

# Opening a text file for saving the results for case 1

f0 = open('shark_mackerel_case1.txt', 'w')

# Initial conditions

a = 0.01
m = 300
s = 150

# ODE solver parameters


t  = np.linspace(0, 60, 1000)

# Pack up the parameters and initial conditions:

w0 = [m,s]

# Call the ODE solver.

wsol = odeint(vectorfield, w0, t,args=(a,))


# Print the solution.

print  "TIME" , "MACKEREL" , "SHARK"

for t1, w1 in zip(t, wsol):
   print t1, w1[0], w1[1]
   print >> f0, t1, w1[0], w1[1]




# Closing the file

f0.close

# Case 2 where Mackerel = 15 and Sharks = 22

# Opening a text file for saving the results for case 2

f1 = open('shark_mackerel_case2.txt', 'w')

# Initial conditions

a = 0.01
m = 15
s = 22

# ODE solver parameters

t  = np.linspace(0, 5, 1000)

# Pack up the parameters and initial conditions:

w0 = [m,s]

# Call the ODE solver.

wsol = odeint(vectorfield, w0, t,args=(a,))


# Print the solution.

print  "TIME" , "MACKEREL" , "SHARK"

for t1, w1 in zip(t, wsol):
   print t1, w1[0], w1[1]
   print >> f1, t1, w1[0], w1[1]

# Closing the file

f1.close


# Case 3 where Mackerel =  Sharks

# Opening a text file for saving the results for case 3

f2 = open('shark_mackerel_case3.txt', 'w')

# Initial conditions

a = 0.01
m = s = 20

# ODE solver parameters

t  = np.linspace(0, 60, 1000)

# Pack up the parameters and initial conditions:

w0 = [m,s]

# Call the ODE solver.

wsol = odeint(vectorfield, w0, t,args=(a,))


# Print the solution.

print  "TIME" , "MACKEREL" , "SHARK"

for t1, w1 in zip(t, wsol):
   print t1, w1[0], w1[1]
   print >> f2, t1, w1[0], w1[1]

# Closing the file

f2.close




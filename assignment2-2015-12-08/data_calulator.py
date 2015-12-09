from numpy import loadtxt

# Taking data from case1 text file

t0,m0,s0 = loadtxt('shark_mackerel_case1.txt', unpack = True )

# for average of mackerel
for i in t0,m0:
    sum = (m0[i] - m0[i+1])/t0[i]
    print sum

# for max and min of mackerel

sum.sort()

for i in sum:
    print sum[1]
    print sum[1000]

# for average of shark
for i in t0,s0:
    sum0 = (s0[i] - s0[i+1])/t0[i]
    print sum0

# for max and min of shark

sum0.sort()

for i in sum0:
    print sum0[1]
    print sum0[1000]

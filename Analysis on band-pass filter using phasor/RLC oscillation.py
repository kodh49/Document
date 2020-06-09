import numpy as np
from math import *
import matplotlib.pyplot as plt

# variable definition
L = 0.012
C = 1.6
R = 1.5
w = sqrt((1/sqrt(L*C))**2-pow((R/2*L), 2))

# Function definition
def getQ(L, C, R, w, t) :
    Q = 100*exp(-R*t/(2*L))*cos(w*t)
    return Q

# create list
t = np.linspace(0, 100, 11)
q = []
for x in t:
    q.append(getQ(L, C, R, w, x))

plt.plot(q, t)
plt.show()
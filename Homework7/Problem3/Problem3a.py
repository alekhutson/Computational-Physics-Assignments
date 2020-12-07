import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint 

def diffequ(x, t, E):
    return np.array([x[1], -E*x[0]])

def diffequ2(x, t, EpdE):
    return np.array([x[1], -EpdE*x[0]])


E = 0.01 #initializes energy
dE = 0.000001 #sets energy step
y0 = [0,1] #Sets inital conditions of system
bE = 1 #initializes bE
t = np.linspace(0, np.pi + (np.pi/1000000), 1000000) #sets the time interval and delta t

while bE > .0000001:
    sol = odeint(diffequ, y0, t, args=(E,)) #solves the differintial equation using rk4
    bE = sol[999999][1] #the value of x at time = pi

    EpdE = E + dE

    sol = odeint(diffequ2, y0, t, args=(EpdE,)) #solves the differintial equation using rk4
    bEpdE = sol[999999][1] #the value of x at time = pi

    bprime = (bEpdE - bE)/dE #defines bprime

    E = E - (bE/bprime) #updates value of E

print(E)
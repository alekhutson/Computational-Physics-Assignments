import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.fft import fft
import pandas as pd

df1 = pd.read_csv (r'C:\Users\alekh\projects\computationalphysics\Midterm\Problem3\data.csv', header=None) #imports file

x=df1.loc[0].values #puts data into an array
fx = fft(x) #computes the fast fourier transform

T=1 #defines the period overwhich to plot
dt=0.001 #time step

npoints=int(T/dt)
tvals=np.linspace(0,T,npoints) #defines the y axis of the plot

S = len(tvals) - len(x)
tvalsC = tvals[: len(tvals)-S] #ensures the length of arrays are the same

plt.plot(tvalsC,x) #plots the x data 
plt.show()

mag=np.abs(fx) #plots the power spectrum of x
plt.plot(mag)

plt.savefig('PSx.png')
plt.show()



m = len(x)
y = []
for i in range(m-1): #computes the y array
    if i == m-1: #defines the periodic boundary conditions
        z=x[0]
        y.append(z)
    else:
        z  = (x[i] - x[i+1])/2
        y.append(z)
fy = fft(y) #fft of y values

K = len(tvals) - len(y) #ensures length of arrays are the same
tvalsK = tvals[: len(tvals)-K]

plt.plot(tvalsK,y) #plots the y data
plt.show()

mag=np.abs(fy) #plots power spectrum of y
plt.plot(mag)

plt.savefig('PSy.png')
plt.show()

#The power spectrum of the averaging procedure has lower peaks for low frequencies. 
#Therefore this averaging procedure is removing elemements of the signal associated with lower frequancies.
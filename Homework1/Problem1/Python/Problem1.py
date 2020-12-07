import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt

pfile=open('errorspython.txt','w') #opens a txt file for error values
hfile=open('hvaluespython.txt','w') #opens a txt file for h values

def function(t):
    return 1/(1+9*np.exp(-t))
    #defines the function

def derivative_of_function(t):
    return 9*np.exp(-t)*function(t)**2
    #defines the functions derivative

t=2 #time

for iter in range(21): #defines y values
    h=10**(-iter)
    e=abs(derivative_of_function(t) - (1/h)*(function(t+h)-function(t)))

    if iter==0:
        pfile.write(str(e))

    if iter>0:
        pfile.write(","+str(e))

    
for niter in range(21): #defines x values
    m=10**(-niter)

    if niter==0:
        hfile.write(str(m))

    if niter>0:
        hfile.write(","+str(m))

pfile.close()
hfile.close()

edata=np.genfromtxt('errorspython.txt',delimiter=',')
hdata=np.genfromtxt('hvaluespython.txt',delimiter=',')

plt.scatter(hdata,edata)
plt.plot(hdata,edata)

ax=plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('delta t')
ax.set_ylabel('absolute error')
ax.set_title('Absolute Error Plot')

plt.show();
#show the plot
plt.savefig('pythonplot.eps', format='eps')
#save the figure.



plt.cla(); 
#this clears all data in the previous plot. 






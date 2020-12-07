import numpy as np

import matplotlib as mp
import matplotlib.pyplot as plt


xpdata=np.genfromtxt('xp_values_2.00.txt',delimiter=',')
xdata=np.genfromtxt('x_values_2.00.txt',delimiter=',')

ypdata=np.genfromtxt('xp_values_2.99.txt',delimiter=',')
ydata=np.genfromtxt('x_values_2.99.txt',delimiter=',')
## This uses numpy to import the data.

#fig, ax = plt.subplots()

plt.plot(xdata,xpdata,color='b',marker='o')
plt.plot(ydata,ypdata,color='g',marker='o')


plt.text(.15, .4, 'r=2.00') 
plt.text(.6, .4, 'r=2.99')
#lables plots for each value of r

ax=plt.gca()
ax.set_xlabel('xn')
ax.set_ylabel('xn+1')
ax.set_title('logistic_map')
#lables graph and axis

plt.show()
#show the plot
plt.savefig('logistic_map.eps', format='eps')
#save the figure.

plt.cla()
#this clears all data in the previous plot.  

#the plot shows that for r=2.00 the fixed point is immediatly reached
#however, for r=2.99 the map oscillates around the fixed point
#it seems to me that 50 iterations is not enogh to really settle on the fixed point for r=2.99

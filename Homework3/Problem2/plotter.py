import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

x,y= np.loadtxt('g1.txt', delimiter=',', unpack=True)
k,h= np.loadtxt('g2.txt', delimiter=',', unpack=True)

fig,(a1)=plt.subplots(1)

a1.set_xscale('log')
a1.set_yscale('log')

a1.plot(x,y,color='r',label='g1')
a1.plot(k,h,color='k',label='g2')


ax1=a1.axes

a1.legend(loc='lower left')
a1.set_xlabel('dt')
a1.set_ylabel('g')
plt.tight_layout()
plt.savefig('g_figure.png')
plt.show()	

#In the figure it looks like g2 and g1 have the largest diffrence when
#dt is equal to .1 and .001
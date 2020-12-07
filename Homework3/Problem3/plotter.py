import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

x,y= np.loadtxt('RK_cpp_d.txt', delimiter=',', unpack=True)
k,h= np.loadtxt('actual_solution.txt', delimiter=',', unpack=True)

fig,(a1)=plt.subplots(1)

a1.plot(x,y,color='r',label='RK4 solution')
#a1.plot(k,h,color='k',label='actual solution')


ax1=a1.axes

a1.legend(loc='lower left')
a1.set_xlabel('z')
a1.set_ylabel('omega')
plt.tight_layout()
plt.savefig('figure_d.png')
plt.show()	
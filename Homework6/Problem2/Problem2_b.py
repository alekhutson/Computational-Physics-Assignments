import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
import matplotlib.ticker as ticker

# Set maximum iteration
maxIter = 500

# Set Dimension and delta
lenX = lenY = 20 #we set it rectangular
delta = 1

# Boundary conditions
Phitop = 0
Phibottom = 1
Phileft = 0
Phiright = 0

#value of Charge
Charge = 2

# Initial guess of interior grid
Phiguess = 0

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Set array size and set the interior value with Tguess
Phi = np.empty((lenX, lenY))
Phi.fill(Phiguess)

# Set Boundary conditions
Phi[10:,:10]=0
Phi[(lenY-1):, :] = Phitop
Phi[:1, :] = Phibottom
Phi[:, (lenX-1):] = Phiright
Phi[:, :1] = Phileft
Phi[5,0]=Charge


# Iteration
for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            #Solves phi with finite diffrence method
            Phi[i, j] = 0.25 * (Phi[i+1][j] + Phi[i-1][j] + Phi[i][j+1] + Phi[i][j-1])

#removes portion of region that is not included in problem
Phi[10:,:10]=0

fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour3D(X, Y, Phi, 50, cmap=cm.cool) 
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_zlabel('Phi') 
ax.set_title('3D contour for Phi')

#rescales grid
ticks_x = ticker.FuncFormatter(lambda X, pos: '{0:g}'.format(X/10))
ax.xaxis.set_major_formatter(ticks_x)

ticks_y = ticker.FuncFormatter(lambda Y, pos: '{0:g}'.format(Y/10))
ax.yaxis.set_major_formatter(ticks_y)

plt.savefig('plot_b.png')
plt.show() 
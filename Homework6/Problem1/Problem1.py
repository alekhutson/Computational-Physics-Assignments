import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib import cm



# Initialize parameters (grid spacing, time step, etc.)
N = 1000
L = 1.                # System extends from -L/2 to L/2
h = L/(N-1)             # Grid size
tau = .01  #time step

#array of x steps
xs = np.arange(N)*h - L/2

#array of time steps
times = np.zeros(N)
for i in range(N):
    times[i] = times[i-1] + tau

Tp, Xp = np.meshgrid(times, xs)


Ds = [1,10,100]
for D in Ds:
    
    #initialize neutron density
    rho = np.zeros(N)
    rho[0] = 1

    # Set up the A operator matrix
    A = np.zeros((N,N))     # Set all elements to zero
    coeff = D/(2*h)
    for i in range(1,N-1) :
        A[i,i-1] = coeff
        A[i,i] = -2*coeff   # Set interior rows
        A[i,i+1] = coeff

    # First and last rows for periodic boundary conditions
    A[0,-1] = coeff;   A[0,0] = -2*coeff;     A[0,1] = coeff
    A[-1,-2] = coeff;  A[-1,-1] = -2*coeff;   A[-1,0] = coeff

    # Compute the Crank-Nicolson matrix
    dCN = np.dot( np.linalg.inv(np.identity(N) - .5*tau*A - .5*tau*np.identity(N)), 
                (np.identity(N) + .5*tau*A + .5*tau*np.identity(N)) )

    rhos = []
    for i in range(N):
        rho = np.dot(dCN,rho)
        rhos.append(rho)

    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.contour3D(Tp, Xp, rhos, 50, cmap=cm.cool)
    ax.set_xlabel("time")
    ax.set_ylabel("x")
    ax.set_zlabel("neutron density")
    ax.set_title('Neutron diffusion')
    ax.text(1,1,22,D)
    ax.legend()
    plt.show()


#The plot demonstrates that the density becomes more uniform as D becomes greater


import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import scipy.linalg as la
from sympy import *

def Fucns(a,b,c): #computes the functions at (a,b,c)

    x, y, z = symbols('x y z', real=True)

    f1 = exp(-x**2)*x**2 + y**2 - z
    f2 = (x**4)/(1+x**2*y**2) - z
    f3 = z-1

    return [N(f1.subs(x,a).subs(y,b).subs(z,c)),N(f2.subs(x,a).subs(y,b).subs(z,c)),N(f3.subs(x,a).subs(y,b).subs(z,c))]

def Jacobian(a,b,c): #computes the Jacobian at (a,b,c)

    x, y, z = symbols('x y z', real=True)

    f1 = exp(-x**2)*x**2 + y**2 - z
    f2 = (x**4)/(1+x**2*y**2) - z
    f3 = z-1

    xf1 = diff(f1,x)
    yf1 = diff(f1,y)
    zf1 = diff(f1,z)

    xf2 = diff(f2,x)
    yf2 = diff(f2,y)
    zf2 = diff(f2,z)

    xf3 = diff(f3,x)
    yf3 = diff(f3,y)
    zf3 = diff(f3,z)

    return [[xf1.subs(x,a).subs(y,b).subs(z,c),yf1.subs(x,a).subs(y,b).subs(z,c),zf1.subs(x,a).subs(y,b).subs(z,c)],
    [xf2.subs(x,a).subs(y,b).subs(z,c),yf2.subs(x,a).subs(y,b).subs(z,c),zf2.subs(x,a).subs(y,b).subs(z,c)],
    [xf3.subs(x,a).subs(y,b).subs(z,c),yf3.subs(x,a).subs(y,b).subs(z,c),zf3.subs(x,a).subs(y,b).subs(z,c)]]


x0=1 #initializes x
y0=1 #initializes y
z0=1 #initializes z
Position = Matrix([x0,y0,z0])

J = Matrix(Jacobian(Position[0],Position[1],Position[2]))
F = Matrix(Fucns(Position[0],Position[1],Position[2]))

deltar = -J.inv()*F #defines the infinitesimal change over the coordinates

while deltar.norm() > .000000001: #sets tolerance
    J = Matrix(Jacobian(Position[0],Position[1],Position[2])) #computes jacobian at new position
    F = Matrix(Fucns(Position[0],Position[1],Position[2])) #computes functions at new position

    deltar = -J.inv()*F #defines the infinitesimal change over the coordinates

    Position = Position + deltar #defines the new position
    

print(Position) #prints the roots




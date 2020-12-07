import numpy as np

def fucn(x): #defines the function
    return np.exp(x) - x**4

a = -1.0 #defines the first interval over which to look for a root
b = -.5

if fucn(a)*fucn(b) < 0: #requires that the function must flip sign
    while abs(b-a) > 10**(-6): #sets the tolerance
        m = (a+b)/2 #determines midpoint
        if fucn(a)*fucn(m)<0:
            b=m
        elif fucn(b)*fucn(m)<0:
            a=m
    k = (a+b)/2
    print(k)

else:
    print("root not found")


a = .5 #defines the second interval over which to look for a root
b = 1.5

if fucn(a)*fucn(b) < 0: #requires that the function must flip sign
    while abs(b-a) > 10**(-6): #sets the tolerance
        m = (a+b)/2 #determines midpoint
        if fucn(a)*fucn(m)<0:
            b=m
        elif fucn(b)*fucn(m)<0:
            a=m
    k = (a+b)/2
    print(k)

else:
    print("root not found")


a = 8 #defines the third interval over which to look for a root
b = 10

if fucn(a)*fucn(b) < 0: #requires that the function must flip sign
    while abs(b-a) > 10**(-6): #sets the tolerance
        m = (a+b)/2 #determines midpoint
        if fucn(a)*fucn(m)<0:
            b=m
        elif fucn(b)*fucn(m)<0:
            a=m
    k = (a+b)/2
    print(k)

else:
    print("root not found")
    

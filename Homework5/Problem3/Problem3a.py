import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

df1 = pd.read_csv (r'C:\Users\alekh\projects\computationalphysics\Homework5\Problem3\data_1.csv')
df2 = pd.read_csv (r'C:\Users\alekh\projects\computationalphysics\Homework5\Problem3\data_2.csv')
df3 = pd.read_csv (r'C:\Users\alekh\projects\computationalphysics\Homework5\Problem3\data_3.csv')

def fitfunction(t,A,T):
	return A*np.exp(-t/T)

init_vals=[1,15]

fits,cov=curve_fit(fitfunction,df1['x'],df1['y'],p0=init_vals) #this fits the data using a non linear least squares method

print(fits)

plt.scatter(df1['x'],df1['y'])
plt.plot(df1['x'],fitfunction(df1['x'],*fits))
plt.savefig('part_a1.png')
plt.show()



fits,cov=curve_fit(fitfunction,df2['x'],df2['y'],p0=init_vals)

print(fits)

plt.scatter(df2['x'],df2['y'])
plt.plot(df2['x'],fitfunction(df2['x'],*fits))
plt.savefig('part_a2.png')
plt.show()



fits,cov=curve_fit(fitfunction,df3['x'],df3['y'],p0=init_vals)

print(fits)

plt.scatter(df3['x'],df3['y'])
plt.plot(df3['x'],fitfunction(df3['x'],*fits))
plt.savefig('part_a3.png')
plt.show()

#it seems as though data_1 is the only one that does not display bi-exponential behaviour becasue T1 and T2 are nearly the same value

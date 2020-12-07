import numpy as np
import matplotlib.pyplot as plt

array = np.random.randint(1,10, size=10000000) #initializes an array of randomly distributed random integers betwween 1 and 10

values = [] #initializes ana array of values to be stored

for i in range(10000000): #loops over each value in "array"
    k = np.zeros(array[i]) #initializes an array tha has the same length as the current random number
    k[0] = 1               # sets the first value to 1
    s = k[np.random.randint(len(k))] #chooses a random element in the array k
    
    if s in range(1,2): #if the random element chosen is a 1 the random number is stored (the probability of getting a 1 is 1/x)
        values.append(array[i])
    if len(values)>10**5-1: #once we get 100000 numbers this exits the loop
        break



plt.hist(values,bins=[1,2,3,4,5,6,7,8,9,10]) #generates a histogram that plots the multiplicity of each integer between 1 and 10
plt.show()

print(len(values))


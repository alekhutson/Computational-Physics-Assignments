import numpy as np

a_vector = np.array([1,2,3]) #defines an array a
b_vector = np.array([4,5,6]) #defines an array b

mag_a = np.sqrt(a_vector[0]**2 + a_vector[1]**2 + a_vector[2]**2) #magnitude of vector a
mag_b = np.sqrt(b_vector[0]**2 + b_vector[1]**2 + b_vector[2]**2) #magnitude of vector b

adotb = a_vector[0]*b_vector[0] + a_vector[1]*b_vector[1] + a_vector[2]*b_vector[2] #dot product of a and b

ab_vector = np.array([0.,0.,0.])

for iter in range (0, 3): #creates elements of ab_vector
    ab_vector[iter] =  (b_vector[iter] - ((adotb)/(mag_a**2))*a_vector[iter])


mag_ab = np.sqrt(ab_vector[0]**2 + ab_vector[1]**2 + ab_vector[2]**2) #magnitude of ab_vector
c= mag_b/mag_ab #defines the value of the constant c

v2_vector = np.array([0.,0.,0.])
for riter in range (0, 3): #creates elements of v2 vector
    v2_vector[riter] = c*ab_vector[riter]

print("v1=")
print(a_vector)
print("v2=")
print(v2_vector)

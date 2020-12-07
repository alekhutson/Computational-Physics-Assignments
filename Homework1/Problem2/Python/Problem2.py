x = 1 #initalizes x

import time
timeout = time.time() + 5
for iter in range(100000): #iteratively multiplies x by two
     m=x
     x=x*2

     #k = "{:e}".format(x)
     print(x)

     

     if x != 2*m: # exits loop if x is not twice the original value
         print(m) 
         exit

#It seems as though this will continue to work untill timed out
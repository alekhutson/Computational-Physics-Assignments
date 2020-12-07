import numpy as np
import pandas as pd

import matplotlib as mp
import matplotlib.pyplot as plt


bdata=np.genfromtxt('bifurcations.txt',delimiter=',')
## This uses numpy to import the data.

nrow=len(bdata)
ncol=len(bdata[0])
for riter in range(0,nrow,5):
	#each row corresponds to a particular choice for r.  
	# we skip every 5th row in this command.  

	yvals=bdata[riter][1:]
	#every observed value for x for this r.  
	# the 0th element is r
	# later elements are one of 256 observed values of x.
	
	yvals=list(set(yvals))
		#this picks out every unique value of r.
		# the set() finds the unique elements.  This is stored as a set

	xvals=[bdata[riter][0]]*len(yvals)
	#this is just a list containing the value r

	plt.scatter(xvals,yvals,marker=".",s=3,color='b')
	#note that this commands creates an image of the points at each value
	#of r.  we have to iterate over r and add each layer to the list.

	plt.suptitle('bifurcation diagram')
	plt.xlabel('r')
	plt.ylabel('x')
	
plt.savefig('bifurcation_python.png')
#save the figure.
plt.show()
#show the plot.  Note that .show() clears the plot afterwards!
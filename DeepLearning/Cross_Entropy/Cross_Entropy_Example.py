## This Function Impements calculation for Cross Entropy for output Y and probability P

import numpy as np

## Take Y and P as input and return Cross Entropy
Y=[1,0,1,1]
P=[0.2,0.5,0.1,0.2]
print (cross_Entropy())

def cross_Entropy(Y, P):
	cross_entropy=0.0

	for i in range (0, len(Y)):
		cross_entropy=cross_entropy+Y[i]*np.log(P[i])+(1-Y[i])*np.log(1-P[i])

	return -cross_entropy
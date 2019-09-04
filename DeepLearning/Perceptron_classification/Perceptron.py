import numpy as np

np.random.seed(42)

def stepFunction(t):
	if t>=0:
		return 1
	return 0

def prediction(X, W, b):
	return stepFunction((np.matmul(X,W)+b)[0])
import numpy as np

highArray  = np.arange(10)
print highArray
print highArray[:-1]
print highArray[1:]
highArray[:-1] = highArray[1:]
print highArray
highArray[-1]  = 10

print highArray

print np.eye(3)
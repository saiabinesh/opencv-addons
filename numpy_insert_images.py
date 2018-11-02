import numpy as np
a = np.zeros(shape = (2,2))
print(a)

b = a[:,:,np.newaxis]


print(b.shape)
print(b)

b= b[True]
print(b.shape)
print(b)

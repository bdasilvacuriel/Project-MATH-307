import numpy as np
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

# this is restarted b/c I noticed we only need black and white
# and color was making it very complicated, using lots of code from old main


A=mpimg.imread('/Users/Bendasilva/Desktop/MATLAB/LennaGray.jpg')

print(A,"\n")
print(A.shape,"\n")

#Print np arrays as images
plt.imshow(A, interpolation='nearest')
plt.show()

At=A.T

U, S, VT = np.linalg.svd(At@A)
print("U matrix:\n", U)
print("Singular values:\n", S)
print("V^T matrix:\n", VT)

# Rank 1 A1 below

# part c

UVT=np.outer(U[:,0],VT[0,:])
print("UVT:",UVT)
A1r=S[0]*UVT

plt.imshow(A1r, interpolation='nearest')
plt.show()


# dont think I'm adding them correctly?

for i in range(0,50):
    Ai=np.zeros(A.shape)
    Ai=Ai+(S[i]*U[:,i]*VT[i,:])
    plt.imshow(Ai,interpolation='nearest')
    plt.show()
   





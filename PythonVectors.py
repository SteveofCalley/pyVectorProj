import numpy as np
import matplotlib.pyplot as plt

V = np.array([[1,1],[-2,2],[4,-7]])
origin = [0], [0] # origin point
plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
v12 = V[0] + V[1] # adding up the 1st (red) and 2nd (blue) vectors
plt.quiver(*origin, v12[0], v12[1])
plt.show()

# Python Triange vectors.
import matplotlib.pyplot as plt
import numpy as np
fig1, ax1 = plt.subplots()
ax1.set_title('An effective vector boxx')
scale_units : {'width', 'height'}
i = 0
ix = [-0.5, -0.5, 0.5, 0.5]
iy = [-0.5, 0.5, 0.5, -0.5]
iu = [0, 1, 0, -1]
iv = [1, 0, -1, 0]
while i < 4:
    Q = ax1.quiver(ix[i], iy[i], iu[i], iv[i], angles='xy', scale_units='xy', scale=1)
    i += 1
plt.show() 
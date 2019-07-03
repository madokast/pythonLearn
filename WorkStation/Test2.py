import numpy as np
import matplotlib.pyplot as plt

nz = np.linspace(-1, 1.5, 2)
print(nz)
nBy = [1, 2]
nBy2 = [3,4]

plt.plot(nz, nBy)
plt.plot(nz, nBy2)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)

plt.figure()
plt.plot(t,y)
plt.savefig("funcion.png")
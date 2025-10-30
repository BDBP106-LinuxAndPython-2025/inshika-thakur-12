#!/usr/bin/python3

"""The normalized Gaussian function centered at x = 0 is given.
Plot and compare the shapes of these functions for standard deviations
σ = 1, 1.5 and 2."""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-12, 12, 1000)
def gaussian(x, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-x**2 / (2 * sigma**2))
g1 = gaussian(x, 1)
g15 = gaussian(x, 1.5)
g2 = gaussian(x, 2)
plt.plot(x, g1, label='sigma=1')
plt.plot(x, g15, label='sigma=1.5')
plt.plot(x, g2, label='sigma=2')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Normalized Gaussian function for three different sigma')
plt.legend()
plt.show()
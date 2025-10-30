#!/usr/bin/python3

"""(9) Plot the function that is given on 1000 points across the range −20 ≤ x ≤ 20.
What happens to these functions at x = nπ/2(n = 0, ±1, ±2, . . .)? What happens in your
plot of them?"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-20, 20, 1000) #this is like from -20 to 20 you will have 1000 points in between

f1=np.log(1/np.cos(x)**2)
f2=np.log(1/np.sin(x)**2)

fig, ax = plt.subplots() #this creates an empty plot
ax.plot(x,f1)
ax.plot(x,f2)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('To plot the function')
plt.show() #this is like a print statement to show the graph


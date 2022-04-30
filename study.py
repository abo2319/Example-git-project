import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)

plt.figure(num = 3, figsize = (8, 5))
plt.plot(x, y2,'b', linewidth = 1.0)
plt.plot(x, y1,'r--', linewidth = 1.0)
plt.show()

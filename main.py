import numpy as np
import matplotlib.pyplot as plt
from parser import *

x, y = parseASCII('./testdata/SiO2.ascii')

plt.plot(x, y)

plt.show()

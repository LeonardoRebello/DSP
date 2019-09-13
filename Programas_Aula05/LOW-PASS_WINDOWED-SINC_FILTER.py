import numpy as np
import matplotlib.pyplot as plt

FC = float(input("FC: "))
BW = float(input("BW: "))

M = 4 / BW

Filter_kernel = []
for i in range(100):
    if i - M/2 == 0:
        Filter_kernel.append(2 * np.pi * FC)
    else:
        Filter_kernel.append(np.sin(2 * np.pi * FC * (i - M/2)) / (i - M/2))
    Filter_kernel[i] = Filter_kernel[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M))

SUM = 0
for i in range(100):
    SUM = SUM + Filter_kernel[i]

for i in range(100):
    Filter_kernel[i] = Filter_kernel[i] / SUM

xAxis = np.linspace(0, len(Filter_kernel), len(Filter_kernel), endpoint=False)

plt.plot(xAxis, Filter_kernel)
plt.show()
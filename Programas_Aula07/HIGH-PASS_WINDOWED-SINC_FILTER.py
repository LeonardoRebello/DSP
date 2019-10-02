import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc

FC = 0.1
M = 160

Filter_kernel = []
for i in range(M):
    if i - M/2 == 0:
        Filter_kernel.append(2 * np.pi * FC)
    else:
        Filter_kernel.append(np.sin(2 * np.pi * FC * (i - M/2)) / (i - M/2))
    Filter_kernel[i] = (Filter_kernel[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M)))

SUM = 0
for i in range(M):
    SUM = SUM + Filter_kernel[i]

for i in range(M):
    Filter_kernel[i] = (Filter_kernel[i] / SUM) * - 1

Filter_kernel[int(M/2)] = Filter_kernel[int(M/2)] + 1

xAxis, yAxis = sc.freqz(Filter_kernel)

plt.plot(xAxis, abs(yAxis))
plt.show()
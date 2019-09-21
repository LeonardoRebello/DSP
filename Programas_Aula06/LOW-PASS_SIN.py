import numpy as np
import matplotlib.pyplot as plt

xAxis = np.linspace(0., 10., 2500, endpoint=False)
Data = np.sin(2 * np.pi * 560 * xAxis)

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

Data_Output = np.convolve(Data, Filter_kernel)

plt.subplot(3, 1, 1)
plt.plot(np.linspace(0, len(Data), len(Data), endpoint=False), Data)
plt.title("Sin de entrada")

xAxis = np.linspace(0, len(Data_Output), len(Data_Output))

plt.subplot(3, 1, 2)
plt.plot(xAxis, Data_Output)
plt.title("Sin filtrado")

plt.subplot(3, 1, 3)
plt.plot(xAxis, abs(np.fft.fft(Data_Output)))
plt.title("Sin filtrado na frequência")
plt.show()
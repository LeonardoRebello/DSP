import matplotlib.pyplot as plt
import numpy as np

n = int(input("Numero de amostras: "))

yAxis_200Hz = []
yAxis_2kHz = []
yAxis_Soma = []

for i in range(n):
    yAxis_200Hz.append(np.sin(2 * np.pi * (200 / 8000) * i))
    yAxis_2kHz.append(np.sin(2 * np.pi * (2000 / 8000) * i))
    yAxis_Soma.append(yAxis_200Hz[i] + yAxis_2kHz[i])


xAxis = np.linspace(0., n, n, endpoint=False)

plt.subplot(3, 1, 1)
plt.suptitle("Trabalho 03 - Senoides de 200Hz e 2kHz e a \nsoma das duas, respectivamente:")
plt.stem(xAxis, yAxis_200Hz, use_line_collection=True)

plt.subplot(3, 1, 2)
plt.stem(xAxis, yAxis_2kHz, use_line_collection=True)

plt.subplot(3, 1, 3)
plt.stem(xAxis, yAxis_Soma, use_line_collection=True)
plt.show()


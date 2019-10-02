import matplotlib.pyplot as plt
import numpy as np

n = int(input("Numero de amostragem: "))

yAxis_100Hz = []
yAxis_1kHz = []

for i in range(n):
    yAxis_100Hz.append(3*np.exp(-2*(i/100)))
    yAxis_1kHz.append(3*np.exp(-2*(i/1000)))


n_100Hz = np.linspace(0., n, n, endpoint=True)
n_1kHz = np.linspace(0., n, n, endpoint=True)

plt.subplot(2, 1, 1)
plt.suptitle("Trabalho 01 - Euler 100Hz e 1kHz, respectivamente:")
plt.stem(n_100Hz, yAxis_100Hz, use_line_collection=True)

plt.subplot(2, 1, 2)
plt.stem(n_1kHz, yAxis_1kHz, use_line_collection=True)
plt.show()





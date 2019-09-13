import numpy as np
import matplotlib.pyplot as plt

FS = float(input("Frequencia de amostragem:"))
fo = float(input("Frequencia em Hertz: "))
a = float(input("Amplitude do sinal: "))
n = int(input("Numero de amostras: "))

yAxis_Sin = []
yAxis_Cos = []

for i in range(n):
    yAxis_Sin.append(a * np.sin(2 * np.pi * (fo / FS) * i))
    yAxis_Cos.append(a * np.cos(2 * np.pi * (fo / FS) * i))

xAxis = np.linspace(0., n, n, endpoint=True)

plt.subplot(2, 1, 1)
plt.title("Trabalho 02 - Sinusoidal: Sin e Cos, respectivamente:")
plt.stem(xAxis, yAxis_Sin, use_line_collection=True)

plt.subplot(2, 1, 2)
plt.stem(xAxis, yAxis_Cos, use_line_collection=True)
plt.show()

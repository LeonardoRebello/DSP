import matplotlib.pyplot as plt
import numpy as np

n = int(input("Numero de amostragem: "))
a = float(input("Valor de a: "))

yAxis = []
for i in range(n):
    yAxis.append(a ** (i))

xAxis = np.linspace(0., n, n, endpoint=True)

plt.title("Trabalho 02 - Exponencial")
plt.stem(xAxis, yAxis, use_line_collection=True)
plt.show()

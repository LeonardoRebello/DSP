import matplotlib.pyplot as plt
import numpy as np

n = int(input("Numero de amostras: "))

yAxis = []
for i in range(n):
    if i >= 0:
        yAxis.append(1)
    else:
        yAxis.append(0)

xAxis = np.linspace(0., n, n, endpoint=True)

plt.title("Trabalho 02 - Degrau unitário")
plt.stem(xAxis, yAxis, use_line_collection=True)
plt.show()

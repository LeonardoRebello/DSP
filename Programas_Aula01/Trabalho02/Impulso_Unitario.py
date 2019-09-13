import matplotlib.pyplot as plt
import numpy as np

n = int(input("Numero de amostras: "))

n_Amostras = np.linspace(0., n, n, endpoint=True)

def Impulso_Unitario(Amostras):
    yAxis = []
    for i in range(len(n_Amostras)):
        if i == 0.:
            yAxis.append(1)
        else:
            yAxis.append(0)
    return yAxis

plt.title("Trabalho 02 - Impulso Unitário")
plt.stem(n_Amostras, Impulso_Unitario(n_Amostras), use_line_collection=True)
plt.show()




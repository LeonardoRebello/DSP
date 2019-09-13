import numpy as np
import matplotlib.pyplot as plt
import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb

x = fb.Degrau_Unitario(1, 11)

Data_Filtro = 0
data_Output = []
for i in range(len(x)):
    for k in range(4):
        if (i - k) >= 0:
            Data_Filtro += x[i - k]

    Data_Filtro = Data_Filtro / 4
    data_Output.append(Data_Filtro)
    Data_Filtro = 0

y = np.convolve(x, data_Output)

xAxis = np.linspace(0, len(y), len(y), endpoint=False)

plt.subplot(2, 1, 1)
plt.stem(xAxis, y, use_line_collection=True)

x = [1/4, 1/2, 1, 1/2, 1/4]
h = [0, 0, 1, 1/2, 1/4]

y = np.convolve(h, x)

xAxis = np.linspace(-2, len(y) -2, len(y), endpoint=False)

plt.subplot(2, 1, 2)
plt.stem(xAxis, y, use_line_collection=True)
plt.show()
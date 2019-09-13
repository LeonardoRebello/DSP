import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import numpy as np
import matplotlib.pyplot as plt

def Sistemas_Discretos(array):
    array_Out = []
    array_Out.append(array[0])
    for i in range(1, len(array)):
        if i > 1:
            array_Out.append(array[i] + ((1/4) * array_Out[i - 1]) - ((1/2) * array_Out[i - 2]))
        else:
            array_Out.append(array[i] + ((1 / 4) * array_Out[i - 1]))
    return array_Out

def Degrau_Unitario(k, Num_Amostras):
    yAxis = []
    for i in range(len(Num_Amostras)):
        if Num_Amostras[i] >= 0:
            yAxis.append(k * 1)
        else:
            yAxis.append(0)
    return yAxis

xAxis = np.linspace(-2, 100, 102, endpoint=False)

plt.suptitle("Equação diferenca aplicada para um degrau\nem um intervalo de -2 a 100")
plt.stem(xAxis, Sistemas_Discretos(Degrau_Unitario(1, xAxis)), use_line_collection=True)
plt.show()
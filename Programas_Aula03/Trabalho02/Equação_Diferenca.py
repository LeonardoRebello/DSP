import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Numero de amostras: "))

def Sistemas_Discretos(array):
    array_Out = []
    array_Out.append(array[0])
    for i in range(1, len(array)):
        if i > 1:
            array_Out.append(array[i] + (-1 * ((1/4)*array_Out[i - 1] + (1/8) * array_Out[i - 2])))
        else:
            array_Out.append(array[i] + (-1 * ((1 / 4) * array_Out[i - 1])))
    return array_Out

xAxis = np.linspace(0., n, n, endpoint=False)

plt.suptitle("Equação diferença para os sinais apresentados")
plt.subplot(3, 1, 1)
plt.stem(xAxis, Sistemas_Discretos(fb.Impulso_Unitario(n)), use_line_collection=True)

plt.subplot(3, 1, 2)
plt.stem(xAxis, Sistemas_Discretos((fb.Degrau_Unitario(2, n))), use_line_collection=True)

plt.subplot(3, 1, 3)
plt.stem(xAxis, Sistemas_Discretos(fb.Exponencial(0.7, n)), use_line_collection=True)
plt.show()

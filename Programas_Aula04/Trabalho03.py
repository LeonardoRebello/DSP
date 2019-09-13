import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import matplotlib.pyplot as plt
import numpy as np

def Sistemas_Discretos(array):
    array_Out = []
    array_Out.append(array[0])
    for i in range(1, len(array)):
        if i > 1:
            array_Out.append(array[i] + 10 * array[i - 1] + 2 * array[i - 2] + 3 * array_Out[i - 1] - 2 * array_Out[i -2])
        else:
            array_Out.append(array[i] + 10 * array[i - 1] + 3 * array_Out[i - 1])
    return array_Out

xAxis = np.linspace(0, 21, 21, endpoint=False)

plt.figure(1)
plt.suptitle("Resposta ao Degrau unitário e ao Impulso Unitário\nrespectivamente")
plt.subplot(2, 1, 1)
plt.stem(xAxis, Sistemas_Discretos(fb.Degrau_Unitario(1, len(xAxis))), use_line_collection=True)

plt.subplot(2, 1, 2)
plt.stem(xAxis, Sistemas_Discretos(fb.Impulso_Unitario(len(xAxis))), use_line_collection=True)

plt.figure(2)
fb.Zplane([6, 10, 2], [1, -3, 2])
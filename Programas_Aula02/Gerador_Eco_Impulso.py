import matplotlib.pyplot as plt
import Biblioteca_FuncoesBasicas.Funcoes_Basicas as Func
import numpy as np

FS = 8000
TS = 1/FS

L = 0.1 * FS
d1 = 0.05 * FS
d2 = 0.075 * FS

P0 = 1
P1 = 0.7
P2 = 0.5

Vet_Amostras = [0]*int(L)
Data_in = Func.Impulso_Unitario(int(L))

def Eco(Data, i):
    Peso = (float)
    if i == 0:
        Peso = P0
    elif i == d1:
        Peso = P1
    else:
        Peso = P2
    return Data * Peso

for i in range(int(L)):
    if i == 0 or i == int(d1) or i == int(d2):
        Vet_Amostras[i] += Eco(Data_in[i], i)
    Data_in.insert(0, 0)
    del Data_in[-1]

xAxis = np.linspace(0., len(Vet_Amostras), len(Vet_Amostras), endpoint=False)

plt.suptitle("Trabalho 05 - Gerador de Eco para impulso de entrada")
plt.stem(xAxis, Vet_Amostras, use_line_collection=True)
plt.show()
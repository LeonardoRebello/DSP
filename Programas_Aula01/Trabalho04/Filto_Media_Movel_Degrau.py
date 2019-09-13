import numpy as np
import matplotlib.pyplot as plt
import Biblioteca_FuncoesBasicas.Funcoes_Basicas as Func

Num_Amostras = int(input("Numero de amostras: "))
Tam_Media = int(input("Tamanho da média: "))

data = Func.Degrau_Unitario(1, Num_Amostras)
Data_Filtro = 0

data_Output = []
for i in range(Num_Amostras):
    for k in range(Tam_Media):
        if (i - k) >= 0:
            Data_Filtro += data[i - k]

    Data_Filtro = Data_Filtro / Tam_Media
    data_Output.append(Data_Filtro)
    Data_Filtro = 0

xAxis = np.linspace(0., len(data_Output), len(data_Output), endpoint=False)

plt.title("Trabalho 04 - Filtro Média Móvel Aplicada no Degrau")
plt.stem(xAxis, data_Output, use_line_collection=True)
plt.show()

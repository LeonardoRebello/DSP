import wave
import numpy as np
import matplotlib.pyplot as plt

Tam_Media = int(input("Tamanho da média: "))

data = np.memmap("Sweep_100_3k4.pcm", dtype='h', mode='r')
Data_Filtro = 0
data_Output = []

for i in range(len(data)):
    for k in range(Tam_Media):
        if (i - k) >= 0:
            Data_Filtro += data[i - k]

    Data_Filtro = Data_Filtro / Tam_Media
    data_Output.append(Data_Filtro)
    Data_Filtro = 0

n = np.arange(0, len(data), 1.)

Out_Audio = np.memmap("Sweep_100_3k4_Filtrado.pcm", dtype='int16', mode='w+', shape=(1, len(data_Output)))
Out_Audio[:] = data_Output[:]
del Out_Audio

plt.subplot(2, 1, 1)
plt.title("Trabalho 04 - Filtro Média Móvel Aplicado ao Sweep")
plt.plot(n, data)

plt.subplot(2, 1, 2)
plt.plot(n, data_Output)
plt.show()

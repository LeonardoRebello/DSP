import matplotlib.pyplot as plt
import numpy as np

Data = np.memmap("C:\\Users\\Leonardo\\Documents\\Faculdade\\8Periodo\\Processador_digital_de_sinais\\Programas_Aula08\\White_Noise.pcm", dtype='h', mode='r')

Filter_Unknown = [1/4, 1/4, 1/4, 1/4]
Data_Op = [0] * len(Filter_Unknown)

Filter_Adaptive = [0] * len(Filter_Unknown)

Error = []

u = 0.000000000002

for i in range(len(Data)):

    Data_Op.insert(0, Data[i])
    del Data_Op[-1]

    Value_Adaptive = np.convolve(Data_Op, Filter_Adaptive)
    Value_Unknown = np.convolve(Data_Op, Filter_Unknown)

    Erro = float(sum(Value_Unknown) - sum(Value_Adaptive))
    Error.append(Erro)

    for y in range(len(Filter_Adaptive)):
        Filter_Adaptive[y] = Filter_Adaptive[y] + (u * Erro * Data_Op[y])

plt.plot(range(0, len(Error)), Error)
plt.show()
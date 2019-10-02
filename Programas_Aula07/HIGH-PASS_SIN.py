import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc

#Data = np.memmap("Sen200Hz.pcm", dtype='h', mode='r')
Data = np.memmap("Sen800Hz.pcm", dtype='h', mode='r')
#Data = np.memmap("Sen2000Hz.pcm", dtype='h', mode='r')

FC = 0.1
M = 160

Filter_kernel = []
for i in range(M):
    if i - M/2 == 0:
        Filter_kernel.append(2 * np.pi * FC)
    else:
        Filter_kernel.append(np.sin(2 * np.pi * FC * (i - M/2)) / (i - M/2))
    Filter_kernel[i] = (Filter_kernel[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M)))

SUM = 0
for i in range(M):
    SUM = SUM + Filter_kernel[i]

for i in range(M):
    Filter_kernel[i] = (Filter_kernel[i] / SUM) * - 1

Filter_kernel[int(M/2)] = Filter_kernel[int(M/2)] + 1

Data_Output = np.convolve(Filter_kernel, Data)

xAxis, yAxis = sc.freqz(Filter_kernel)

plt.subplot(3, 1, 1)
plt.plot(xAxis, abs(yAxis))

plt.subplot(3, 1, 2)
plt.plot(np.linspace(0, len(Data), len(Data), endpoint=False), Data)

plt.subplot(3, 1, 3)
plt.plot(np.linspace(0, len(Data_Output), len(Data_Output), endpoint=False), Data_Output)
plt.show()

#Out_Audio = np.memmap("Sen200hz_Filtrado.pcm", dtype='int16', mode='w+', shape=(1, len(Data_Output)))
Out_Audio = np.memmap("Sen800hz_Filtrado.pcm", dtype='int16', mode='w+', shape=(1, len(Data_Output)))
#Out_Audio = np.memmap("Sen2000hz_Filtrado.pcm", dtype='int16', mode='w+', shape=(1, len(Data_Output)))
Out_Audio[:] = Data_Output[:]
del Out_Audio
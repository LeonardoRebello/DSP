import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import matplotlib.pyplot as plt
import scipy.signal as sg
import numpy as np

Data = np.memmap("DTMF.pcm", dtype='h', mode='r')

Fs = 8000
BW = 20
M = int(4 / (BW / (Fs / 2)))

FC1 = (697 - (BW / 2)) / (Fs / 2)
FC2 = (697 + (BW / 2)) / (Fs / 2)

Filter_Low = fb.LOWPASS_WINDOWED(FC1, M)
Filter_High = fb.HIGHPASS_WINDOWED(FC2, M)

Filter_band = []
for i in range(M):
    Filter_band.append(Filter_High[i] + Filter_Low[i])

for i in range(M):
    Filter_band[i] = Filter_band[i] * -1

Filter_band[int(M/2)] = Filter_band[int(M/2)] + 1

Data_Output = np.convolve(Filter_band, Data)

xAxis, yAxis = sg.freqz(Filter_band)

plt.plot(np.linspace(0, len(Data_Output), len(Data_Output), endpoint=False), Data_Output)
plt.show()

Out_Audio = np.memmap("DTMF_Filtrado.pcm", dtype='int16', mode='w+', shape=(1, len(Data_Output)))
Out_Audio[:] = Data_Output[:]
del Out_Audio
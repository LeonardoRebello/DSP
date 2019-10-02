import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import matplotlib.pyplot as plt
import scipy.signal as sg

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

xAxis, yAxis = sg.freqz(Filter_band)

plt.plot(xAxis, abs(yAxis))
plt.show()
import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import numpy as np
import matplotlib.pyplot as plt

Gb = 0.5
Gm = 1
Ga = 0.3

FS = 48000
BW = 1000
M = int(4 / (BW / FS))

Data = np.memmap("Music.pcm", dtype='h', mode='r')

Low_Pass = fb.LOWPASS_WINDOWED(2500 / FS, M)
Band_Pass = fb.BANDPASS_WINDOWED(2500 / FS, 8500 /FS, M)
High_Pass = fb.HIGHPASS_WINDOWED(8500 / FS, M)

Low_Pass = np.convolve(Data, Low_Pass)
Band_Pass = np.convolve(Data, Band_Pass)
High_Pass = np.convolve(Data, High_Pass)

Data_Output = (Low_Pass * Gb) + (Band_Pass * Gm) + (High_Pass * Ga)

plt.plot(range(0, len(Data_Output)), Data_Output)
plt.show()

Out_Audio = np.memmap("Sweep_Out.pcm", dtype='int16', mode='w+', shape=(1, len(Data_Output)))
Out_Audio[:] = Data_Output[:]
del Out_Audio
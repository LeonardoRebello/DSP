import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)

Gb = 0
Gm = 0
Ga = 1

FS = 48000
BW = 1000
M = int(4 / (BW / FS))

Data = np.memmap("Sweep_100_3k4.pcm", dtype='h', mode='r')

Low_Pass = fb.LOWPASS_WINDOWED(2500 / FS, M)
Band_Pass = fb.BANDPASS_WINDOWED(2500 / FS, 8500 /FS, M)
High_Pass = fb.HIGHPASS_WINDOWED(8500 / FS, M)

Low_Pass = np.convolve(Data, Low_Pass)
Band_Pass = np.convolve(Data, Band_Pass)
High_Pass = np.convolve(Data, High_Pass)

print(len(Low_Pass))

#for i in range(len(Low_Pass)):
 #   print(str(Low_Pass[i]) + ', ')

Data_Output = (Low_Pass * Gb) + (Band_Pass * Gm) + (High_Pass * Ga)

plt.plot(range(0, len(Data_Output)), Data_Output)
plt.show()

Out_Audio = np.memmap("Sweep_Out.pcm", dtype='int16', mode='w+', shape=(1, len(Data_Output)))
Out_Audio[:] = Data_Output[:]
del Out_Audio
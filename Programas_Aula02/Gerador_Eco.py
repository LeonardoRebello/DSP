import numpy as np
import matplotlib.pyplot as plt

FS = 8000
TS = 1 / FS

d1 = 0.05 * FS
d2 = 0.250 * FS

Delays = [d1, d2]

P0 = 1
P1 = 0.7
P2 = 0.5

Pesos = [P1, P2]

Audio_in = np.memmap("teste.pcm", dtype='h', mode='r')
Audio_Eco = [0]*len(Audio_in)

def Gerador_Eco():
    Pos = 0
    for i in range(int(Delays[0]), len(Audio_in), 1):
        if Pos + 1 == len(Delays):
            Audio_Eco[i] += Audio_in[i - int(Delays[-1])] * Pesos[-1]
        elif i < int(Delays[Pos + 1]):
            Audio_Eco[i] += Audio_in[i - int(Delays[Pos])] * Pesos[Pos]
        else:
            Pos += 1

Gerador_Eco()

xAxis = np.linspace(0., len(Audio_in), len(Audio_in), endpoint=False)

Out_Audio = np.memmap("Audio_Eco.pcm", dtype='int16', mode='w+', shape=(1, len(Audio_Eco)))
Out_Audio[:] = Audio_Eco[:]
del Out_Audio

plt.suptitle("Trabalho 05 - Gerador de Eco para audio de entrada")
plt.plot(xAxis, Audio_in)
plt.plot(xAxis, Audio_Eco)
plt.show()


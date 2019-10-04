import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import matplotlib.pyplot as plt
import numpy as np

FS = 8000
BW = 40
M = int(4 / (BW / FS))

Data = np.memmap("DTMF_Ruido.pcm", dtype='h', mode='r')

Lin01 = fb.BANDPASS_WINDOWED(((697 + 20) / 8000), ((697 - 20) / 8000), M)
Lin02 = fb.BANDPASS_WINDOWED(((770 + 20) / 8000), ((770 - 20) / 8000), M)
Lin03 = fb.BANDPASS_WINDOWED(((852 + 20) / 8000), ((852 - 20) / 8000), M)
Lin04 = fb.BANDPASS_WINDOWED(((941 + 20) / 8000), ((941 - 20) / 8000), M)
Col01 = fb.BANDPASS_WINDOWED(((1209 + 20) / 8000), ((1209 - 20) / 8000), M)
Col02 = fb.BANDPASS_WINDOWED(((1336 + 20) / 8000), ((1336 - 20) / 8000), M)
Col03 = fb.BANDPASS_WINDOWED(((1477 + 20) / 8000), ((1477 - 20) / 8000), M)

Lin01_OUT = np.convolve(abs(np.convolve(Data, Lin01)), fb.LOWPASS_WINDOWED(697 / FS, M))
Lin02_OUT = np.convolve(abs(np.convolve(Data, Lin02)), fb.LOWPASS_WINDOWED(770 / FS, M))
Lin03_OUT = np.convolve(abs(np.convolve(Data, Lin03)), fb.LOWPASS_WINDOWED(852 / FS, M))
Lin04_OUT = np.convolve(abs(np.convolve(Data, Lin04)), fb.LOWPASS_WINDOWED(941 / FS, M))
Col01_OUT = np.convolve(abs(np.convolve(Data, Col01)), fb.LOWPASS_WINDOWED(1209 / FS, M))
Col02_OUT = np.convolve(abs(np.convolve(Data, Col02)), fb.LOWPASS_WINDOWED(1336 / FS, M))
Col03_OUT = np.convolve(abs(np.convolve(Data, Col03)), fb.LOWPASS_WINDOWED(1477 / FS, M))

plt.subplot(3, 1, 1)
plt.plot(range(0, len(Data)), Data)

plt.subplot(3, 1, 2)
plt.plot(range(0, len(Lin01_OUT)), Lin01_OUT)
plt.plot(range(0, len(Lin02_OUT)), Lin02_OUT)
plt.plot(range(0, len(Lin03_OUT)), Lin03_OUT)
plt.plot(range(0, len(Lin04_OUT)), Lin04_OUT)

plt.subplot(3, 1, 3)
plt.plot(range(0, len(Col01_OUT)), Col01_OUT)
plt.plot(range(0, len(Col02_OUT)), Col02_OUT)
plt.plot(range(0, len(Col03_OUT)), Col03_OUT)

Numero = ""
lastValue = [0]*len(Lin01_OUT)
insetNumber = True

for i in range(0, len(Lin01_OUT)):

    if((insetNumber == False) and lastValue[i] < 1000):

        insetNumber = True
        lastValue = [0]*len(Lin01_OUT)
    else:
        insetNumber = False

    if(insetNumber == True):

        if Lin01_OUT[i] > 5000:
            if Col01_OUT[i] > 4000:
                Numero += '1'
            elif Col02_OUT[i] > 5000:
                Numero += '2'
            elif Col03_OUT[i] > 5000:
                Numero += '3'

            insetNumber = False
            lastValue = Lin01_OUT

        elif Lin02_OUT[i] > 5000:
            if Col01_OUT[i] > 4000:
                Numero += '4'
            elif Col02_OUT[i] > 5000:
                Numero += '5'
            elif Col03_OUT[i] > 4000:
                Numero += '6'

            insetNumber = False
            lastValue = Lin02_OUT

        elif Lin03_OUT[i] > 5000:
            if Col01_OUT[i] > 4000:
                Numero += '7'
            elif Col02_OUT[i] > 5000:
                Numero += '8'
            elif Col03_OUT[i] > 4000:
                Numero += '9'

            insetNumber = False
            lastValue = Lin03_OUT

        elif Lin04_OUT[i] > 5000:
            if Col01_OUT[i] > 4000:
                Numero += '*'
            elif Col02_OUT[i] > 5000:
                Numero += '0'
            elif Col03_OUT[i] > 5000:
                Numero += '#'
            insetNumber = False
            lastValue = Lin04_OUT

print(Numero)
plt.show()
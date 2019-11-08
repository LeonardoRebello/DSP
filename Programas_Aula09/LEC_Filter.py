import matplotlib.pyplot as plt
import numpy as np

FAR = np.memmap("far.pcm", dtype='h', mode='r')
NEAR = np.memmap("near.pcm", dtype='h', mode='r')

coefficient = 100

Data_Op = [0] * coefficient

Filter_Adaptive = [0] * coefficient

Error = []

u = 0.000000002

for i in range(len(FAR)):

    Data_Op.insert(0, FAR[i])
    del Data_Op[-1]

    Conv_Adaptive = float(sum(np.convolve(Data_Op, Filter_Adaptive)))

    Erro = NEAR[i] - Conv_Adaptive
    Error.append(Erro)

    for y in range(len(Filter_Adaptive)):
        Filter_Adaptive[y] = Filter_Adaptive[y] + (u * Erro * Data_Op[y])

Out_Audio = np.memmap("LEC_Filter.pcm", dtype='int16', mode='w+', shape=(1, len(Error)))
Out_Audio[:] = Error[:]
del Out_Audio

plt.plot(range(0, len(Error)), Error)
plt.show()
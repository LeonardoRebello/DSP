import numpy as np

def norm(Sample, MaxValue):

    Sample_Out = []

    for i in range(len(Sample)):

        if Sample[i] != 0:

            Sample_Out.append(Sample[i] / MaxValue)
        else:

                Sample_Out.append(0)

    return Sample_Out

Data = np.memmap("Guitar_test.pcm", dtype='h', mode='r')

MaxValue = 31809

Data = norm(Data, MaxValue)

Out_Audio = np.memmap("Guitar_Norm.pcm", dtype='int16', mode='w+', shape=(1, len(Data)))
Out_Audio[:] = Data[:]
del Out_Audio
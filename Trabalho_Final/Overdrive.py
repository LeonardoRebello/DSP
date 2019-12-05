import numpy as np

def norm(Sample, MaxValue):

    Sample_Out = []

    for i in range(len(Sample)):

        if Sample[i] != 0:

            Sample_Out.append(Sample[i] / MaxValue)
        else:

                Sample_Out.append(0)

    return Sample_Out

def OVERDRIVE(Sample):

    Sample_Out = Sample
    Threshold = 1/3

    for i in range(len(Sample)):

        if (0 < Sample_Out[i] <= Threshold) or ((-1 * Threshold) <= Sample_Out[i] < 0):
            Sample_Out[i] = 2 * Sample_Out[i]

        if Sample_Out[i] >= Threshold:
            Sample_Out[i] = (3 - (2 - (3 * Sample_Out[i])) ** 2) / 3

        if Sample_Out[i] <= (-1 * Threshold):
            Sample_Out[i] = (-1 * (3 - (2 - (3 * (-1 * Sample_Out[i]))) ** 2)) / 3

        if Sample_Out[i] >= (2 * Threshold):
            Sample_Out[i] = 1

        if Sample_Out[i] <= (-2 * Threshold):
            Sample_Out[i] = -1

    return Sample_Out

Data = np.memmap("Guitar_test.pcm", dtype='h', mode='r')

MaxValue = 31809

Data = norm(Data, MaxValue)

Data = OVERDRIVE(Data)

for i in range(len(Data)):

    Data[i] = Data[i] * MaxValue

Out_Audio = np.memmap("Overdrive_Python.pcm", dtype='int16', mode='w+', shape=(1, len(Data)))
Out_Audio[:] = Data[:]
del Out_Audio


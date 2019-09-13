import numpy as np

Vetor_in = []
Vetor_out = []
Filter_kernel = []

FC = .14
M = 100

for i in range(100):
    if i - M/2 == 0:
        Filter_kernel[i] = 2 * np.pi * FC
    else:
        Filter_kernel[i] = np.sin(2 * np.pi * FC * (i - M/2)) / (i - M/2)
    Filter_kernel[i] = Filter_kernel[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M))

SUM = 0
for i in range(100):
    SUM = SUM + Filter_kernel[i]

for i in range(100):
    Filter_kernel[i] = Filter_kernel[i] / SUM

for i in range(100, 4999):
    Vetor_out[i] = 0
    for j in range(100):
        Vetor_out[i] = Vetor_out[i] + Vetor_in[i - j] * Filter_kernel[j]


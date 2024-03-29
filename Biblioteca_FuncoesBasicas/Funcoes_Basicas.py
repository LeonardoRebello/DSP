import numpy as np

def Impulso_Unitario(Num_Amostras):
    yAxis = []
    for i in range(Num_Amostras):
        if i == 0.:
            yAxis.append(1)
        else:
            yAxis.append(0)
    return yAxis

def Degrau_Unitario(k, Num_Amostras):
    yAxis = []
    for i in range(Num_Amostras):
        if i >= 0:
            yAxis.append(k * 1)
        else:
            yAxis.append(0)
    return yAxis

def Exponencial(a, Num_Amostras):
    yAxis = []
    for i in range(Num_Amostras):
        yAxis.append(a**(i))
    return yAxis

def Senoide(a, fo, FS, Num_Amostras):
    yAxis = []
    for i in range(Num_Amostras):
        yAxis.append(a * np.sin(2 * np.pi * (fo / FS) * i))
    return yAxis

def Cossenoide(a, fo, FS, Num_Amostras):
    yAxis = []
    for i in range(Num_Amostras):
        yAxis.append(a * np.cos(2 * np.pi * (fo / FS) * i))
    return yAxis

def Zplane(xAxis, yAxis):
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import patches

    ax = plt.subplot(111)
    uc = patches.Circle((0, 0), radius=1, fill=False, color='black', ls='dashed')
    ax.add_patch(uc)

    Zeros = np.roots(xAxis)
    Poles = np.roots(yAxis)

    t1 = plt.plot(Zeros.real, Zeros.imag, 'go', ms=10)
    plt.setp(t1, markersize=10.0, markeredgewidth=1.0, markeredgecolor='k', markerfacecolor='g')

    t2 = plt.plot(Poles.real, Poles.imag, 'rx', ms=10)
    plt.setp(t2, markersize=12.0, markeredgewidth=3.0, markeredgecolor='r', markerfacecolor='r')

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    r = 1.2
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])
    ticks = [-1, -.75, -.5, -.25, 0,.25,.5, .75,1]
    plt.xticks(ticks)
    plt.yticks(ticks)

    plt.show()

def HIGHPASS_WINDOWED(FC, M):

    Filter_kernel = []
    for i in range(M):
        if i - M / 2 == 0:
            Filter_kernel.append(2 * np.pi * FC)
        else:
            Filter_kernel.append(np.sin(2 * np.pi * FC * (i - M / 2)) / (i - M / 2))
        Filter_kernel[i] = (Filter_kernel[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M)))

    SUM = 0
    for i in range(M):
        SUM = SUM + Filter_kernel[i]

    for i in range(M):
        Filter_kernel[i] = (Filter_kernel[i] / SUM) * - 1

    Filter_kernel[int(M / 2)] = Filter_kernel[int(M / 2)] + 1

    return Filter_kernel

def LOWPASS_WINDOWED(FC, M):

    Filter_kernel = []
    for i in range(M):
        if i - M / 2 == 0:
            Filter_kernel.append(2 * np.pi * FC)
        elif (i - M / 2 > 0) or (i - M / 2 < 0):
            Filter_kernel.append(np.sin(2 * np.pi * FC * (i - M / 2)) / (i - M / 2))
        Filter_kernel[i] = Filter_kernel[i] * (0.54 - 0.46 * np.cos(2 * np.pi * i / M))

    SUM = 0
    for i in range(M):
        SUM = SUM + Filter_kernel[i]

    for i in range(M):
        Filter_kernel[i] = Filter_kernel[i] / SUM

    return Filter_kernel

def BANDPASS_WINDOWED(FC1, FC2, M):

    Filter_Low = LOWPASS_WINDOWED(FC1, M)
    Filter_High = HIGHPASS_WINDOWED(FC2, M)

    Filter_band = []
    for i in range(M):
        Filter_band.append(Filter_High[i] + Filter_Low[i])

    for i in range(M):
        Filter_band[i] = Filter_band[i] * -1

    Filter_band[int(M / 2)] = Filter_band[int(M / 2)] + 1

    return Filter_band

def MediaMovel(Tam_Media, data):

    Data_Filtro = 0
    data_Output = []
    for i in range(len(data)):
        for k in range(Tam_Media):
            if (i - k) >= 0:
                Data_Filtro += data[i - k]

        Data_Filtro = Data_Filtro / Tam_Media
        data_Output.append(Data_Filtro)
        Data_Filtro = 0

    return data_Output
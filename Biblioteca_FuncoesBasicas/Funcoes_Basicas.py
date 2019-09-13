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
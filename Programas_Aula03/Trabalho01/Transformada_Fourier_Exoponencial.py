import numpy as np
import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb
import matplotlib.pyplot as plt

n = int(input("Valor do expoente: "))
w = (np.pi) / 4
K = 1

Sinal = fb.Exponencial(.5, n)

def Exp_Fourier_Phase(a, w, n):
    Phase = []
    for i in range(n):
        Phase.append(0 - np.arctan((a * np.sin(w * i)) / (1 - (a * np.cos(w * i)))))

    return Phase

def Exp_Fourier_Magnitude(a, w, K, n):
    imag = 1j
    Magnitude = []
    for i in range(n):
        Magnitude.append(K * (1 / (1 - (a * (np.cos(w * i) - (imag * np.sin(w * i)))))))

    return Magnitude

xAxis = np.linspace(0., n, n, endpoint=False)

plt.subplot(3, 1, 1)
plt.suptitle("Exponencial e sua transformada de Fourier (Magnitude e Fase)")
plt.stem(xAxis, Sinal, use_line_collection=True)

plt.subplot(3, 1, 2)
plt.plot(xAxis, Exp_Fourier_Magnitude(.5, w, K, n))

plt.subplot(3, 1, 3)
plt.plot(xAxis, Exp_Fourier_Phase(.5, w, n))

plt.show()

import numpy as np
import Biblioteca_FuncoesBasicas.Funcoes_Basicas as fb

Wo = np.pi / 4

def Magnitude():
    Magnitude = np.roots([1, (-0.5) * np.cos(Wo), 0])
    return Magnitude

def Polos():
    Polos = np.roots([1, -2 * 0.5 * np.cos(Wo), (0.5 ** 2)])
    return Polos

fb.Zplane([1, (-0.5) * np.cos(Wo), 0], [1, -2 * 0.5 * np.cos(Wo), (0.5 ** 2)])


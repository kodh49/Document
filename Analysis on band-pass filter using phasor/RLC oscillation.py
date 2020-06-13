import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

# variable definition
R_1 = 220
R_2 = 100
R_3 = 50
L = 0.1
C = 3.3e-7
w_0 = 1/np.sqrt(L*C)

def H(w, R):
    impedance = ((1/(L*C))-(w**2))
    result = ((R/L)*w)/np.sqrt(((R/L)*w)**2+impedance**2)
    return result

def dB(x):
    return 10*np.log(x)

print("Resonance at "+str(w_0))


def FTF():
    w = np.linspace(100, 10000, 100000) # Domain of a function
    output = H(w, R_1)
    plt.title("Filter Transfer Function")
    plt.plot(w, output, color='k', label="H(ω)")
    plt.legend(fontsize='medium')
    plt.xlabel("Angular Frequency (ω)")
    plt.ylabel("Magnitude")
    plt.axvline(x=w_0, color='r', linestyle='--', linewidth=1)
    plt.show()


def FTF_R():
        w = np.linspace(100, 10000, 100000) # Domain of a function
        output_1 = H(w, R_3)
        output_2 = H(w, R_2)
        output_3 = H(w, R_1)
        plt.title("Filter Transfer Function")
        plt.plot(w, output_1, label="220Ω")
        plt.plot(w, output_2, label="100Ω")
        plt.plot(w, output_3, label="50Ω")
        plt.legend(fontsize='medium')
        plt.xlabel("Angular Frequency (ω)")
        plt.ylabel("Magnitude")
        plt.axvline(x=w_0, color='r', linestyle='--', linewidth=1)
        plt.show()


def ARF():
    w = np.linspace(1000, 8000, 100000) # Domain of a function
    output = dB(H(w, R_1))
    plt.title("Amplitude Response Function")
    plt.plot(w, output, color='k', label="A(ω)")
    plt.legend(fontsize='medium')
    plt.xlabel("Angular Frequency (ω)")
    plt.ylabel("Amplitude (dB)")
    plt.axhline(y=-3, color='r', linestyle='--', linewidth=1)
    plt.show()

def ARF_R():
        w = np.linspace(1000, 8000, 100000) # Domain of a function
        output_1 = dB(H(w, R_3))
        output_2 = dB(H(w, R_2))
        output_3 = dB(H(w, R_1))
        plt.title("Amplitude Response Function")
        plt.plot(w, output_1, label="220Ω")
        plt.plot(w, output_2, label="100Ω")
        plt.plot(w, output_3, label="50Ω")
        plt.legend(fontsize='medium')
        plt.xlabel("Angular Frequency (ω)")
        plt.ylabel("Amplitude (dB)")
        plt.axhline(y=-3, color='r', linestyle='--', linewidth=1)
        plt.show()

FTF()
FTF_R()
ARF()
ARF_R()
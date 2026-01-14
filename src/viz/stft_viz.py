# Visualization using Short-Time-Fourier Transforms
# Use Manim Library to generate animation


import matplotlib.pyplot as plt
from manim import *
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import gaussian

def plot_fft(y, fs, name=None):
    
    wsz = 256*2
    hop = 128
    win = gaussian(wsz, std=4096, sym=True)
    SFT = ShortTimeFFT(win, hop, fs)

    Sy = SFT.stft(y)

    fig1, ax1 = plt.subplots(figsize=(6., 4.))

    if name:
        title = rf"{name} STFT ({SFT.m_num*SFT.T:g}$\,s$ fs={fs})"
    else:
        title = rf"STFT ({SFT.m_num*SFT.T:g}$\,s$ fs={fs})"
    ax1.set_title(title)

    im1 = ax1.imshow(20*np.log10(abs(Sy)), origin='lower', aspect='auto',
                     extent = SFT.extent(len(y)), cmap='viridis')
    
    ax1.set_ylabel("freq (Hz)")
    ax1.set_xlabel("time (seconds)")
    ax1.legend()
    fig1.tight_layout()
    plt.show()



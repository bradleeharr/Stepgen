import librosa
from src.viz.stft_viz import *
import time

def test_Plot_fft():
    dir = "tests/test_assets"
    #file = "Test-Song1.wav"
    file = "Fluffing-a-Duck.mp3"
    #file = "Sneaky-Snitch.mp3"
    y, sr = librosa.load(f"{dir}/{file}")
    plot_fft(y, sr)

    time.sleep(1)


def test_Plot_time():
    dir = "test/test_assets"
    file = "Fluffing-a-Duck.mp3"
    y, sr = librosa.load(f"{dir}/{file}")

    
if __name__ == "__main__":
    test_Plot_fft()
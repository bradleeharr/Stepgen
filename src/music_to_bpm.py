import librosa

def music_file_to_bpm(file):
    y, sr = librosa.load(file)
    print(y)
    print(sr)
    tempo = librosa.feature.tempo(y=y, sr=sr)
    print(f"TEMPO Detected: {tempo}")
    return tempo[0]
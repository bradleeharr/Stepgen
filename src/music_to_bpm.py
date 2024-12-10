import librosa

def music_file_to_bpm(file):
    y, sr = librosa.load(file)
    print(y)
    print(sr)
    return 120
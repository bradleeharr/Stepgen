from src.song import Song

def test_Song_to_file():
    a = Song()
    a.to_stepfile("test_stepfile.sm")

    print("test finished")

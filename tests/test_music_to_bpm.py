import pytest

from src.music_to_bpm import music_file_to_bpm

def test_BPM():
    file = "tests/test_assets/Test-Song.wav"

    bpm = music_file_to_bpm(file)
    assert bpm == pytest.approx(120, 1)

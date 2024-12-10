import pytest

from src.music_to_bpm import music_file_to_bpm

def test_BPM():
    dir = "tests/test_assets"
    files = ["Test-Song1.wav", "Fluffing-a-Duck.mp3", "Sneaky-Snitch.mp3"]
    expected_bpms = [120, 123, 87]
    bpm_tolerance = 0.02

    est_bpms = []
    for file in files:
        est_bpms.append(music_file_to_bpm(f"{dir}/{file}"))
    
    for est_bpm, expected_bpm in zip(est_bpms, expected_bpms):
        print(f"Estimated: {est_bpm} | Actual {expected_bpm}")
        assert est_bpm == pytest.approx(expected_bpm, bpm_tolerance)


from src.stepfilenotes import StepFileNotes
from src.stepfileenums import ModeType, Difficulty, NoteType, Direction

def test_Notes_to_file():
    uut = StepFileNotes()
    assert uut.mode_type == ModeType.DANCE_SINGLE
    assert uut.difficulty == Difficulty.EASY
    assert uut.difficulty_level == 0
    
    uut.add_note(NoteType.QUARTER)

def test_Parse_Wav_File():
    a = StepFile()
    
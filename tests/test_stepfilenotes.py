from src.stepfilenotes import StepFileNotes
from src.stepfileenums import ModeType, Difficulty, NoteType, Direction

def test_Notes_to_file():
    uut = StepFileNotes()
    assert uut.mode_type == ModeType.DANCE_SINGLE
    assert uut.difficulty == Difficulty.EASY
    assert uut.difficulty_level == 0
    
    uut.add_note(NoteType.QUARTER, [Direction.DOWN])
    uut.add_rest(NoteType.QUARTER)
    uut.add_note(NoteType.QUARTER, [Direction.LEFT])

    [print("\n",row) for row in uut.beatsList]
    assert uut.beatsList == [
        [[0, 0, 1, 0], [0, 0, 1, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0,]],
        [[1, 0, 0, 0], [1, 0, 0, 0,]]
    ]

def test_Parse_Wav_File():
    pass
    #a = StepFile()
    
if __name__ == '__main__':
    test_Notes_to_file()
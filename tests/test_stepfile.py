from src.stepfile import StepFile

from src.stepfileenums import NoteType, Direction




def test_Song_to_file():
    a = StepFile()
    a.header.title = "Test Step File"
    a.header.artist = "TestArtist"
    
    a.notes.add_note(NoteType.QUARTER, [Direction.DOWN, Direction.UP])
    a.notes.add_note(NoteType.QUARTER, [Direction.UP])
    a.notes.add_note(NoteType.QUARTER, [Direction.DOWN])
    a.notes.add_note(NoteType.QUARTER, [Direction.LEFT, Direction.RIGHT])

    a.to_stepfile("test_stepfile.sm")

    print("test finished")


def test_Parse_Wav_File():
    a = StepFile()
    
from src.stepfile import StepFile

def test_Song_to_file():
    a = StepFile()
    a.header.title = "Test Step File"
    a.header.artist = "TestArtist"
    
    a.to_stepfile("test_stepfile.sm")

    print("test finished")

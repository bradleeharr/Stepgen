
from src.stepfileenums import StepFileType
from src.stepfileheader import StepFileHeader
from src.stepfilenotes import StepFileNotes



class StepFile:
    def __init__(self):
        self.animation_file = None # AVI
        self.audio_file = None   # OGG
        self.banner_file = None # PNG
        self.step_file = StepFileType.UNKNOWN # .STEP   

        self.header = StepFileHeader()
        self.notes = StepFileNotes()

        self.album_name = "InitAlbum" # This is the output folder name that can hold a collection of songs which will themselves be folders
        self.song_name = "Title" # This is the song folder name that holds the the mp3, stepfile, and images/animations
        

    def to_stepfile(self, out_file):
        with open(out_file, "w") as f:
            f.write(self.header.to_file_format())
            f.write(self.notes.to_file_format()) 
        
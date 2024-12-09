
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

    def to_stepfile(self, out_file):
        with open(out_file, "w") as f:
            f.write(self.header.to_file_format())
            f.write(self.notes.to_file_format()) 
        
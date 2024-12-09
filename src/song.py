from enum import Enum

from stepfileheader import StepFileHeader
from stepfilenotes import StepFileNotes

class StepFileType(Enum):
    SM = "StepMania Simfile"
    SSC = "StepMania Spinal Shark Collective Format"
    UNKNOWN = "Unknown"


class Song:
    def __init__(self):
        self.animation_file = None # AVI
        self.audio_file = None   # OGG
        self.banner_file = None # PNG
        self.step_file = StepFileType.UNKNOWN # .STEP   

        self.header = StepFileHeader()
        self.notes = StepFileNotes()

    def to_stepfile(self, out_file):
        with open(out_file, "w") as f:
            for key, value in self.header.items():
                f.write(f"#{key}:{value};\n")
            
        
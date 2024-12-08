from enum import Enum

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


        self.header = {
            "TITLE": "",
            "SUBTITLE" : "",
            "ARTIST" : "",

        }
        self.title=""
        self.subtitle=""
        self.artist=""
        self.titletranslit="" 
        #transliteration, alternative or romanized version of the title for easier readability
        self.subtitletranslit=""
        self.artisttranslit=""
        self.genre=""
        self.credit=""
        self.banner=""
        self.background=""
        self.lyricspath=""
        self.cdtitle=""
        self.music=""
        self.offset=-1
        self.samplestart=-1
        self.selectable=None
        self.displaybpm=None
        self.bpms=[]
        self.stops=[]
        self.timesignatures=[]
        self.bgchanges=[]
        self.keysounds=[]

        self.out_file = "TEST_out_stepfile"

    def to_stepfile(self, out_file):
        with open(out_file, "w") as f:
            for key, value in self.header.items():
                f.write(f"#{key}:{value};\n")
            
        
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

        self.title=""
        self.subtitle=""
        self.artist=""
        self.titletranslit=""
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


        

# Would be cool to add an option for lyrics popping up
# default.lua script seems like you can animate backgrounds and stuff


# Manim for animations maybe?

# Visualizer would be an interesting additiojn
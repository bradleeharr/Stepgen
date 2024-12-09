from enum import Enum

class StepFileType(Enum):
    SM = "StepMania Simfile"
    SSC = "StepMania Spinal Shark Collective Format"
    UNKNOWN = "Unknown"

class ModeType(Enum):
    DANCE_SINGLE = "dance-single"
    DANCE_DOUBLE = "dance-double"

class Difficulty(Enum):
    Easy = 0
    Hard = 1

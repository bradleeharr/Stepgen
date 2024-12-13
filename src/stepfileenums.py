from enum import Enum

class StepFileType(Enum):
    SM = "StepMania Simfile"
    SSC = "StepMania Spinal Shark Collective Format"
    UNKNOWN = "Unknown"

class ModeType(Enum):
    DANCE_SINGLE = "dance-single"
    DANCE_DOUBLE = "dance-double"

class Difficulty(Enum):
    EASY = 0
    HARD = 1


class NoteType(Enum):
    HALF = 0
    QUARTER = 1
    EIGHTH = 2

class Direction(Enum):
    NONE = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    RIGHT = 4 
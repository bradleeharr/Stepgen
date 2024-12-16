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
    LEFT = 0
    UP = 1
    DOWN = 2
    RIGHT = 3 
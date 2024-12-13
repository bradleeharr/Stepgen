from typing import List
from stepfileenums import NoteType, Direction

from src.stepfileenums import ModeType, Difficulty

class StepFileNotes:
    def __init__(self):
        self.mode_type = ModeType.DANCE_SINGLE
        self.difficulty = Difficulty.EASY
        self.difficulty_level = 0
        self.beatsList = []


    def add_note(self, note: NoteType, directions: List[Direction]) -> None:
        self.beatsList.append()
        
    def add_rest(self, note: NoteType):
        match note:
            case NoteType.HALF:
                self.beatsList.append([0, 0, 0, 0])
                self.beatsList.append([0, 0, 0, 0])
                self.beatsList.append([0, 0, 0, 0])
                self.beatsList.append([0, 0, 0, 0])
            case NoteType.QUARTER:
                self.beatsList.append([0, 0, 0, 0])
                self.beatsList.append([0, 0, 0, 0])
            case NoteType.EIGHTH:
                self.beatsList.append([0, 0, 0, 0])
            case _:
                raise NotImplementedError("NoteType to add_rest() not implemented")

    def get_beats_list_str(self):
        out_str = ""
        for line in self.beatsList:
            out_str = out_str + line
        return out_str

    def to_file_format(self):
        out_str = \
        f"""//---------------{self.mode_type.value} - ----------------
        #NOTES:
             {self.mode_type.value}:
             :
             {self.difficulty.name}:
             {self.difficulty_level}:
             :
        """
        out_str = out_str + self.get_beats_list_str() + ";\n\n"
        return out_str

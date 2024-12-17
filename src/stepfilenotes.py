from typing import List
from src.stepfileenums import NoteType, Direction, ModeType, Difficulty

class StepFileNotes:
    def __init__(self):
        self.mode_type = ModeType.DANCE_SINGLE
        self.difficulty = Difficulty.EASY
        self.difficulty_level = 0
        self.beatsList = []



    def add_note(self, note: NoteType, directions: List[Direction]) -> None:

        row = [0, 0, 0, 0]
        for direction in directions:
            idx = direction.value
            row[idx] = 1

        match note:
            case NoteType.HALF:
                self.beatsList.append([row]*4)
            case NoteType.QUARTER:
                self.beatsList.append([row]*2)
            case NoteType.EIGHTH:
                self.beatsList.append([row])
            case _:
                raise NotImplementedError("NoteType to add_note() not implemented")
    
    def add_rest(self, note: NoteType):
        self.add_note(note, [])



    def get_beats_list_str(self):
        out_str = ""
        for group in self.beatsList:
            for line in group:
                    out_str = out_str + "".join(map(str, line)) + ",\n\t"
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

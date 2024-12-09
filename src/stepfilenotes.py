from src.stepfileenums import ModeType, Difficulty

class StepFileNotes:
    def __init__(self):
        self.mode_type = ModeType.DANCE_SINGLE
        self.difficulty = Difficulty.Easy
        self.difficulty_level = 0
        self.beatsList = []

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
        for line in self.beatsList:
            out_str = out_str + line 

        out_str = out_str + ";\n\n"
        return out_str


class StepFileHeader:
    def __init__(self):
        self.title = ""
        self.subtitle = ""
        self.artist = ""
        self.title_translit = ""
        self.subtitle_translit = ""
        self.artist_translit = ""
        self.genre = ""
        self.credit = ""
        self.banner = ""
        self.background = ""
        self.lyrics_path = ""
        self.cd_title = ""
        self.music = ""
        self.offset = ""
        self.sample_start = ""
        self.selectable = ""
        self.display_bpm = ""
        self.bpms = []
        self.stops = []
        self.time_signatures = []
        self.bg_changes = []
        self.key_sounds = []
    
    def to_file_format(self):
        fields = vars(self)
        out_lines = []
        for key in fields:
            value = getattr(self, key, None)
            line = f"#{key.upper().replace("_","")}:{value};"
            out_lines.append(line)
        
        out_lines.append("")
        return "\n".join(out_lines)


    

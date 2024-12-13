
class StepFileHeader:
    def __init__(self):
        self.title = "Untitled"
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
        self.music = "Music.ogg"
        self.offset = 0.000
        self.sample_start = ""
        self.selectable = "Yes"
        self.display_bpm = ""
        self.bpms = []
        self.stops = []
        self.time_signatures = []
        self.bg_changes = []
        self.key_sounds = []
    
    #TITLE:Untitled;
    #SUBTITLE:;
    #ARTIST:;
    #TITLETRANSLIT:;
    #SUBTITLETRANSLIT:;
    #ARTISTTRANSLIT:;
    #CREDIT:;
    #BANNER:;
    #BACKGROUND:;
    #LYRICSPATH:;
    #CDTITLE:;
    #MUSIC:Music.ogg;
    #OFFSET:0.000;
    #SAMPLESTART:40.859;
    #SAMPLELENGTH:10.000;
    #SELECTABLE:YES;

    def to_file_format(self):
        fields = vars(self)
        out_lines = []
        for key in fields:
            value = getattr(self, key, None)
            line = f"#{key.upper().replace("_","")}:{value};"
            out_lines.append(line)
        
        out_lines.append("")
        return "\n".join(out_lines)


    

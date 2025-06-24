
def color(codes: list[str] | str) -> str:
    if isinstance(codes, str):
        codes = [codes]
    return f"\033[{';'.join(codes)}m"

CLEAR = color('0')
BOLD = '1'
ITALIC = '3'
UNDERLINE = '4'

class FG:
    """Foreground color codes."""
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'
    BRIGHT_BLACK = '90'
    BRIGHT_RED = '91'
    BRIGHT_GREEN = '92'
    BRIGHT_YELLOW = '93'
    BRIGHT_BLUE = '94'
    BRIGHT_MAGENTA = '95'
    BRIGHT_CYAN = '96'
    BRIGHT_WHITE = '97'

class BG:
    """Background color codes."""
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'
    BRIGHT_BLACK = '100'
    BRIGHT_RED = '101'
    BRIGHT_GREEN = '102'
    BRIGHT_YELLOW = '103'
    BRIGHT_BLUE = '104'
    BRIGHT_MAGENTA = '105'
    BRIGHT_CYAN = '106'
    BRIGHT_WHITE = '107'

def colorize(text, fg=None, bg=None, style=None):
    codes = []
    if style:
        codes.append(style)
    if fg:
        codes.append(fg)
    if bg:
        codes.append(bg)
    return f"{color(codes)}{text}{CLEAR}"
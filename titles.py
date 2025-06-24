
from style import *

MAIN = colorize(r"""
      .o8      .    
     "888    .o8   
 .oooo888  .o888oo 
d88' `888    888    
888   888    888    dubis' terminal
888   888    888 .    -h for help
`Y8bod88P"   "888"
""", FG.GREEN)

CHAT = colorize(r"""
          oooo                      .   
          `888                    .o8   
 .ooooo.   888 .oo.    .oooo.   .o888oo 
d88' `"Y8  888P"Y88b  `P  )88b    888    -x to exit
888        888   888   .oP"888    888    -r to reset
888   .o8  888   888  d8(  888    888 .  -m to change the model
`Y8bod8P' o888o o888o `Y888""8o   "888"  default: gpt-4.1-mini
""", FG.MAGENTA)

MATH = colorize(r"""
                               .   oooo        
                             .o8   `888        
ooo. .oo.  .oo.    .oooo.  .o888oo  888 .oo.   
`888P"Y88bP"Y88b  `P  )88b   888    888P"Y88b  
 888   888   888   .oP"888   888    888   888  
 888   888   888  d8(  888   888 .  888   888   -x to exit
o888o o888o o888o `Y888""8o  "888" o888o o888o  -r to reset
""", FG.RED)
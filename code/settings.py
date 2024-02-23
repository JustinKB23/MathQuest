"""level_map = [
"                            ",
"                            ",
"  A                   A     ",
" XX    XXX            XX    ",
" XX P          M            ",
" XXXX         XX         XX ",
" XXXX       XX              ",
" XX    X  XXXX    XX  XXA   ",
"       X  XXXX    XX  XXX   ",
"    XXXX  XXXXXX  XX  XXXX  ",
"XXXXXXXX  XXXXXX  XX  XXXX  "]"""

level_map = [
"XXXXXX                                                                                                                                                           XXXXX",
"XXXXXX                  XX                                   A                                                                                                   XXXXX",
"XXXXXX           XXXX          XXXX  X   X    XX XX    XXXXXXXX                                          X                                                       XXXXX",
"XXXXXX                                                                               A                  X X                                                      XXXXX",
"XXXXXX       XXX                                                                   XXXXXXX     XXX     X   XXXXXXX                                               XXXXX",
"XXXXXX  X                                                                       X         X   X   X   X           X                                              XXXXX",
"XXXXXX                    X                      XX    XX                    X             XXX     XXX             X                                             XXXXX",
"XXXXXX   XXX              X    X               XXXX    XX                 X                                         X                          X                 XXXXX",
"XXXXXX         M    XX   XX   XX              XXXXX    XX  XX          X                                             X                 X      XXX   XX           XXXXX",
"XXXXXX   P     XX  XXX   XX   XXX            XXXXXX    XX  XX       X                                                 X    XX   XX    XXX    XXXXX  XX    A      XXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXX    XX  XXXXXXXXXX                                                  XXXXXX   XXXXXXXXXXXXXXXXXX  XX  XXXXXXXXXXXXXX"]

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
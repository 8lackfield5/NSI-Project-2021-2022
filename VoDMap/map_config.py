### Variables: "X" = Tile ; "H" = Tile cachée ; "L" = Pièce (pickup --> +10 coins, par exemple) ; "P" = Pique ; "M" = Marchand ; "E" = Ennemi ; "-" = Chemin d'un ennemi ; "C" = Piques cachés ; "N" = Niveau terminé

map_list = [

[ #Map démo qui a pour but de tester le personnage
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXX        XXXXXXXXXX',
'XXXXXXX                  HH LX',
'XXXXXX        XXX         H XX',
'XXXXX               XXX   XXXX',
'XXX       XXX              XXX',
'X                    XXX     N',
'XS     XXXXXXXXXPPPPPXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 1 (Il y a 8 niveaux par monde)
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXX              XXXXXXXX',
'XXXX                      XXXX',
'X                           XX',
'X                  XX        N',
'XS        PP      XXXXXXX    N',
'XXXXXXPPXXXXXXXXPPXXXXXXXXXXXX',  ### Placer des piques dans les cases "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 2
'                             N',
'                             N',
'                             N',
'                             N',
'             CC              N',
'                             N',
'         XXX                 N',
'   XXXX                XX    N',
'S                  XX  XXX   N',
'XXPPPPPPPPPPXXXXXPPXXPPXXXX  N', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,



[ #Monde 1 Niveau 3
'X                            X',
'X                XXX         X',
'X                            N',
'X            XXX             N',
'X                            X',
'X        XXX           XXX   X',
'X                            X',
'X    XXX                     X',
'X                            X',
'XS XPPPPPPPPPPPPPPPPPPPPPXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 4
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXHHHHHHLXXXXXXXXXXXXXXXXXXXX',
'XHHHHH---EXXXXXX          XXXX',
'XLHHHHXXXX                   X',
'XXXHH                        N',
'XXXX                         N',
'XX     XXX                   X',
'X                    XXX     X', ### Placer un ennemi dans la case "E"
'XS XXXX---------E---XXXXX    X', ### Les cases "-" representent la zone de mouvement de l'ennemi
'XXXXXXXXXXXXXXXXXXXXXXXXXPPXXX', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Monde dans lequel le personnage peut interagir avec le marchand
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXX XXX      XXXXXXXXXX',
'XXXXXXXX    X         XXXXXXXX',
'X                     X      N',
'X                     X      N',
'X     XXX   XXXXXXX          X',
'X           MMMMMMXX   XX    X', ### Placer le marchand dans les cases "M"
'XS XX       MMMMMMXXXXXXXX  XX', ### "M"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Monde 1 Niveau 5
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'                             X',
'                             X',
'                             X',
'                             X',
'                  XXX        X',
'S   XX                       N',
'X-----E-X    XXXX  -----E----N', ### "E" et "-"
'XXXXXXXXXPP       PPXXXXXXXXXX', ### "P"
'XXXXXXXXXXXPPPPPPPXXXXXXXXXXXX'] ### "P"
,


[ #Monde 1 Niveau 6
'                             N',
'                             N',
'                             N',
'                  ---E--     N',
'           XX     XXXXXX     N',
'                             N',
'             XXXX            N',
'                   X    X    N',
'S CC  CC XXXCCCCCCCCCCCCCX   N', ### Placer des piques cachés dans les cases "C"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 7
'                             N',
'                             N',
' CC                          N',
' XX     XXXX                 N',
'                             N',
'    XXXXCCC   XX  XX  XX  XXXX',
'S        XXX                  ',
'XX                            ',
'XXXPPCCPPCCPPCCPPCCPPCCPPCCPPC',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 8
'C                            X',
'XX                           N',
'XXXC                    CCCCCX',
'XXXXX         CXXXX   XXXXXXXX',
'S        CXXXX       XX      N',
'XC   XXXXX    CCCC X  X     XX',
'XX            XXXX         CXX',
'XXXC                      CXXX',
'XXXXC                 XXXXX  N',
'XXXXXC---E-----E-----E-----E-N',
'XXXXXXCXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Le marchand vends de meilleures marchandises qu'a la première rencontre
'X                            N',
'X                          XXX',
'X                        XXXXX',
'X                      XXXXXXX',
'X                    XXXXXXXXX',
'XX                XXXXXXXXXXXX',
'XXX         XXXXXXXXXXXXXXXXXX',
'XXXX   XX   MMMMMMXXXXXXXXXXXX',
'X           MMMMMMXXXXXXXXXXXX',
'XS   XXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Monde 2 Niveau 1
'S                            X',
'XX        C  -E---E-         X',
'XXXC     XX  XXXXXXX         X',
'XXXX                XXXX     X',
'XXXXX                        N',
'XXX            C    C       XX',
'XXX XXXC---E---XXPPXX--E---XXX',
'XXX XXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXX XX     XXXX     XXX     XX',
'XXX-----E--------E-------E---N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 2
'X                            X',
'X   C--E--C----E---C-E-C     X',
'X  XXXXXXXXXXXXXXXXXXXXX     X',
'X  X                    XX   X',
'XSX                          X',
'X         C---E---CCPCC  CXX X',
'X     C X XXXXXXXXXXXXXXXXXXXX',
'X   C XX                   XXX',
'X   XX                      XX',
'X-E---------E----E----E----E--N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 3
'X                            X',
'X                            X',
'X                            X',
'X          CXXC              X',
'X        CXX  XXC            X',
'X       XX      XX           X',
'X                            X',
'XSCXXXX    -E--     XXC      X',
'XX         XXXX       XX     X',
'--E----E----E----E----E----E-N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 4
'X                           SX',
'X                           XX',
'X                         CXXX',
'X                        XXXXX',
'X    --E-----E-----E--CXXXXXXX',
'X    XXXXXXXXXXXXXXXXXXXXXXXXX',
'X  XX                        X',
'X--E-----C------E--C-------  X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXX  X',
'N                            X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Le marchand vends les meilleures marchandises du jeu
'XS                           X',
'XX                           X',
'XXX                          X',
'XXXX                         X',
'XXXXX                        N',
'XXXXXXXXXXXX                 N',
'XXXXXXXXXXXXX                X',
'XXXXXMMMMMM  X              XX',
'XXXXXMMMMMM                XXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 5
'X                           XX',
'X    ---E-----E-----E---    XX',
'X    XXXXXXXXXXXXXXXXXXX    XX',
'X   X                   X   XX',
'X  X                     XX  X',
'XS    C    C    C    C       N',
'XX    XXXXXXXXXXXXXXXXXXX   XX',
'XXX                        XXX',
'XXXX                      XXXX',
'XXXXXP   P   P P   P   PXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 6
'                             X',
'                             X',
'                C            X',
'   -E-E-       XXC           X',
'   XXXXX     CXXXX           X',
'S            XXXXXXC         X',
'XX         CXXXXXXXX         X',
'XXXC       XXXXXXXXXXC       X',
'XXXX     CXXXXXXXXXXXX     C N',
'XXXXXE--EXXXXXXXXXXXXXXE--EXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


world2_lvl7 = [ #Monde 2 Niveau 7
'X                     XXXXXXXX',
'X          XXC   C    X      X',
'X         XXXXX       H CXXXHX',
'X        XXXXXXXCCXHHXXXXXXXHX',
'X      CXXLLLHHHXXCCCLXXX    X',
'X      XXXX--E-HHHXXXXXX  XXXX',
'X     XXXXXXXXXHHHHHHHHH     N',
'X      XXXXXXXXXXXXXXXXXXXXXXX',
'XS  X   XX   XX   XX   XX    X',
'XXXXX.-E----E----E----E----E--N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

]

world2_lvl8 = [ #Monde 2 Niveau 8
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ']






bonus_lvl = [ #Niveau Bonus
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ']


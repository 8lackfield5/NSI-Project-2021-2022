### Variables: "X" = Tile ;; "P" = Pique ; "M" = Marchand ; "E" = Ennemi ; "-" = Reverse d'un enemie ; "C" = Piques cachés ; "N" = Niveau terminé

map_list = [

[ #Map démo qui a pour but de tester le personnage
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXX       XXXXXXXXX',
'XXXXXXXXXXXX           XXXXXXX',
'XXXXXXX                      X',
'XXXXXX        XXX           XX',
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
'X                            N',
'X                            N',
'X                            N',
'X                            N',
'X            CC              N',
'X                            N',
'X        XXX                 N',
'X   XXX                XX    N',
'XS                 XX  XXX   N',
'XXXPPPPPPPPPPXXXXPPXXPPXXXX  N', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,



[ #Monde 1 Niveau 3
'X                            X',
'X                XXX         X',
'X                            N',
'X            XXX             N',
'X                            N',
'X        XXX           XXX   X',
'X                            X',
'X    XXX                     X',
'X                            X',
'XS XPPPPPPPPPPPPPPPPPPPPPPPPPX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 4
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXX       XXXXXXXXXXXXXXXXXXXX',
'X     -E -XXXXXX          XXXX',
'X     XXXX                   X',
'XXX                          N',
'XXXX                         N',
'XX     XXX                   N',
'X                    XXX     N', ### Placer un ennemi dans la case "E"
'XS XXXX-        E  -XXXXX    N', ### Les cases "-" representent la zone de mouvement de l'ennemi
'XXXXXXXXXXXXXXXXXXXXXXXXXPPXXX', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Monde dans lequel le personnage peut interagir avec le marchand
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXX XXX      XXXXXXXXXX',
'XXXXXXXX    X         XXXXXXXX',
'X                     X      N',
'X           XXXXXXX   X      N',
'X     XXX                    N',
'X                 XX   XX    N', ### Placer le marchand dans les cases "M"
'XS XX           MBXXXXXXXX  XX', ### "M"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Monde 1 Niveau 5
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XX                           X',
'X                            X',
'X                            X',
'X                            N',
'X                 XXX        N',
'XS    X                      N',
'XX-   E-X    XXXX   -   E    -N', ### "E" et "-"
'XXXXXXXXXPP       PPXXXXXXXXXX', ### "P"
'XXXXXXXXXXXPPPPPPPXXXXXXXXXXXX'] ### "P"
,


[ #Monde 1 Niveau 6
'X                            N',
'X                            N',
'X                            N',
'X                 -  E -     N',
'X          XX     XXXXXX     N',
'X                            N',
'X            XXXX            N',
'X                  X    X    N',
'XS CC  CCXXXCCCCCCCCCCCCCX   N', ### Placer des piques cachés dans les cases "C"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 7
'X                            N',
'X                            N',
'XCC                          N',
'XXX     XXXX                 N',
'X                            N',
'X   XXXXCCC   XX  XX  XX  XXXX',
'XS       XXX                  ',
'XX                            ',
'XXXPPCCPPCCPPCCPPCCPPCCPPCCPPC',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 8
'C                            N',
'XX                           N',
'XXX                    CCCCCX',
'XX            CXXXX   XXXXXXXX',
'XS       CXXXX       XX      N',
'XXC  XXXXX    CCCC X  X     XX',
'XXX           XXXX         CXX',
'XXXXC                     CXXX',
'XXXXXC                XXXXX   N',
'XXXXXXC- E     E     E     E -N',
'XXXXXXCXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Le marchand vends de meilleures marchandises qu'a la première rencontre
'X                            N',
'X                            N',
'X                          XXX',
'X                       XXXXXX',
'X                    XXXXXXXXX',
'XX              XXXXXXXXXXXXX',
'XXX         XXX   XXXXXXXXXXXX',
'XXXX   XX         XXXXXXXXXXXX',
'X               MBXXXXXXXXXXXX',
'XS   XXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Monde 2 Niveau 1
'XS                           X',
'XX        C  -E   E-         X',
'XXXC     XX  XXXXXXX         X',
'XXXX                XXXX     X',
'XXXXX                        N',
'XXX            C    C       XX',
'XXX XXXC-  E  -XXPPXX- E  -XXX',
'XXX XXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXX XX     XXXX     XXX     XX',
'XXX-    E        E       E   -N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 2
'X                            X',
'X    C- E  C  E  C  E -C     X',
'X   XXXXXXXXXXXXXXXXXXXX     X',
'X  X                    XX   X',
'XSX                          X',
'XX        C-  E  -CCPCC  CXX X',
'X     C X XXXXXXXXXXXXXXXXXXXX',
'X   C XX                   XXX',
'X   XX                      XX',
'X-E        E    E    E    E -N',
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
'XSCXXXX    -E -     XXC      X',
'XXX        XXXX       XX     X',
'- E    E    E    E    E    E-N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 4S
'                             XX',
'X                            XX',
'X                           SX',
'X                         CXXX',
'X                        XXXXX',
'X    - E     E     E -CXXXXXXX',
'X    XXXXXXXXXXXXXXXXXXXXXXXXX',
'X  XX                        X',
'X- E     C      E  C      -  X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXX  X',
'N                            X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Le marchand vends les meilleures marchandises du jeu
'XX                           X',
'XX                           X',
'XXS                          X',
'XXXX                         X',
'XXXXX                        N',
'XXXXXXXXXXXX                 N',
'XXXXX     XX                 X',
'XXXXX                       XX',
'XXXXX  MB                  XXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 5
'X                           XX',
'X    -  E     E     E C-    XX',
'X    XXXXXXXXXXXXXXXXXXXC   XX',
'X   X                   XC  XX',
'X  X                     XX  X',
'XS    C    C    C    C       N',
'XX    XXXXXXXXXXXXXXXXXXX   XX',
'XXX                        XXX',
'XXXX                      XXXX',
'XXXXXP   P   P P   P   PXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 6
'X                            X',
'X                            X',
'X               C            X',
'X  -E  -       XXC           X',
'X  XXXXX     CXXXX           X',
'XS           XXXXXXC         X',
'XX         CXXXXXXXX         X',
'XXXC       XXXXXXXXXXC       X',
'XXXX     CXXXXXXXXXXXX     C N',
'XXXXX-E -XXXXXXXXXXXXXX- E-XXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 7
'X                     XXXXXXXX',
'X          XXC   C    X      X',
'X         XXXXX         CXXXXX',
'X        XXXXXXXCCX  XXXXXXXXX',
'X      CXXXXCCC       XXX    X',
'X      XXXX- E  - XXXXXX  XXXX',
'X     XXXXXXXXX              N',
'X      XXXXXXXXXXXXXXXXXXXXXXX',
'XS  X   XX   XX   XX   XX    X',
'XXXXX.-E   E    E    E    E -N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Niveau de fin de jeu, il ne sert à rien
'                           X',
'                           X',
'                           X',
'                           X',
'                           X',
'  XHHXXHH                  X',
' X                         X',
'X    XXX                   X',
'   XXXXXX                XXX',
'  XXXXXXXXXXXXXXXXXXXXXXXXXN',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']

]

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


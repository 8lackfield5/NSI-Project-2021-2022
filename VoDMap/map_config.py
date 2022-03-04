#TO-DO: 


### Variables: "P" = Pique ; "M" = Marchand ; "E" = Ennemi ; "-" = Chemin d'un ennemi ; "C" = Piques cachés ; "N" = Niveau terminé

demo_lvl = [ #Map démo qui a pour but de tester le personnage
'                             N',
'                             N',
'                             N',
'                             N',
'                             N',
'              XXX            N',
'                    XXX      N',
'          XXX                N',
'                     XXX     N',
'      XXXXXXXXXXPPPPPXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl1 = [ #Monde 1 Niveau 1 (Il y a 8 niveaux par monde)
'                             N',
'                             N',
'                             N',
'                             N',
'                             N',
'                             N',
'                             N',
'                    XX       N',
'                  XXXXXXX    N',
'XXXXXXPPXXXXXXXXPPXXXXXXXXXXXX',  ### Placer des piques dans les cases "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl2 = [ #Monde 1 Niveau 2
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'        XXX                 N',
'  XXXX                XX    N',
'S                 XX  XXX   N',
'XPPPPPPPPPPXXXXXPPXXPPXXXX  N', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl3 = [ #Monde 1 Niveau 3
'                            N',
'                XXX         N',
'                            N',
'            XXX             N',
'         C                  N',
'        XXX           XXX   N',
'                            N',
'    XXX                     N',
'                            N',
'  XPPPPPPPPPPPPPPPPPPPPPXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl4 = [ #Monde 1 Niveau 4
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'      XXX                   N',
'                    XXX     N', ### Placer un ennemi dans la case "E"
'  XXXX---------E---XXXXX    N', ### Les cases "-" representent la zone de mouvement de l'ennemi
'XXXXXXXXXXXXXXXXXXXXXXXXPPXXX', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX']






merchant_lvl1 = [ #Monde dans lequel le personnage peut interagir avec le marchand
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'     XXX   XXXXXX           N',
'           MMMMMM     XX    N', ### Placer le marchand dans les cases "M"
'  XX       MMMMMM    XXXX  XX', ### "M"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX']






world1_lvl5 = [ #Monde 1 Niveau 5
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'                            N',
'                 XXX        N',
'    XX                      N',
'X-----E-X   XXXX  -----E----N', ### "E" et "-"
'XXXXXXXXXPP      PPXXXXXXXXXX', ### "P"
'XXXXXXXXXXXPPPPPPXXXXXXXXXXXX'] ### "P"



world1_lvl6 = [ #Monde 1 Niveau 6
'                            N',
'                            N',
'                            N',
'                 ---E--     N',
'          XX     XXXXXX     N',
'                            N',
'            XXXX            N',
'                  X    X    N',
'  CC  CC XXXCCCCCCCCCCCCCX  N', ### Placer des piques cachés dans les cases "C"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl7 = [ #Monde 1 Niveau 7
'                            N',
'                            N',
' CC                         N',
' XX     XXXX                N',
'                            N',
'    XXXXCCC   XX  XX  XX  XXX',
'        XXX                  ',
' XX                          ',
' CCPPCCPPCCPPCCPPCCPPCCPPCCPP',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl8 = [ #Monde 1 Niveau 8
'                            N',
'                            N',
'CCCCCC                CCCCCCX',
'XXXXXX        CXXXX   XXXXXXX',
'         CXXXX       XX     N',
'XC   XXXXX    CCCC X  X    XX',
'XX            XXXX        CXX',
'XXXC                     CXXX',
'XXXXC               XXXXXX  N',
'XXXXXC --E--E--E--E--E--E---N',
'XXXXXXCXXXXXXXXXXXXXXXXXXXXX']






merchant_lvl2 = [ #Le marchand vends de meilleures marchandises qu'a la première rencontre
'                            ',
'                          XX',
'                        XXXX',
'                      XXXXXX',
'                    XXXXXXXX',
'X                 XXXXXXXXXX',
'XX         XXXXXXXXXXXXXXXXX',
'XXX    XX  MMMMMMXXXXXXXXXXX',
'           MMMMMMXXXXXXXXXXX',
'    XXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']






world2_lvl1 = [ #Monde 2 Niveau 1
'                            ',
'XX        C  -E---E-        ',
'  XC     XX  XXXXXXX        ',
'   X                XXXX    ',
'    XC                      ',
'     X         C    C      X',
'      XC---E---XXPPXX--E--X ',
'       XXXXXXXX  XX  XXXXX  ',
'                            ',
'                            ',
'                            ']



world2_lvl2 = [ #Monde 2 Niveau 2
'                           X',
'    C--E--C----E---C-E-C   X',
'   XXXXXXXXXXXXXXXXXXXXX   X',
'  X                     X  X',
' X                         X',
'X         C---E---CCPCC  CXX',
'      C XXXXXXXXXXXXXXXXXXXX',
'    C XX                   X',
'    XX                     X',
'-E---------E----E----E----E-',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world2_lvl3 = [ #Monde 2 Niveau 3
'                           X',
'                           X',
'                           X',
'           CXXC            X',
'         CXX  XXC          X',
'        XX      XX         X',
'                           X',
'   CXX     --E-     XXC    X',
'  XX       XXXX       XX   X',
'--E----E----E----E----E----E',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world2_lvl4 = [ #Monde 2 Niveau 4
'                            ',
'                           X',
'                         CXX',
'                       XXXXX',
'   --E-----E-----E--CXXXXXXX',
'   XXXXXXXXXXXXXXXXXXXXXXXXX',
' XX                        X',
'-E-----C------E--C-------  X',
'XXXXXXXXXXXXXXXXXXXXXXXXX  X',
'                           X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



merchant_lvl3 = [ #Le marchand vends les meilleures marchandises du jeu 
'                            ',
'X                           ',
'XX                          ',
'XXX                         ',
'XXXX                        ',
'XXXXXXXXXXXX                ',
'XXXXXXXXXXXXX              X',
'XXXXXMMMMMM  X            XX',
'XXXXXMMMMMM              XXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world2_lvl5 = [ #Monde 2 Niveau 5
'                           X ',
'    ---E-----E-----E---    X ',
'    XXXXXXXXXXXXXXXXXXX    X ',
'   X                   X   X ',
'  X                     XX   ',
'     C    C    C    C       N',
'X    XXXXXXXXXXXXXXXXXXX   XX',
'XX                        XXX',
'XXX                      XXXX',
'XXXX P  P  P  P  P  P  PXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world2_lvl6 = [ #Monde 2 Niveau 6
'                            ',
'                            ',
'                C           ',
'   -E-E-       XXC          ',
'   XXXXX     CX  X          ',
'             X    XC        ',
'XX         CX      X        ',
'  X        X        XC      ',
'   X     CX          X      ',
'    XE--EX            XE--EX',
'     XXXX              XXXX ']



world2_lvl7 = [ #Monde 2 Niveau 7
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
### Variables: "P" = Pieux ; "M" = Marchand ; "E" = Ennemi ; "-" = Chemin d'un ennemi ; "C" = Pieux cachés

demo_lvl = [ #Map démo qui a pour but de tester le personnage
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'              XXX           ',
'                    XXX     ',
'          XXX               ',
'                     XXX    ',
'      XXXXXXXXXXPPPPPXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl1 = [ #Monde 1 Niveau 1 (Il y a 8 niveaux par monde)
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                    XX      ',
'                  XXXXXXX   ',
'XXXXXXPPXXXXXXXXPPXXXXXXXXXX',  ### Placer des pieux dans les cases "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl2 = [ #Monde 1 Niveau 2
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'        XXX                 ',
'  XXXX                XX    ',
'                  XX  XXX   ',
'XPPPPPPPPPPXXXXXPPXXPPXXXX  ', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl3 = [ #Monde 1 Niveau 3
'                            ',
'                XXX         ',
'                            ',
'            XXX             ',
'                            ',
'        XXX           XXX   ',
'                            ',
'    XXX                     ',
'                            ',
'  XPPPPPPPPPPPPPPPPPPPPPXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl4 = [ #Monde 1 Niveau 4
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'      XXX                   ',
'                    XXX     ', ### Placer un ennemi dans la case "E"
'  XXXX---------E---XXXXX    ', ### Les cases "-" representent la zone de mouvement de l'ennemi
'XXXXXXXXXXXXXXXXXXXXXXXXPPXX', ### "P"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']






merchant_lvl1 = [ #Monde dans lequel le personnage peut interagir avec le marchand
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'     XXX   XXXXXX           ',
'           MMMMMM     XX    ', ### Placer le marchand dans les cases "M"
'  XX       MMMMMM    XXXX  X', ### "M"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']






world1_lvl5 = [ #Monde 1 Niveau 5
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                 XXX        ',
'    XX                      ',
'X-----E-X   XXXX  -----E----', ### "E" et "-"
'XXXXXXXXXPP      PPXXXXXXXXX', ### "P"
'XXXXXXXXXXXPPPPPPXXXXXXXXXXX'] ### "P"



world1_lvl6 = [ #Monde 1 Niveau 6
'                            ',
'                            ',
'                            ',
'                 ---E--     ',
'          XX     XXXXXX     ',
'                            ',
'            XXXX            ',
'                  X    X    ',
'  CC  CC XXXCCCCCCCCCCCCCX  ', ### Placer des pieux cachés dans les cases "C"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl7 = [ #Monde 1 Niveau 7
'                            ',
'                            ',
' CC                         ',
' XX     XXXX                ',
'                            ',
'    XXXXCCC   XX  XX  XX  XX',
'        XXX                 ',
' XX                         ',
' CPCPCPCPCPCPCPCPCPCPCPCPCPC',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']



world1_lvl8 = [ #Monde 1 Niveau 8
'                            ',
'                            ',
'CCCCCC                CCCCCC',
'XXXXXX        CXXXX   XXXXXX',
'         CXXXX       XX     ',
'XC   XXXXX    CCCC X  X    X',
'XX            XXXX    XX   C',
'XXXC                     CXX',
'XXXXC               XXXXXX  ',
'XXXXXC --E--E--E--E--E--E---',
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
'XXXX       MMMMMMXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
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
'                            ',
'    ---E-----E-----E---     ',
'    XXXXXXXXXXXXXXXXXXX     ',
'   X                   X    ',
'  X                     XX  ',
'     C    C    C    C       ',
'X    XXXXXXXXXXXXXXXXXXX   X',
' X                        X ',
'  X                      X  ',
'   X P  P  P  P  P  P  PX   ',
'    XXXXXXXXXXXXXXXXXXXX    ']



world2_lvl6 = [ #Monde 2 Niveau 6
'                            ',
'                            ',
'                       XX   ',
' XX     XXX                 ',
' XX     XXX              XX ',
' XX                         ',
' XX                         ',
' XX    X          XX  XX    ',
'       X          XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']



world2_lvl7 = [ #Monde 2 Niveau 7
'                            ',
'                            ',
'                       XX   ',
' XX     XXX                 ',
' XX     XXX              XX ',
' XX                         ',
' XX                         ',
' XX    X          XX  XX    ',
'       X          XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']



world2_lvl8 = [ #Monde 2 Niveau 8
'                            ',
'                            ',
'                       XX   ',
' XX     XXX                 ',
' XX     XXX              XX ',
' XX                         ',
' XX                         ',
' XX    X          XX  XX    ',
'       X          XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']






bonus_lvl = [ #Niveau Bonus
'                            ',
'                            ',
'                       XX   ',
' XX     XXX                 ',
' XX     XXX              XX ',
' XX                         ',
' XX                         ',
' XX    X          XX  XX    ',
'       X          XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']
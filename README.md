# Projet de NSI (2021-2022): Jeu sous Python/Pygame
Collaborateurs: Remi K-S et Nathan D

Lien de l'environnement IDE de Python en ligne: https://replit.com/join/lqrqvuwvkd-8lackfield5 ET si le premier lien ne marche pas: https://replit.com/join/xczalmmhdt-ndd7

Le deuxième lien est le plus modifié et mis à jour entre les des deux en général.


⚠ Voir "Instructions du jeu" à la fin de ce fichier README, les touches de controle peuvent aussi être trouvées dans le menu de VoD: Menu --> Options --> Controls

# Idées de jeux sur lesquels se baser
- Super Mario Bros. (1985)
- Terraria
- Pac-Man
- **Trap Adventure 2 (Impossible Game)**


# Idée générale: jeu Side Scroller nommé "Voyage of Death" (semblable à Trap Adventure 2)
- Nom du jeu: "Voyage of Death"
- Jeux programmé avec le moteur de jeu Pygame en utilisant le langage Python
- L'arrière plan du jeu ne se déplace pas, mais c'est le personnage lui-même qui se déplace et une fois qu'il à atteint un coté de l'écran, le niveau change 
- Ce sera un Jeu de Plates-Formes (Platformer), où le joueur doit éviter des obstacles (piques, trous, ...) sous peine de perdre des coeurs (PV ---> Points de Vie)
- "Voyage of Death" sera inspiré et basé sur le jeu Trap Adventure 2. Voici un lien Youtube pour donner une idée visuelle du jeu envisagé: https://youtu.be/YUTzQ-A0-oA
- **Il y aura plusieurs mondes, chacun contenant plusieurs niveaux**
- **Chaque monde aura un thèmes different qui affectera les caracteristiques du personnage selon l'environnement, ces caractéristiques seront apliquées sur tout les niveaux de chaque monde**
- Une fois arrivé à la fin de tout les mondes sans mourir (sans avoir perdu tous les coeurs), le joueur à gagné le jeu 
- Les obstacles peuvent être statiques ou **mobiles, les obsacles peuvent aussi apparaitre en dehors de l'écran**
- **Le personnage sera customisable, differents cosmetiques, (couleurs, ...)**
- **Il y aura un ou plusieurs niveau ou le personnage sera dans l'eau**
- Il y aura des super-pouvoirs (power-ups) qui auront des effets positifs et négatifs tels que double-saut, ralentissement, vitesse, plus de coeurs (amélioration)... qui seront achetables depuis un marchand
- **Il y aura un Boss au dernier niveau de chaque monde, qu'il faudra tuer pour progresser dans le jeu**
- Le personnage sera capable de sauter, s'accroupir, aller à gauche et à droite et d'attaquer
- Il sera impossible de retourner à un niveaux précédent, sauf si le joueur tombe dans un piège (caché ou non)
- **Il y aura des passages secrets contenant soit des pièces d'argent ou des pièges que le joueur devra éviter**
- A chaque fin de niveau il est possible de gagner plus ou moins de pièces d'argent selon le temps pris par le joueur pour le compléter, si des power-ups ont été utilisés et la difficulté du niveau
- Il y aura 2 modes de difficulté dans le jeu: "Normal" et "Hardcore". Le mode "Normal" laisse le joueur la possibilité d'utiliser l'entièreté du stock du marchand (sans pénalités), le joueur a un bon nombre de coeurs et si il meurs il peut réapparaitre à des checkpoints répartis à travers le jeu. Le mode "Hardcore" donnera au joueur moins d'options d'achat au marchand, il aura moins de coeurs et si il meurs, il devra recommencer au tout début du jeu (Monde 1, Niveau 1) et quand il gagne le jeu, il sera très bien récompensé     
- Des effets sonores et de la musique seront également présents dans le jeu

*Les idées marquées en gras sont soit trop ambitieuses (pas absolument nécessaires) et ne seront peut-être pas achevées ou sont destinées à être modifiées*


# Planning prévisionnel général sur 15 semaines:
✅ = Fini ; ❌ = Incomplet ou pas commencé

- ✅Semaine 1-3 (3 Déc. - 10 Déc. - 17 Déc.): Brainstorming d'idées pour la création du jeu

- ✅Semaine 4-6 (7 Jan. - 14 Jan. - 21 Jan.): Etablir les bases du jeu: Création du personnage (son Sprite ---> son apparence), ses déplacements (gauche, droite, saut, accroupissement (et peut-être attaque))

- Nathan: Faire le Pixel art des sprites du Personnage et du Marchand

- Rémi: Faire le plan de la carte du premier monde (Idée de projet --> 2 Mondes), faire la logique du marchand et ses marchandises

- ✅Semaine 7-9 (28 Jan. - 4 Fév. - 11 Fév.): Introduire plusieurs éléments dans la base du jeu: Système monétaire (pièces d'argent), marchand, power-ups, cosmétiques

- Nathan: Collision du personnage avec les obstacles, faire le pixel-art des ennemis

- Rémi: Faire tous les niveaux de chaque monde (Idée de projet --> 2 mondes), faire la logique du marchand et ses marchandises

- ❌Semaine 10-12 (18 Fév. - 25 Fév. - 4 Mars): Ajouter au jeu: le son, la musique, animations des Sprites et du monde

- ❌Semaine 13-15 (11 Mars - 18 Mars - 25 Mars): Testing du jeu, recherche de bugs et glitches ---> debugging, balancement du jeu (Equitabilité de la difficulté)


# Instructions du jeu programmé:
✅ = Fini ; ❌ = Incomplet ou pas commencé

✅Pour déplacer le personnage:
- Flèches directionnelles horizontales: '←' et '→' --> Aller à gauche et à droite
- Barre d'Espace: ' ' --> Sauter (On pourra peut-être utiliser '↑' pour sauter)
- Flèche basse: '↓' --> S'accroupir

❌Pour interagir avec l'environnement:
- Touche f ou e: 'f' ou 'e' --> Interagir (avec marchand ou autre)
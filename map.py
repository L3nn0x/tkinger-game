from glob import *
from tkinter import *
from entity import *
from enemies import *
from perso import *
import random

class Map(Canvas):        #Création de la classe Map, qui hérite de Canvas
    def __init__(self, parent, filename, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)   #Initialiser le parent
        self.perso = None
        self.load(filename)

    def load(self, filename):
        self.time = 0
        self.delete("all")          #Vide le Canvas
        self.entities = []          # Crée (ou vide) le tableau des entités
        with open(filename, "r") as f:
            lines = [l.rstrip("\r\n") for l in f] #Lire le fichier level...
            self.maxRed = int(lines[0])
            self.maxGreen = int(lines[1])
            self.w = int(lines[2])
            self.h = int(lines[3])
            self.map = "".join(lines[4:])
            for i in range(len(self.map)):    # Boucle pour créer toutes les entités
                if self.map[i] == '0':
                    self.entities.append(Wall(self, (i % self.w, i // self.w), 0))
                elif self.map[i] == "s":
                    self.entities.append(Exit(self, (i % self.w, i // self.w)))
                elif self.map[i] == "j":
                    if self.perso == None:
                        self.perso = Perso(self, (i % self.w, i // self.w))
                    else:
                        self.perso.reset((i % self.w, i // self.w))
        for i in range(self.w):               #Crée le contour de la map
            self.entities.append(Wall(self, (i, -1), 0))
            self.entities.append(Wall(self, (i, self.h), 0))
        for i in range(self.h):               #...
            self.entities.append(Wall(self, (-1, i), 0))
            self.entities.append(Wall(self, (self.w, i), 0))
        self.config(scrollregion=(0, 0, self.w*SIZE+CST, self.h*SIZE+CST))

    def show(self):           #Boucle pour afficher toutes les entités
        for i in self.entities:
            i.show()
        self.perso.show()
        pos = list(map(lambda x: x*SIZE+CST, self.perso.pos))
        pos[0] = (pos[0] - self.winfo_width()/2) / (self.w*SIZE+CST)
        pos[1] = (pos[1] - self.winfo_height()/2) / (self.h*SIZE+CST)
        self.xview_moveto(pos[0])
        self.yview_moveto(pos[1])

    def update(self, dt):   #Boucle pour mettre à jour les entités...
        for i in self.entities:
            i.update(dt, self)
        self.perso.update(dt, self) #...le perso
        self.time += dt
        if self.time > 250:        #Ajout aléatoire d'ennemis
            self.time = 0
            if random.randint(0, 100) < 50:
                self.addEnnemy()

    def addEnnemy(self):     #Fonctoin pour ajouter un ennemi
        entity = None
        poss = [i.pos for i in self.entities]
        pos = (random.randint(0, self.w), random.randint(0, self.h))
        while pos in poss or pos == self.perso.pos:   #Trouver une position libre
            pos = (random.randint(0, self.w), random.randint(0, self.h))
        nbRed = len(list(filter(lambda e: isinstance(e, Red), self.entities)))  #Compter nb de rouges
        nbGreen = len(list(filter(lambda e: isinstance(e, Green), self.entities)))# et de verts
        if random.randint(0, 1) and nbRed < self.maxRed: #Choix de la couleur
            entity = Red(self, pos)
        elif nbGreen < self.maxGreen:
            entity = Green(self, pos)
        if entity is not None:
            self.entities.append(entity)      # Et ajout.

    def entity_type(self, coord):   #Pour récupérer le type d'une entité
        for i in self.entities:
            if i.pos == coord:
                if isinstance(i, Wall): 
                    return WALL
                elif isinstance(i, Red): 
                    return REDENNEMY
                elif isinstance(i, Green): 
                    return GREENENNEMY
                elif isinstance(i, Exit): 
                    return FINISH
                elif isinstance(i, Perso):
                    return PERSO
        return NOTHING


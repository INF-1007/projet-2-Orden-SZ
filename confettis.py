import random
import pygame
from config import WIDTH, HEIGHT

class Confetti: 
    
    def __init__(self):
    
        self.taille = random.randint(5, 10)
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0) 
        self.vitesse = random.randint(150, 400)
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def tomber(self, dt):
    
        self.y += self.vitesse * dt
        
        if self.y > HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, WIDTH)

    def dessiner(self, screen):
        pygame.draw.rect(screen, self.couleur, (self.x, self.y, self.taille, self.taille))

    # TODO : Compléter la classe
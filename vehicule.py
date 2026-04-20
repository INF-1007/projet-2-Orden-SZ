import numpy as np
import pygame
from specifications import DENSITE_AIR

# TODO : Créer la classe Vehicule

class Vehicule:

    
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):

        # TODO : ajouter les attributs
        self.__nom = nom
        self.__position = np.array(position_dep,dtype = float)
        self.__vitesse = np.array([0.0 , 0.0],dtype = float)
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__poids_total = self.calculer_poids_total()

        # TODO : ajouter un attribut pour l'image du véhicule
        image_originale = pygame.image.load(image_path)
        nouvelle_taille = (Specs.image_width, Specs.image_height)
        self.image = pygame.transform.scale(image_originale, nouvelle_taille)
        
    
    def affichage_vehicule(self, screen):
        # TODO : compléter la méthode 
        
        position = self.__position.astype(int)
        screen.blit(self.image , (position[0],position[1]))

    
    def calculer_poids_total(self):
        # TODO : compléter la méthode
        
        p_moteur = self.__moteur.get_poids()
        p_chassis = self.__chassis.get_poids()
        p_roues = 0
        for r in self.__roues:
            p_roues += r.get_poids()
            
        return p_moteur + p_chassis + p_roues

    def calculer_traction(self):
        # TODO : compléter la méthode 
        
        traction = self.__poids_total * self.__moteur.get_acceleration()
        
        return traction

    def calculer_friction(self):
        # TODO : compléter la méthode 
        
        v_norme = np.linalg.norm(self.__vitesse)
        friction = self.__roues[0].get_coefficient_friction() * v_norme
        
        return friction
        

    def calculer_trainee(self):
        # TODO : compléter la méthode 
        v_norme = np.linalg.norm(self.__vitesse)
        trainee = 0.5 * self.__chassis.get_coefficient_trainee() * DENSITE_AIR * (v_norme ** 2)
        
        return trainee

    def accelerer(self, dt):
        # TODO : compléter la méthode 
        
        f_traction = self.calculer_traction()
        f_friction = self.calculer_friction()
        f_trainee = self.calculer_trainee()
        
        f_nette = f_traction - f_trainee - f_friction
        a = f_nette / self.__poids_total
        
        self.__vitesse[0] += a * dt
        self.__position += self.__vitesse * dt
        
    def get_position(self):
        return self.__position

    def get_nom(self):
        return self.__nom
        

    def celebrer(self):
        # TODO : compléter la méthode 
        return f"{self.__nom} remporte la course !"
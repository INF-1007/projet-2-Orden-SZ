# moto.py
from vehicule import Vehicule
from specifications import MotoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Moto(Vehicule):

    def __init__(self, nom, position_dep, image_path):
        
        moteur = Moteur(MotoSpecs.moteur_nom, MotoSpecs.moteur_puissance, MotoSpecs.moteur_acceleration)
        chassis = Chassis(MotoSpecs.chassis_nom, MotoSpecs.chassis_poids, MotoSpecs.chassis_aire, MotoSpecs.chassis_trainee)
        roues = []
        for i in range (2):
            nouvelle_roue = Roue(MotoSpecs.roue_nom, MotoSpecs.roue_poids, MotoSpecs.roue_friction, MotoSpecs.roue_support)
            roues.append(nouvelle_roue)
       
        super().__init__(nom, position_dep, roues, moteur, chassis, MotoSpecs, image_path)
        
    # TODO : Compléter la classe
# auto.py
# auto.py
from vehicule import Vehicule
from specifications import AutoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Auto(Vehicule):

    def __init__(self, nom, position_dep, image_path):
        
        moteur = Moteur(AutoSpecs.moteur_nom, AutoSpecs.moteur_puissance, AutoSpecs.moteur_acceleration)
        chassis = Chassis(AutoSpecs.chassis_nom, AutoSpecs.chassis_poids, AutoSpecs.chassis_aire, AutoSpecs.chassis_trainee)
        roues = []
        for i in range(4) :
            nouvelle_roue = Roue(AutoSpecs.roue_nom, AutoSpecs.roue_poids, AutoSpecs.roue_friction, AutoSpecs.roue_support)
            roues.append(nouvelle_roue)
       
        super().__init__(nom, position_dep, roues, moteur, chassis, AutoSpecs, image_path)

    # TODO : Compléter la classe
from vehicule import Vehicule
from roue import Roue
from moteur import Moteur
from chassis import Chassis
from specifications import CamionSpecs

class Camion(Vehicule): 
    
 def __init__(self, nom, position_dep, image_path):
        
        moteur = Moteur(CamionSpecs.moteur_nom, CamionSpecs.moteur_puissance, CamionSpecs.moteur_acceleration)
        chassis = Chassis(CamionSpecs.chassis_nom, CamionSpecs.chassis_poids, CamionSpecs.chassis_aire, CamionSpecs.chassis_trainee)
        roues = []
        for i in range(6) :
            nouvelle_roue = Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support)
            roues.append(nouvelle_roue)
       
        super().__init__(nom, position_dep, roues, moteur, chassis, CamionSpecs, image_path)   

    # TODO : Compléter la classe
from .controleur import Ia_Avancer_tout_droit, IAseq, IATournerAngle,BoucleIA,TracerCarre
from robot.IA.proxy import ControleurRobotVirtuel, ControleurRobotVraieVie

delta_ia=0.0001

def get_AvancerToutDroit(cr,dist,v):
    """
    Creer une IA qui permet au robot d'avancer tout droit d'une certaine distance et a une certaine vitesse 
    :param cr : le controleur du robot
    :param dist : distance de laquelle avance le robot en mm
    :param v : vitesse a laquelle avance le robot en dps
    :return : l'IA crée
    """
    #ia pour avancer tout droit 
    ia10=Ia_Avancer_tout_droit(dist,v,cr)
    return ia10

def get_TournerAngle(cr,angle,v):
    """
    Creer une IA qui permet au robot de tourner d'un certain angle et a une certaine vitesse 
    :param cr : le controleur du robot 
    :param angle: l'angle que le robot tourne en mm
    :param v: vitesse a laquelle tourne le robot en degre
    :return : l'IA crée
    """
    #ia pour tourner 
    iaa=IATournerAngle(cr,angle,v)
    return iaa

def get_Tracerarre(cr,longueur,v):
    """
    Creer une IA qui permet au robot de tracer un carre d'une certaine longeueur et a une certaine vitesse 
    :param cr : le controleur du robot
    :param longueur: la longueur du carre
    :param v: vitesse a laquelle tourne le robot
    :return : l'IA crée
    """
    #ia seq 
    Carre=TracerCarre(cr,longueur,v)
    return Carre

def get_IABoucle(cr, strategie):
    """
    Creer une IA boucle de la strategie sohaitée
    :param cr : le controleur du robot
    :param strategie: strategie sohaitée
    :return : l'IA crée
    """
    iaboucle=BoucleIA(cr,strategie,delta_ia)
    return iaboucle

def get_Seq_IA(cr,nb_repition, strategie):
    """
    Creer une IA sequentielle d'une MÊME STRATEGIE un nombre souhaité de fois
    :param cr : le controleur du robot
    :param nb_repitition: le nombre de repition de la strategie souhaité
    :param strategie: strategie sohaitée
    :return : l'IA crée
    """
    list=[]
    for i in range(nb_repition):
        list.append(strategie)
    iaseq=IAseq(cr,list)
    return iaseq

def get_Seq_list(cr,nb_repition, list_strat):
    """
    Creer une IA sequentielle d'une LISTE DE STRATEGIES un nombre souhaité de fois
    :param cr : le controleur du robot
    :param nb_repitition: le nombre de repition de la liste  de strategies souhaité
    :param list_start : liste  de strategies souhaité
    :return : l'IA crée
    """
    list=[]
    for i in range(nb_repition):
        list=list+list_strat
    iaseq=IAseq(cr,list)
    return iaseq
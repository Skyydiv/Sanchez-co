from tkinter import *    
from Objet import Robot
from Objet import Obstacle
from environnement import Environnement 
from Simulation import Simulation
"""
Création de la fenêtre d'affichage
"""
env=Environnement(500,500,5)
Largeur=env.nbcolonnes
Hauteur=env.nblignes

root = Tk()
canvas=Canvas(root, width=Largeur , height=Hauteur , background="black")
canvas.pack(fill="both",expand=True)


"""creation de notre robot et de l'obstacle 
"""

rob=Robot([5,2])
x0=rob.x
y0=rob.y
dx=rob.vitesse[0]
dy=rob.vitesse[1]


ob1=Obstacle(200,200,4,5.6)
x1=ob1.x
y1=ob1.y

"""
    creation de nos 2 rectangles avec 4 cordonnées pour chaque sommets, les deux sont des carrés de 20*20
"""
rect=canvas.create_rectangle(x0,y0,x0+20,y0+20,width=2,fill="red")
rect1=canvas.create_rectangle(x1,y1,x1+20,y1+20,width=2,fill="yellow")

def deplacer():
    """
        Modifie les coordonnées du rectangle a l'aide de la vitesse dx et dy et appelle la fonction tout les 50ms
            si x0 n'est plus dans le cadre change le sens du vecteur vitesse 
    """

        
    global x0,y0,dx,dy
        
    x0=x0+dx
    y0=y0+dy
    
    canvas.coords(rect,x0,y0,x0+20,y0+20)
    
    if x0<0 or x0>Largeur:
        return
    if y0<0 or y0>Hauteur:
        return
    
    
    canvas.after(50,deplacer)

    return
    
def action():
    """
        action appelle la fonction deplacer() 
    """
    deplacer()
    return 

    """
        creation d'un bouton qui lance la commande action() permettant de lancer l'affichage et deplacer le carré
    """

def afficher(simu):
    """
    Affiche l'environnemment en mettant 'R' s'il y a un robot, 'O' s'il y a un obstacle et ' ' si rien.
    """
    
    for i in range simu.environnement.nblignes:
        for j in range simu.environnement.nbcolonnes:
            if simu.environnement.tab[i][j]==set():
                print(' ')
            else:
                for obj in tab[i][j]:
                    if obj isinstance Robot:
                        print('R')
                    elif obj isinstance Obstacle:
                        print('O')
        print()
            
                        
             
bouton=Button(root,text="Lancer simu", width=20,command=action)
bouton.pack(pady=10)

root.mainloop()





from tkinter import *    
Largeur =600
Hauteur=500



root = Tk()
canvas=Canvas(root, width=Largeur , height=Hauteur , background="black")
canvas.pack(fill="both",expand=True)




x0,y0=100,100
dx=+5
dy=+2

x1,y1=200,200

rect=canvas.create_rectangle(x0,y0,x0+30,y0+20,width=2,fill="red")
rect1=canvas.create_rectangle(x1,y1,x1+20,y1+20,width=2,fill="yellow")


def deplacer():

        
    global x0,y0,dx,dy
        
    x0=x0+dx
    y0=y0+dy
    
    canvas.coords(rect,x0,y0,x0+30,y0+20)
    
    if x0<0 or x0>Largeur:
        dx=-dx
    if y0<0 or y0>Hauteur:
        dy=-dy
    
    
    canvas.after(50,deplacer)

    return

def action():
    deplacer()
    return 

bouton=Button(root,text="Lancer simu", width=20,command=action)
bouton.pack(pady=10)

root.mainloop()





from robot.simu import simulation
from robot.IA import iaboucle 
from robot.affichage import root

iaboucle.start()
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
from graphique import *

gr = Grille(-4.0,4.0,-4.0,4.0)

f = Fonction("x",-4.0,4.0,"red")
g = Fonction("-x^2+1",-2.0,2.0,"blue","g")

graphique = Graphique(gr,[f,g])
graphique.export("courbe")
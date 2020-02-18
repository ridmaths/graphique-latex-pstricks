from graphique import *

# quelques tests


f = Fonction("2*x+1",-10.0,10.0,"red")
g = Fonction("x^2+1",-5.0,5.0,"blue","g")

#gr = Grille(-5.0,5.0,-2.0,2.0,0.5,0.5)
gr = Grille()

graphique = Graphique(gr,[f,g])

print(graphique.codeTex())

graphique.export("coucou")
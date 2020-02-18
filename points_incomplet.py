class Point:
	def __init__(self,abscisse,ordonnee,nom="A",couleur="black"):
		self.abscisse = abscisse
		self.ordonnee = ordonnee
		self.nom = nom
		self.couleur = couleur

	def code(self):
		punto = f"\\psdots[dotstyle=*,linecolor={self.couleur}]({self.abscisse},{self.ordonnee})"
		texto = f"\\rput[bl]({self.abscisse},{self.ordonnee}){{\\{self.couleur}{{${self.nom}$}}}}"
		return [punto,texto]


class Grille:
	def __init__(self,xmin=-10.0,xmax=10.0,ymin=-5.0,ymax=5.0,xgrid=1.0,ygrid=1.0):
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax
		self.xgrid = xgrid
		self.ygrid = ygrid

	def code(self):
		# Construction axes
		axes = f"\\psaxes[labelFontSize=\\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=1]{{->}}(0,0)({self.xmin},{self.ymin})({self.xmax},{self.ymax})"
		
		# Lignes verticales
		pasX = int((self.xmax-self.xmin)/self.xgrid)+1
		lignesX = f"\\multips({self.xmin},0)({self.xgrid},0){{{pasX}}}{{\\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=1pt,linecolor=lightgray]{{c-c}}(0,{self.ymin})(0,{self.ymax})}}"
		
		# Lignes horizontales
		pasY = int((self.ymax-self.ymin)/self.ygrid)+1
		lignesY = f"\\multips(0,{self.ymin})(0,{self.ygrid}){{{pasY}}}{{\\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=1pt,linecolor=lightgray]{{c-c}}({self.xmin},0)({self.xmax},0)}}"

		return  [lignesX,lignesY,axes]

class Graphique:
	def __init__(self,grille,points,xunit=1.0,yunit=1.0):
		self.grille = grille
		self.points = points
		self.xunit = xunit
		self.yunit = yunit

	def code(self):
		texte = f"\\psset{{xunit={self.xunit}cm,yunit={self.yunit}cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}} \n"
		texte += f"\\begin{{pspicture*}}({self.grille.xmin},{self.grille.ymin})({self.grille.xmax},{self.grille.ymax}) \n"
		for el in self.grille.code():
			texte += el
			texte += "\n"
		for point in self.points:
			[punto,texto] += point.code()
			texte += punto+"\n"+texto+"\n"
		texte += "\\end{pspicture*}  \n"
		return texte

	def codeTex(self,classe="standalone"):
		if classe=="standalone":
			document = "\\documentclass{standalone}"
		else:
			document = "\\documentclass[10pt]{article}"
		document += '''
\\usepackage{amsmath,amsfonts,amssymb}
\\usepackage{mathrsfs}
\\usepackage{pstricks-add}
\\pagestyle{empty}
\\begin{document}
'''
		document += self.code()
		document += "\\end{document}"
		return document

	def export(self,nom):
		fichier = open(nom+".tex","w")
		fichier.write(self.codeTex())
		fichier.close()
		print("*** Export en .tex termine ***")


class GraphiqueFonc:
	def __init__(self,grille,fonctions,xunit=1.0,yunit=1.0):
		self.grille = grille
		self.fonctions = fonctions
		self.xunit = xunit
		self.yunit = yunit

	def code(self):
		texte = f"\\psset{{xunit={self.xunit}cm,yunit={self.yunit}cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}} \n"
		texte += f"\\begin{{pspicture*}}({self.grille.xmin},{self.grille.ymin})({self.grille.xmax},{self.grille.ymax}) \n"
		for el in self.grille.code():
			texte += el
			texte += "\n"
		for fonction in self.fonctions:
			texte += fonction.code()
			texte += "\n"
		texte += "\\end{pspicture*}  \n"
		return texte

	def codeTex(self,classe="standalone"):
		if classe=="standalone":
			document = "\\documentclass{standalone}"
		else:
			document = "\\documentclass[10pt]{article}"
		document += '''
\\usepackage{amsmath,amsfonts,amssymb}
\\usepackage{mathrsfs}
\\usepackage{pstricks-add}
\\pagestyle{empty}
\\begin{document}
'''
		document += self.code()
		document += "\\end{document}"
		return document

	def export(self,nom):
		fichier = open(nom+".tex","w")
		fichier.write(self.codeTex())
		fichier.close()
		print("*** Export en .tex termine ***")

### FIN FONCTIONS

# quelques tests


f = Fonction("2*x+1",-10.0,10.0,"red")
g = Fonction("x^2+1",-5.0,5.0,"blue")

print(f.nomCourbe)

gr = Grille(-5.0,5.0,-2.0,2.0,0.5,0.5)

#graphique = Graphique(gr,[f,g])

#print(graphique.codeTex())

#graphique.export("coucou")



		for el in self.grille.code():
			texte += el
			texte += "\n"

from random import uniform
import sympy as sp

x = sp.symbols("x")

class Fonction:
	def __init__(self,fonction,debut,fin,couleur="blue",nom="f",taille=1.2):
		self.fonction = fonction
		self.debut = debut
		self.fin = fin
		self.couleur = couleur
		self.nom = nom
		self.nomCourbe = "\\mathscr{C}_"+nom
		self.taille = taille

		self.hasard = int(uniform(self.debut+0.5,self.fin-0.5)*100)/100
		self.image = sp.sympify(self.fonction.replace("^","**")).subs(x,self.hasard)
	
	def code(self):
		texte = f'''\\psplot[linewidth={str(self.taille)}pt,linecolor={self.couleur},plotpoints=200]{{{str(self.debut)}}}{{{str(self.fin)}}}{{{self.fonction}}}
\\rput[bl]({self.hasard},{self.image}){{\\{self.couleur}{{${self.nomCourbe}$}}}}'''
		return texte

class Grille:
	def __init__(self,xmin=-10.0,xmax=10.0,ymin=-10.0,ymax=10.0,xgrid=1.0,ygrid=1.0):
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

		return  f'''{lignesX}
{lignesY}
{axes}'''

class Graphique:
	def __init__(self,grille,fonctions,xunit=1.0,yunit=1.0):
		self.grille = grille
		self.fonctions = fonctions
		self.xunit = xunit
		self.yunit = yunit

	def code(self):
		texte = f"\\psset{{xunit={self.xunit}cm,yunit={self.yunit}cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}} \n"
		texte += f"\\begin{{pspicture*}}({self.grille.xmin},{self.grille.ymin})({self.grille.xmax},{self.grille.ymax}) \n"
		texte += self.grille.code()
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
import os

## Constantes :

fonction = "x^2+1"
definition = {"debut" : -2.0, "fin" : 3.0}
params = {"xunit" : 1.0, "yunit" : 1.0, "axis" : {"xmin": -5.0, "xmax": 5.0, "ymin": -5.0, "ymax": 5.0}, "xgrid" : 1, "ygrid" : 1}


## Fonctions utiles

def docLatex(contenu):
	document = '''\\documentclass{standalone}
\\usepackage{pstricks-add}
\\pagestyle{empty}
\\begin{document}
'''
	document += contenu
	document += '''
\\end{document}'''
	return document


def codeGraphique(fonction,definition,params):
	graphique = f'''\\psset{{xunit={params["xunit"]}cm,yunit={params["yunit"]}cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}}
\\begin{{pspicture*}}({params["axis"]["xmin"]},{params["axis"]["ymin"]})({params["axis"]["xmax"]},{params["axis"]["ymax"]})
\\multips(0,{params["axis"]["ymin"]})(0,{params["ygrid"]}){{{int((params["axis"]["ymax"]-params["axis"]["ymin"])/params["ygrid"])+1}}}{{\\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.8pt,linecolor=lightgray]{{c-c}}({params["axis"]["xmin"]},0)({params["axis"]["xmax"]},0)}}
\\multips({params["axis"]["xmin"]},0)({params["xgrid"]},0){{{int((params["axis"]["xmax"]-params["axis"]["xmin"])/params["xgrid"])+1}}}{{\\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.8pt,linecolor=lightgray]{{c-c}}(0,{params["axis"]["ymin"]})(0,{params["axis"]["ymax"]})}}
\\psaxes[labelFontSize=\\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=1]{{->}}(0,0)({params["axis"]["xmin"]},{params["axis"]["ymin"]})({params["axis"]["xmax"]},{params["axis"]["ymax"]})
\\psplot[linewidth=1.2pt,linecolor=blue,plotpoints=200]{{{definition["debut"]}}}{{{definition["fin"]}}}{{{fonction}}}
\\end{{pspicture*}}
'''
	return graphique

## FIN FONCTIONS

## Construction du graphique pstricks en latex

nom = "courbe"

file = open(nom+".tex","w")
file.write(docLatex(codeGraphique(fonction,definition,params)))
file.close()

## Generation du pdf 

commande1 = "latex -quiet "+nom+".tex"
print("[*] Compilation latex vers dvi")
os.system(commande1)

commande1 = "dvips -q "+nom+".dvi"
print("[*] Compilation dvi vers ps")
os.system(commande1)

commande1 = "ps2pdf "+nom+".ps"
print("[*] Compilation ps vers pdf")
os.system(commande1)

print("[*] Suppression des fichiers inutiles")
Ext = [".log",".aux",".dvi",".ps"]
for e in Ext:
	commande2 = "del "+nom+e
	os.system(commande2)
print("[*] Execution terminee")

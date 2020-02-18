# Objectifs 

On souhaite automatiser le tracé de courbes avec PsTricks et l'export en pdf.

## Les programmes 

* **graphique** : fonctionnel, ensemble de classes / méthodes permettant de construire et d'obtenir la courbe sous format .tex

* **graphique_old** : c'est nul, mais ça peut dépanner : il faut modifier l'expression de la fonction dans le programme puis l'exécuter avec Python. Cela donne un tex puis un pdf de la courbe (tex version standalone)

 * **tests** : on importe les fonctions / classes de graphique_v2 et on obtient un graphique avec une grille et deux coubes

 * **tracerCourbe** : il faut modifier ce fichier pour les paramètres, et l'exécuter avec Python.

  * **points_incomplet** : incomplet pour le moment. Permet de placer des points sur le graphique.


## Le dossier tests 

ce dossier contient :

* coucou (.tex et .pdf ) : résultat de l'exécution de **tests.py**
* courbe (.tex et .pdf ) : résultat de l'exécution de **tracerCourbe**
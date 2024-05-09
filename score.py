import os


def initialisationFichier():
    nom_fichier = "fichiers/score.csv"
    if os.path.exists(nom_fichier) == False:
        try:
            with open(nom_fichier, 'w') as f:
                print(f"Le fichier {nom_fichier} a été créé avec succès.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la création du fichier : {str(e)}")
        return True
    return True

# à faire
def ajouterScore(pseudo,score):
    pass
def recupererScores():
    pass
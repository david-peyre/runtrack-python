chaine = "abcdefghijklmnopqrstuvwxyz" * 10

longueur_chaine = len(chaine)
niveau = 0

while niveau * (niveau + 1) // 2 < longueur_chaine:
    debut = niveau * (niveau + 1) // 2
    fin = (niveau + 1) * (niveau + 2) // 2
    ligne = chaine[debut:fin]
    print(ligne.center(50))  # Ajuste la largeur de l'affichage
    niveau += 1

chaine = "abcdefghijklmnopqrstuvwxyz" * 10

longueur_chaine = len(chaine)
niveau = 0
caracteres_par_niveau = 1

while niveau * caracteres_par_niveau < longueur_chaine:
    debut = (niveau * (niveau + 1) // 2) * 2  # Ajustement ici pour obtenir les indices corrects
    fin = ((niveau + 1) * (niveau + 2) // 2) * 2  # Ajustement ici également
    ligne = chaine[debut:fin]
    print(ligne.ljust(50))
    niveau += 1
    caracteres_par_niveau += 2

def my_sort(liste):
    # Initialiser le compteur de coups
    coups = 0
    # Initialiser la variable pour indiquer si un échange a été effectué lors du dernier passage
    echange_effectue = True

    # Tant qu'il y a eu un échange lors du dernier passage
    while echange_effectue:
        echange_effectue = False
        # Parcourir la liste
        for i in range(len(liste) - 1):
            # Comparer les éléments adjacents
            if liste[i] > liste[i + 1]:
                # Échanger les éléments
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                # Augmenter le compteur de coups
                coups += 1
                # Indiquer qu'un échange a été effectué
                echange_effectue = True

    # Afficher le nombre total de coups
    print("Nombre total de coups pour trier la liste :", coups)
    # Retourner la liste triée
    return liste

# Exemple d'utilisation
liste_non_triee = [34, 22, 64, 12, 25, 11, 90]
liste_triee = my_sort(liste_non_triee)
print("Liste triée :", liste_triee)

def remplacer_element(liste, index):
    if index >= 1 and index < len(liste) - 1:
        somme_voisins = liste[index - 1] + liste[index + 1]
        liste[index] = somme_voisins

L = [1, 2, 3, 4, 5]


print("Deuxième valeur de la liste :", L[1])


remplacer_element(L, 3)


print("Liste après la modification :", L)


print("Dernière valeur de la liste :", L[-1])

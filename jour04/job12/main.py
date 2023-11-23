def tri_croissant(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]

ma_liste = [7, 11, 42, 39, 2]
tri_croissant(ma_liste)

print("La liste triée dans l'ordre croissant est :", ma_liste)

def echanger_premiere_et_derniere(liste):
    if len(liste) >= 2:
        liste[0], liste[-1] = liste[-1], liste[0]

# Exemple d'utilisation
liste1 = [5, 2, 3, 4, 1]
echanger_premiere_et_derniere(liste1)
print(liste1)  # Résultat attendu : [1, 2, 3, 4, 5]

liste2 = [1, 2, 3, 4, 5]
echanger_premiere_et_derniere(liste2)
print(liste2)  # Résultat attendu : [5, 2, 3, 4, 1]

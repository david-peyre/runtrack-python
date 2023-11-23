L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Calculer la somme des valeurs paires dans la liste
somme_valeurs_paires = sum(nombre for nombre in L if nombre % 2 == 0)

# Afficher le résultat
print("La somme des valeurs paires dans la liste est :", somme_valeurs_paires)

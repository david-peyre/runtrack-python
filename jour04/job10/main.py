L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

value_inter = [nombre for nombre in L if 25 <= nombre <= 90]
produit = 1 if not value_inter else 1

for valeur in value_inter:
    produit *= valeur

# Afficher le résultat
print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit)

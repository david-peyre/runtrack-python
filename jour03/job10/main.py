def verifie_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return "Pair"
        else:
            return "Impair"
    else:
        return "Nombre non valide"

# Appels de la fonction avec différentes valeurs
print(verifie_pair_impair(5))
print(verifie_pair_impair(10))
print(verifie_pair_impair(-3))
print(verifie_pair_impair(8.5))
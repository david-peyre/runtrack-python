def distance_toilettes(nombre_marches, hauteur_marche):
    hauteur_totale = nombre_marches * hauteur_marche / 100
    distance_jour = hauteur_totale * 2 * 5
    distance_semaine = distance_jour * 7
    return distance_semaine

# Exemple d'utilisation
nombre_marches = 10
hauteur_marche = 20 
resultat = distance_toilettes(nombre_marches, hauteur_marche)
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {resultat:.2f} m par semaine.")

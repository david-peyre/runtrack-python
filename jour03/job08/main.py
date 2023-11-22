def afficher_produits(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("poire, fraise, cassis")
    elif type == "legume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "ete":
            print("artichaut, aubergine, navet")
    else:
        print("Type ou saison non reconnu")

# Exemples d'appels de la fonction
afficher_produits("fruits", "hiver")
afficher_produits("fruits", "ete")
afficher_produits("legume", "hiver")
afficher_produits("legume", "ete")
afficher_produits("inconnu", "ete")

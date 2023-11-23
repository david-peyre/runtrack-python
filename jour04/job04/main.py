def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    
    if len(fruits) >= 3:
        fruits.insert(2, "Mangue") 
        return fruits
    else:
        print("La liste n'a pas assez d'éléments.")

# Appel de la fonction
resultat = ajouter_mangue()
if resultat:
    print(resultat)

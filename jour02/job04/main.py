while True:
    try:
        N = int(input("Entrer un entier supérieur à zéro (N) : "))
        if N <= 0:
            print("Veuillez entrer un entier supérieur à zéro.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

print(f"\nTables de multiplication de 1 à {N} :\n")

for i in range(1, N + 1):
    print(f"Table de multiplication de {i} :")
    for j in range(1, 11):
        resultat = i * j
        print(f"{i} x {j} = {resultat}")
2

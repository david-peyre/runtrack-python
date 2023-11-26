def triangle(hauteur):
    for i in range(hauteur - 1, -1, -1):
        espaces = ' ' * i
        if i == hauteur - 1:
            print(espaces + '/\\')
        elif i == 0:
            print('/' + '_' * (2 * (hauteur - 1)) + '\\')
        else:
            print(espaces + '/' + ' ' * (2 * (hauteur - 1 - i)) + '\\')

hauteur_triangle = int(input("Entrez la hauteur du triangle : "))

triangle(hauteur_triangle)


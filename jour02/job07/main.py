chaine = "abcdefghijklmnopqrstuvwxyz" * 10
leng_chaine = len(chaine)
niveau = 0
caracteres_par_niveau = 1

while niveau * caracteres_par_niveau < leng_chaine:
    debut = (niveau * (niveau + 1) // 2) * 2  
    fin = ((niveau + 1) * (niveau + 2) // 2) * 2  
    ligne = chaine[debut:fin]
    print(ligne.ljust(50))
    niveau += 1
    caracteres_par_niveau += 2

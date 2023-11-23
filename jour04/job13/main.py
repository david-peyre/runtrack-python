def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Exemple d'utilisation
my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
result = remove_duplicates(my_list)

# Afficher la liste sans doublons
print("La liste sans doublons est :", result)

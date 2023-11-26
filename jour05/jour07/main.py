def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            # Pas d'arrondie
            notes_arrondies.append(note)
        else:
            # Arrondir à un multiple de 5
            multiple5sup = (note + 4) // 5 * 5
            if multiple5sup - note < 3:
                notes_arrondies.append(multiple5sup)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
notes_eleves = [83, 72, 55, 38, 91, 60]
notes_arrondies = arrondir_notes(notes_eleves)
print("Notes initiales :", notes_eleves)
print("Notes arrondies :", notes_arrondies)

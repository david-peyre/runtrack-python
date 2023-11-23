def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0 and minutes_restantes == 0:
            print("0 heures et 0 minutes")
        elif heures == 0:
            print(f"{minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
        elif minutes_restantes == 0:
            print(f"{heures} heure{'s' if heures > 1 else ''}")
        else:
            print(f"{heures} heure{'s' if heures > 1 else ''} et {minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
    else:
        print("Nombre de minutes non valide")

# Appels de la fonction avec différentes valeurs
time_to_text(120)   
time_to_text(75)    
time_to_text(45)   
time_to_text(0)     
time_to_text(-30)    
time_to_text("abc")  
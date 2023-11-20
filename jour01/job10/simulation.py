invest = 10000
rate = 5
print("Montant initial de l'investissement :", invest, "euros")
print("Taux de rendement annuel :", rate, "%")

annual_return = (rate / 100) * invest
print("Retour sur investissement :", annual_return, "euros")

invest = (invest + 5000)
rate = (rate + 2)
annual_return = (rate / 100) * invest
print("L'investisseur augmente son capital de 5000 euros, il est désormais de", invest, "euros" )
print("Le nouveau taux de rendement a augmenté de 2 % et est à présent de", rate,"%")
print("Son retour sur investissement sur l'année est à présent de", annual_return, "euros")

invest = (invest + annual_return)
print("Il possède donc à la fin de l'année", invest, "euros investis")

invest = (invest * 0.9)
print("L'investisseur retire 10% du montant total de son investissement, ce qui le porte à", invest, "euros")

rate = rate - 1
annual_return = (rate / 100) * invest
invest = invest + annual_return
print("Suite à quoi le rendement diminue de 1 %, il est donc désormais de", rate, "%, de sorte que son retour sur investissemnt à l'année est à présent de", annual_return, "euros")
print("De sorte qu'à la fin de cette année le montant de son investissemnt sera de", invest)
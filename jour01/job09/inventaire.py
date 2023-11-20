divice = "ordinateur"
price = 1000
quantity = 500

print("article =", divice)
print("prix =", price, "euros")
print(quantity, "articles en stock")

purchase = int(input("Quelle quantité d'ordinateur voulez vous acheter ?"))
transacprice = price * purchase

if purchase<=quantity:
    print("Le montant de la transactione est de", transacprice, "euros")
    quantity = quantity - purchase
    print ("Il y a désormais", quantity, "ordinateurs en stock")
else:
    print("Il n'y a pas suffisament d'acticles en stock pour effectuer cette transaction")

price = price * 1.10
print("Du fait de l'inflation, le nouveau prix unitaire d'un ordinateur est de", price, "euros")

print("Inventaire mis à jour :")
print("article :", divice)
print("prix :", price, "euro")
print(quantity, "article(s) restant en stock") 

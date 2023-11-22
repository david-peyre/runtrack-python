num1 = float(input("Entre le premier terme de l'opération (nombre)"))
operator = input("Entre le second terme de l'opération (opérateur)")
num2 = float(input("Entre le troisième terme de l'opération (nombre)"))

def calcule(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "/":
            return "La division par zéro n'est pas définie en mathématiques" if num2 == 0 else num1 / num2
        case "*":
            return num1 * num2
        case "%":
            return num1 % num2

resultat = calcule(num1, operator, num2)
print(f"Résultat de {num1} {operator} {num2} = {resultat}")

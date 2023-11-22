num1 = int(input("Entre le premier terme de l'opération (nombre)"))
operator = input("Entre le second terme de l'opération (opérateur)")
num2 = int(input("Entre le troisième terme de l'opération (nombre)"))

def calcule(num1, operator, num2):
    if operator == "+":
        return (num1 + num2)
    elif operator == "-":
        return (num1 - num2)
    elif operator == "/":
        if num2 == 0:
            return "La division par zéro n'est pas définie en mathématiques"
        else:
            return (num1 / num2)
    elif operator == "*":
        return (num1 * num2)
    elif operator == "%":
        return (num1 % num2)

print(f"Résultat de {num1} {operator} {num2} = {calcule(num1, operator, num2)}")
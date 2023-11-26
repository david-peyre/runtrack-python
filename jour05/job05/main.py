def chiffrement_cesar(message, decalage):
    message_chiffre = ""  

    for caractere in message:
        if caractere.isalpha():  
            est_majuscule = caractere.isupper()  

            code_ascii = ord(caractere)
            nouveau_code_ascii = (code_ascii - ord('A' if est_majuscule else 'a') + decalage) % 26 + ord('A' if est_majuscule else 'a')
            caractere_chiffre = chr(nouveau_code_ascii)

            message_chiffre += caractere_chiffre
        else:
            message_chiffre += caractere  

    return message_chiffre  

# Exemple d'utilisation
message_original = "Hello, World Z!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")

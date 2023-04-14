def calcule(num1,operator,num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 * (num2/100)
    else:
        print("Operateur Invalide")


resultat=calcule(8,'+',18)
print("le resultat est ", resultat)
resultat=calcule(8,'-',2)
print("le resultat est ", resultat)
resultat=calcule(4,'*',4)
print("le resultat est ", resultat)
resultat=calcule(15,'/',3)
print("le resultat est ", resultat)








peso = int(input("escribe tu peso: "))
altura = float(input("escribe tu estatura en metros: "))

imc = peso/(altura*altura)

print("Tu IMC es: ", round(imc, 2))


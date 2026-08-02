print("el IMC es una referencia general, pero puede ser menos preciso en:")
print("- Menores de 18 años, porque se interpreta de forma diferente según edad y desarrollo")
print("- Embarazadas, porque el emparazo genera cambios en el peso y la composición corporal")
print("- Atletas o personas con alta masa mmuscular, porque el musculo aumenta el peso")
print("- Personas mayoresc on pérdida de masa muscular")
print("- Personas con ciertas condiciones médicas")

continuar = input("¿quieres continuar? (si/no): ")

if continuar == "no":
    print("¡Gracias por usar la calculadora de IMC! ¡Cuida tu salud!")
    exit()
else:
    print("¡Perfecto! Vamos a calcular tu IMC.")
    nombre = input("¡hola! ¿Cuál es tu nombre? ")
    peso = int(input("escribe tu peso: "))
    altura = float(input("escribe tu estatura en metros: "))

    imc = peso/(altura*altura)

    if imc < 18.5:
        print(f"Hola, {nombre}! Tu IMC es: ", round(imc, 2))
        print("Parece que estás por debajo del peso ideal. Intenta  mantener una alimentación variada y consumir los nutrientes que tu cuerpo necesita.")
    elif imc < 25:
        print(f"Hola, {nombre}! Tu IMC es: ", round(imc, 2))
        print("Parece que estás en un peso saludable. Sigue cuidando tu alimentación, descanso y hábitos diarios.")
    elif imc < 30:
        print(f"Hola, {nombre}! Tu IMC es: ", round(imc, 2))
        print("Parece que estás por encima del peso ideal. Pequeños cambios en tu alimentación y actividad diaria pueden ayudarte a mejorar tus hábitos.")
    else:
        print(f"Hola, {nombre}! Tu IMC es: ", round(imc, 2))
        print("Parece que estás muy por encima del peso ideal. considera mejorar tus hábitos y buscar orientación profesional para mejorar tu salud.")
    print("Recuerda que el IMC es solo una referencia y no sustituye la evaluación de un profesional de la salud. ¡Cuida tu bienestar!")


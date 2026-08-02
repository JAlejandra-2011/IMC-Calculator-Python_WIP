sexo =input("selecciona tu sexo(mujer/hombre)").strip().lower()

if sexo == "mujer":
    grupo = input("1. embarazada\n2. Atleta\n3. ninguna\nEscribe el número de tu grupo: ")
elif sexo == "hombre":
    grupo = input("1. Atleta\n2. Ninguna\nEscribe el número de tu grupo: ")
else:
    print("Sexo no válido. Por favor, selecciona 'mujer' o 'hombre'.")
    exit()

if ((grupo == "1" or grupo == "2") and sexo == "mujer") or (grupo == "1" and sexo == "hombre"):
    continuar = input("\033[31m¡Atención! El IMC puede ser menos preciso para tu grupo. ¿Deseas continuar? (si/no): \033[0m").strip().lower()
    if continuar == "no":
        print("¡Gracias por usar la calculadora de IMC! ¡Cuida tu salud!")
        exit()
    elif continuar != "si":
        print("Respuesta no válida. Por favor, escribe 'si' o 'no'.")
        exit()

# Aquí empieza el proceso de edad
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
print("\033[31msi eres menor de 18 años, embarazada, atleta o tienes alguna condición médica, consulta con un profesional de la salud para una evaluación más precisa.\033[0m]")

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
print("\033[31mnota: El IMC es una referencia general. En menores de 18 años, embarazadas, atletas y personas con alta masa muscular, puede intepretarse de forma diferente.\033[0m")

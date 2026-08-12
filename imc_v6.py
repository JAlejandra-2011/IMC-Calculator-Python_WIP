
historial = []
while True:
 while True:
     respuesta = input("¿quieres ver el historial? (si/no): ").strip().lower()
     if respuesta == "si":
         if len(historial) == 0:
             print("El historial está vacío.")
             break
         else:
              print("historial de IMC")
              for i, registro in enumerate(historial, start=1):
                 nombre, imc = registro
                 print(f"{i}. {nombre}: IMC = {round(imc, 2)}")
              break
     elif respuesta == "no":
         break
 iniciar = input("Deseas calcular tu IMC? (si/no): ").strip().lower()
 if iniciar == "no":
    print("¡Gracias por usar la calculadora de IMC!")
    break
   
 elif iniciar != "si":
    print("Respuesta no válida. Por favor, escribe 'si' o 'no'.")
    continue
 #Aqui empieza el imc
 while True:
     sexo =input("selecciona tu sexo(mujer/hombre)").strip().lower()
     if sexo == "mujer":
         grupo = input("1. embarazada\n2. Atleta\n3. ninguna\nEscribe el número de tu grupo: ")
         if  grupo not in ["1","2","3"]:
              print("Grupo no válido. Por favor, selecciona un grupo válido.")
              continue
     elif sexo == "hombre":
         grupo = input("1. Atleta\n2. Ninguna\nEscribe el número de tu grupo: ")
         if grupo not in ["1","2"]:
              print("Grupo no válido. Por favor, selecciona un grupo válido.")
              continue
     else:
         print("Sexo no válido. Por favor, selecciona 'mujer' o 'hombre'.")
         continue
     break

    
 while True:

     if (sexo == "mujer" and grupo in["1","2"]) or (grupo == "1" and sexo == "hombre"):
         continuar = input("\033[31m¡Atención! El IMC puede ser menos preciso para tu grupo. ¿Deseas continuar? (si/no): \033[0m").strip().lower()
         if continuar == "no":
             print("¡Gracias por usar la calculadora de IMC! ¡Cuida tu salud!")
             exit()
         elif continuar == "si":
             break
         else:
             print("Respuesta no válida. Por favor, escribe 'si' o 'no'.")
             continue
     break 
     
 # Aquí empieza el proceso de calcular el IMC
 while True:
     print("¡Perfecto! Vamos a calcular tu IMC.")
     print("(pulse enter para continuar)")
     input()
     nombre = input("¡hola! ¿Cuál es tu nombre? ")
     peso = int(input("escribe tu peso: "))
     if peso < 10 or peso > 300:
             print("Peso no válido. Por favor, ingresa un peso entre 10 y 300 kg.")
             continue
     altura = float(input("escribe tu estatura en metros: "))
     if altura < 0.5 or altura > 2.5:
            print("Altura no válida. Por favor, ingresa una altura entre 0.5 y 2.5 metros.")
            continue
     else:
         break

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

 continuar = input("¿Deseas calcular tu IMC nuevamente? (si/no): ").strip().lower()
 if continuar == "no":
    print("¡Gracias por usar la calculadora de IMC!")
    break
 elif continuar != "si":
    print("Respuesta no válida. Por favor, escribe 'si' o 'no'.")
    continue
 historial.append([nombre, imc])
 
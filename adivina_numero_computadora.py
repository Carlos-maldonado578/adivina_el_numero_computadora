import random

def adivina_numero_computadora(x):

    print("=========================")
    print("¡Bienvenido(a) al Juego!")
    print("=========================")

    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo... ")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #generar una predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
        
        #obtener una respuesta del user.
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta ingresa (A), si es muy baja ingresa (B). Si es correcto ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"¡Siii! la computadora adivino tu número correctamente: {prediccion}")


adivina_numero_computadora(10)
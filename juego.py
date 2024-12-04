import random

def main():
    print("¡Bienvenido al juego de adivinar el número!")
    
    # Solicitar el rango máximo
    while True:
        try:
            max_range = int(input("Introduce el número máximo del rango: "))
            if max_range <= 0:
                print("Por favor, introduce un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    # Calcular el número de intentos
    max_attempts = max_range // 20
    if max_attempts == 0:
        max_attempts = 1 

    # Generar el número a adivinar
    number_to_guess = random.randint(1, max_range)
    attempts = 0
    guessed = False

    print(f"Tienes {max_attempts} intento/s para adivinar el número entre 1 y {max_range}.")

    while attempts < max_attempts and not guessed:
        user_input = input("Introduce tu intento: ")
        attempts += 1

        # Validar la entrada
        try:
            guess = int(user_input)
        except ValueError:
            print("Entrada no válida. Debes introducir un número entero.")
            continue

        # Comparar el intento con el número a adivinar
        if guess < number_to_guess:
            print("El número a adivinar es mayor.")
        elif guess > number_to_guess:
            print("El número a adivinar es menor.")
        else:
            guessed = True
            print(f"¡Felicidades! Has adivinado el número {number_to_guess} en {attempts} intento/s.")

    if not guessed:
        print(f"Lo siento, has agotado tus intentos. El número era {number_to_guess}.")

if __name__ == "__main__":
    main()
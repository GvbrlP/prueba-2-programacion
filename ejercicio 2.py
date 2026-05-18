from random import randint

print("\n--- EJERCICIO 2: JUEGO DE ADIVINAR EL NÚMERO ---")

lim_inferior = int(input("Ingrese límite inferior: "))
lim_superior = int(input("Ingrese límite superior: "))

if lim_inferior >= lim_superior:
    print("Error: El límite inferior debe ser menor que el superior.")
else:
    numero_inicial = randint(lim_inferior, lim_superior)
    numero_final = numero_inicial

    if numero_final % 2 != 0:
        if (numero_final + 1) <= lim_superior:
            numero_final = numero_final + 1
        else:
            numero_final = numero_final - 1
    
    intento1 = int(input("Intente adivinar: "))
    
    if intento1 == numero_final:
        print("Felicitaciones, adivinó en el primer intento.") 
    else:
        if numero_final > intento1:
            print("El número es mayor.")
        else:
            print("El número es menor.")
            
        intento2 = int(input("Intente de nuevo: "))
        
        if intento2 == numero_final:
            print("Felicitaciones, adivinó en su segundo intento.")
        else:
            if numero_final > intento2:
                print("El número es mayor.")
            else:
                print("El número es menor.")
                
            print("Te daré una pista:")
            distancia1 = abs(numero_final - intento1)
            distancia2 = abs(numero_final - intento2)
            
            if distancia2 < distancia1:
                print(f"El número que buscas está más cerca de {intento2} que de {intento1}")
            else:
                print(f"El número que buscas está más cerca de {intento1} que de {intento2}")
                
            intento3 = int(input("Intente la última vez: "))
            
            if intento3 == numero_final:
                print("Felicitaciones, pudiste adivinar.")
            else:
                print("Perdiste.")
                print(f"El número era: {numero_final}")
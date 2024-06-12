import random
import time

def tirar_dado():
    return random.randint(1, 6)

def tirada_NPC():
    print("Turno del NPC...")
    time.sleep(2)
    return tirar_dado()

def Minijuego_del_dado():
    print("Bienvenido al juego del dado, aquí se demostrará que tan NPC eres a partir de jugar con uno")
    Jugador = 0
    NPC = 0

    for i in range(3):  # Tres rondas
        input("Presiona Enter para tirar el dado: ")
        print("Tirada del jugador:")
        tiro_jugador = tirar_dado()
        print(tiro_jugador)

        tiro_NPC = tirada_NPC()
        print(tiro_NPC)

        if tiro_jugador > tiro_NPC:
            Jugador += 1
        
        elif tiro_jugador < tiro_NPC:
            NPC += 1

    print("\nResultados finales:")
    print("Victorias del jugador: {}".format(Jugador))
    print("Victorias del NPC: {}".format(NPC))
    
    if Jugador > NPC:
        print("Le ganaste a un NPC, toma un poco de carbón como premio (has tenido suerte no te ilusiones)")
    elif Jugador < NPC:
        print("Un NPC te ganó???? XD")
    else:
        print("Has empatado con un NPC (no tiene por qué ser algo bueno)")


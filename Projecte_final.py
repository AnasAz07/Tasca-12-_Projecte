import Dado
import Fitxer
import Pong
import Clases
import Scrapping
import Ex_Servidor

def menu():
    op = 0
    while op<1 or op>6:
        print("""
        Programa Principal
        1. Llistes i Nums Aleatoris (Minijuego del Dado)
        2. Treballar amb Fitxers (Ticket de compra)
        3. Pong
        4. Classes
        5. Scrapping
        6. Servei Web Django
        7. Sortir
        """)
        op = int(input("Introdueix una Opció: "))
        if op<1 or op>7:
            print("Opció no vàlida \n")
        else:
            return op

op = 1
while op!= 7:
    op = menu()
    match(op):
        case 1:
            Dado.Minijuego_del_dado()
        case 2:
            Fitxer.PP()
        case 3:
            Pong.Juego()
        case 4:
            Clases.Programa_Principal()
        case 5:
            Scrapping.funscrap()
        case 6:
            Ex_Servidor.iniciar_servidor_django()
        case other:
            print("Programa Finalizado")
        
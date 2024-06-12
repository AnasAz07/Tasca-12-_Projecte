import pygame
import random

pygame.init()

resolucion = 800, 600
ANCHO, ALTO = resolucion

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (185, 0, 0)
VERDE = (0, 185, 0)
AZUL = (0, 0, 185)

# Movimiento de los objetos
PALAS = 10
BOLA_VEL = 7
TAMAÑO_BOLA = 20
FPS = 60
INCREMENTO_TIEMPO = 3000  # Tiempo en milisegundos para incrementar la velocidad de la bola
INCREMENTO_VELOCIDAD = 1  # Incremento de la velocidad de la bola

class Bola:
    def __init__(self):  # Posición Inicial (centro de la pantalla)
        self.figura = pygame.Rect(ANCHO // 2 - TAMAÑO_BOLA // 2, ALTO // 2 - TAMAÑO_BOLA // 2, TAMAÑO_BOLA, TAMAÑO_BOLA)
        self.vx = random.choice([-BOLA_VEL, BOLA_VEL])
        self.vy = random.choice([-BOLA_VEL, BOLA_VEL])

    def movimiento(self):
        self.figura.x += self.vx
        self.figura.y += self.vy
        if self.figura.top <= 0 or self.figura.bottom >= ALTO:
            self.vy *= -1

    def incrementar_velocidad(self):
        if self.vx > 0:
            self.vx += INCREMENTO_VELOCIDAD
        else:
            self.vx -= INCREMENTO_VELOCIDAD
        if self.vy > 0:
            self.vy += INCREMENTO_VELOCIDAD
        else:
            self.vy -= INCREMENTO_VELOCIDAD

    def dibujo(self, surface):
        pygame.draw.ellipse(surface, BLANCO, self.figura)  # Dibujar círculo

class Pala:
    def __init__(self, x):
        self.figura = pygame.Rect(x, ALTO // 2 - 50, 10, 100)
        self.velocidad = PALAS

    def movimiento(self, dy):
        self.figura.y += dy * self.velocidad
        self.figura.clamp_ip(pygame.Rect(0, 0, ANCHO, ALTO))

    def dibujo(self, surface):
        pygame.draw.rect(surface, VERDE, self.figura) # Dibujar rectángulo

def Juego():
    # Pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Pong PvP")
    clock = pygame.time.Clock()
    # Iniciar Palas y Bola (Posición de inicio)
    pala_1 = Pala(20)
    pala_2 = Pala(ANCHO - 30)
    bola = Bola()
    # Puntajes
    puntaje_1 = 0
    puntaje_2 = 0
    # Fuente de texto
    fuente = pygame.font.Font(None, 36)
    ultimo_incremento = pygame.time.get_ticks()

    def reiniciar_bola():
        nonlocal bola
        bola = Bola()
        pantalla.fill(AZUL)
        pala_1.dibujo(pantalla)
        pala_2.dibujo(pantalla)
        bola.dibujo(pantalla)
        pygame.display.flip()
        pygame.time.delay(1000)

    # Retraso inicial antes de comenzar el juego
    pantalla.fill(NEGRO)
    texto_inicio = fuente.render("¡El juego comenzará en 2 segundos!", True, BLANCO)
    pantalla.blit(texto_inicio, (ANCHO // 2 - texto_inicio.get_width() // 2, ALTO // 2 - texto_inicio.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

    # Bucle del juego
    while puntaje_1 < 5 and puntaje_2 < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Incrementar la velocidad de la bola cada cierto tiempo
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_incremento > INCREMENTO_TIEMPO:
            bola.incrementar_velocidad()
            ultimo_incremento = tiempo_actual

        # Teclas usadas para las palas
        keys = pygame.key.get_pressed()
        # Mover las palas basadas en las teclas presionadas
        pala_1.movimiento(keys[pygame.K_s] - keys[pygame.K_w])
        pala_2.movimiento(keys[pygame.K_DOWN] - keys[pygame.K_UP])
        # Mover la pelota
        bola.movimiento()

        # Rebotar la pelota si choca con una paleta
        if bola.figura.colliderect(pala_1.figura) or bola.figura.colliderect(pala_2.figura):
            bola.vx *= -1

        # Actualizar puntajes y reiniciar la bola si se marca un punto
        if bola.figura.left <= 0:
            puntaje_2 += 1
            reiniciar_bola()
        elif bola.figura.right >= ANCHO:
            puntaje_1 += 1
            reiniciar_bola()

        # Dibujar elementos en la pantalla
        pantalla.fill(AZUL)
        pala_1.dibujo(pantalla)
        pala_2.dibujo(pantalla)
        bola.dibujo(pantalla)

        # Mostrar los puntajes
        texto_puntaje_1 = fuente.render(f"Jugador 1: {puntaje_1}", True, BLANCO)
        texto_puntaje_2 = fuente.render(f"Jugador 2: {puntaje_2}", True, BLANCO)
        pantalla.blit(texto_puntaje_1, (10, 10))
        pantalla.blit(texto_puntaje_2, (ANCHO - texto_puntaje_2.get_width() - 10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    ganador = "Jugador 1" if puntaje_1 == 5 else "Jugador 2"
    color_ganador = ROJO if ganador == "Jugador 1" else AZUL
    texto_final = fuente.render(f"¡Se acabó el juego! Ha ganado {ganador}", True, color_ganador)
    pantalla.fill(NEGRO)
    pantalla.blit(texto_final, (ANCHO // 2 - texto_final.get_width() // 2, ALTO // 2 - texto_final.get_height() // 2))

    pygame.display.flip()
    pygame.time.delay(3000)

    pygame.quit()
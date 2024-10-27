import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
DORADO = (255, 215, 0)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego estilo Mario")

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Definir la fuente para mostrar texto
font = pygame.font.SysFont(None, 36)

# Definir el jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 100)
        self.vel_y = 0
        self.salto = False
        self.puntos = 0
        self.vidas = 3  # Vida del jugador

    def update(self):
        # Movimiento lateral
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5

        # Movimiento vertical (gravedad)
        self.vel_y += 1
        if self.salto:
            self.vel_y = -15
            self.salto = False

        self.rect.y += self.vel_y

        # Evitar que el jugador caiga por debajo de la pantalla
        if self.rect.bottom >= ALTO - 50:
            self.rect.bottom = ALTO - 50
            self.vel_y = 0

        # Añadir puntos si toca una plataforma
        if pygame.sprite.spritecollide(self, plataformas, False):
            self.puntos += 1

    def saltar(self):
        if self.rect.bottom >= ALTO - 50 or pygame.sprite.spritecollide(self, plataformas, False):
            self.salto = True

    def perder_vida(self):
        self.vidas -= 1
        if self.vidas <= 0:
            return True
        return False

# Definir una plataforma
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Definir enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, tipo_movimiento):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = 3
        self.tipo_movimiento = tipo_movimiento

    def update(self):
        if self.tipo_movimiento == 'horizontal':
            self.rect.x += self.velocidad
            if self.rect.right >= ANCHO or self.rect.left <= 0:
                self.velocidad *= -1
        elif self.tipo_movimiento == 'vertical':
            self.rect.y += self.velocidad
            if self.rect.top <= 0 or self.rect.bottom >= ALTO:
                self.velocidad *= -1

# Definir moneda
class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(DORADO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Función para mostrar puntos en la pantalla
def mostrar_puntos(pantalla, puntos):
    texto = font.render(f"Puntos: {puntos}", True, NEGRO)
    pantalla.blit(texto, (10, 10))

# Función para mostrar vidas en la pantalla
def mostrar_vidas(pantalla, vidas):
    texto = font.render(f"Vidas: {vidas}", True, NEGRO)
    pantalla.blit(texto, (10, 50))

# Crear el jugador
jugador = Jugador()

# Grupo de sprites
todos_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
monedas = pygame.sprite.Group()

todos_sprites.add(jugador)

# Crear plataformas
plataforma_base = Plataforma(0, ALTO - 50, ANCHO, 50)
todos_sprites.add(plataforma_base)
plataformas.add(plataforma_base)

# Crear plataformas flotantes
for i in range(5):
    p = Plataforma(random.randint(0, ANCHO - 100), random.randint(100, ALTO - 150), random.randint(100, 200), 20)
    todos_sprites.add(p)
    plataformas.add(p)

# Crear enemigos
enemigo1 = Enemigo(300, ALTO - 100, 50, 50, 'horizontal')
enemigo2 = Enemigo(200, 300, 50, 50, 'horizontal')
enemigo3 = Enemigo(500, 150, 50, 50, 'vertical')
todos_sprites.add(enemigo1, enemigo2, enemigo3)
enemigos.add(enemigo1, enemigo2, enemigo3)

# Crear monedas
for i in range(5):
    moneda = Moneda(random.randint(0, ANCHO - 30), random.randint(50, ALTO - 100))
    todos_sprites.add(moneda)
    monedas.add(moneda)

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.saltar()

    # Actualizar los sprites
    todos_sprites.update()

    # Verificar colisiones entre jugador y plataformas
    if pygame.sprite.spritecollide(jugador, plataformas, False):
        jugador.vel_y = 0

    # Verificar si el jugador recoge monedas
    monedas_recogidas = pygame.sprite.spritecollide(jugador, monedas, True)
    if monedas_recogidas:
        jugador.puntos += 5

    # Verificar colisión con enemigos
    if pygame.sprite.spritecollide(jugador, enemigos, False):
        if jugador.perder_vida():
            jugando = False

    # Dibujar todo en la pantalla
    pantalla.fill(BLANCO)
    todos_sprites.draw(pantalla)

    # Mostrar puntos y vidas en la pantalla
    mostrar_puntos(pantalla, jugador.puntos)
    mostrar_vidas(pantalla, jugador.vidas)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas (FPS)
    reloj.tick(60)

# Mostrar pantalla de fin del juego
pantalla.fill(BLANCO)
texto = font.render("¡Juego Terminado!", True, ROJO)
pantalla.blit(texto, (ANCHO // 2 - 100, ALTO // 2))
pygame.display.flip()
pygame.time.wait(3000)

# Cerrar Pygame
pygame.quit()
sys.exit()

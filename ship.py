import pygame
from pygame.sprite import Sprite
from resource_helper import resource_path

class Ship(Sprite):
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load(resource_path('images/ship.bmp'))
        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte
        # inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Actualiza la posicion de la nave en funcion de la bandera de movimiento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = int(self.x)

    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento
    del juego."""

    def __init__(self):
        """Inicializa el juego y crea recursos."""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        """Inicia el bucle principal para el juego."""

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

     
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Responde a pulsaciones de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responde a liberaciones de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()
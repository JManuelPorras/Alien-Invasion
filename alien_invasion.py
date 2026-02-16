import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Inicia el bucle principal para el juego."""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a liberaciones de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """Crea la flota de aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        currentx, currenty = alien_width, alien_height
        while currenty < (self.settings.screen_height - 3*alien_height):
            while currentx < (self.settings.screen_width - 2*alien_width):
                self._create_alien(currentx, currenty)
                currentx += 2*alien_width
            currentx = alien_width
            currenty += alien_height*2

    def _create_alien(self, x_position, y_position):
        """Crea un alienígena y lo coloca en la fila."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Responde adecuadamente si algún alien ha llegado a un
        borde."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Comprueba si la flota está en un borde, después actualiza las
        posiciones."""
        self._check_fleet_edges()
        self.aliens.update()

    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas."""
        self.bullets.update()
        # Deshace las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()
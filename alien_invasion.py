import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from resource_helper import resource_path

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento
    del juego."""

    def __init__(self):
        """Inicializa el juego y crea recursos."""
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Cargar sonidos
        self._load_sounds()

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = False
        self.play_button = Button(self, "Play")

    def _load_sounds(self):
        """Carga la música y los efectos de sonido."""
        pygame.mixer.music.load(resource_path('sounds/background.mp3'))
        pygame.mixer.music.set_volume(0.5)
        
        self.laser_sound = pygame.mixer.Sound(resource_path('sounds/laser.wav'))
        self.explosion_sound = pygame.mixer.Sound(resource_path('sounds/explosion.wav'))
        self.explosion_sound.set_volume(1.0)

    def run_game(self):
        """Inicia el bucle principal para el juego."""

        while True:
            self._check_events()

            if self.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Inicia un juego nuevo cuando el jugador hace clic en Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Restablece las configuraciones del juego.
            self.settings.initialize_dynamic_settings()

            # Restablece las estadísticas del juego.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Reproducir música de fondo
            pygame.mixer.music.play(-1)

            # Se deshace de los aliens y las balas que quedan.
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y centra la nave.
            self._create_fleet()
            self.ship.center_ship()

            # Oculta el cursor del ratón.
            pygame.mouse.set_visible(False)
    
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
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()
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
        # Busca colisiones alien-nave.
        if pygame.sprite.spritecollideany(self.ship, self.aliens): # type: ignore
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Comprueba si algún alien ha llegado al fondo de la
        pantalla."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Trata esto como si la nave hubiese sido alcanzada.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Responde al impacto de un alien en la nave."""
        # Se reproduce el sonido de explosión
        self.explosion_sound.play()

        # Reduce ships_left y actualiza el marcador.
        self.stats.ships_left -= 1
        self.sb.prep_ships()

        if self.stats.ships_left > 0:
            # Se deshace de los aliens y balas restantes.
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y centra la nave.
            self._create_fleet()
            self.ship.center_ship()

            # Pausa.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            # Detener la música de fondo al perder
            pygame.mixer.music.stop()

    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.laser_sound.play()

    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas."""
        self.bullets.update()
        # Deshace las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
         
    def _check_bullet_alien_collisions(self):
        """Responde a las colisiones bala-alien."""
        # Busca balas que hayan dado a aliens.
        # Si hay, se deshace de la bala y del alien.
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # Destruye las balas existentes y crea una flota nueva.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Aumenta el nivel.
            self.stats.level += 1
            self.sb.prep_level()

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()
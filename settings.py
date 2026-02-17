class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion."""

    def __init__(self):
        """Inicializa la configuración estatica del juego."""

        # Configuración de la pantalla
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.fullscreen = True

        # Configuración de las balas.
        self.bullet_width = 3000 # estaba en 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuraciones de alien.
        self.fleet_drop_speed = 10

        # Configuraciones de estadísticas
        self.ship_limit = 3

        # Rapidez con la que se acelera el juego
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa las configuraciones que cambian durante el juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        # fleet_direction de 1 representa la derecha; -1 representa la izquierda.
        self.fleet_direction = 1

    def increase_speed(self):
        """Incrementa las configuraciones de velocidad."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion."""

    def __init__(self):
        """Inicializa la configuración del juego."""

        # Configuración de la pantalla
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.fullscreen = False

        # Configuración de las balas.
        self.bullet_speed = 4.0
        self.bullet_width = 3000 # estaba en 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuraciones de alien.
        self.alien_speed = 1 #estaba en 1
        self.fleet_drop_speed = 10
        # fleet_direction de 1 representa derecha; -1 representa izquierda.
        self.fleet_direction = 1

        # Configuraciones de estadísticas
        self.ship_speed = 2.0
        self.ship_limit = 3

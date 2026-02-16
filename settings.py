class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion."""

    def __init__(self):
        """Inicializa la configuración del juego."""

        # Configuración de la pantalla
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2
        self.fullscreen = False
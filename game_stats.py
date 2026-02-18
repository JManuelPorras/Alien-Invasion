import json
from pathlib import Path

class GameStats:
    """Sigue las estadísticas de Alien Invasion."""

    def __init__(self, ai_game):
        """Inicializa las estadísticas."""
        self.settings = ai_game.settings
        self.load_high_score()
        self.reset_stats()

    def load_high_score(self):
        """Carga la puntuación más alta desde un archivo JSON."""
        path = Path('high_score.json')
        try:
            if path.exists():
                contents = path.read_text()
                self.high_score = json.loads(contents)
            else:
                self.high_score = 0
        except (ValueError, FileNotFoundError):
            self.high_score = 0

    def save_high_score(self):
        """Guarda la puntuación más alta en un archivo JSON."""
        path = Path('high_score.json')
        contents = json.dumps(self.high_score)
        path.write_text(contents)
        
    def reset_stats(self):
        """Inicializa las estadísticas que pueden cambiar durante el
        juego."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
# Alien Invasion 🛸

¡Bienvenido a **Alien Invasion**! Un juego de disparos estilo arcade inspirado en el clásico Space Invaders, desarrollado en Python utilizando la librería **Pygame**.

## 📝 Descripción
En este juego, controlas una nave espacial con la misión de defender la Tierra de una flota de alienígenas que desciende progresivamente. Tu objetivo es destruir tantos aliens como sea posible, subir de nivel y alcanzar la puntuación más alta antes de que los aliens destruyan tu nave o lleguen a la superficie.

## 🚀 Características (v1.0)
- **Jugabilidad Dinámica**: La dificultad aumenta (velocidad y puntos) a medida que eliminas flotas completas.
- **Sistema de Puntuación**: Registro de puntos por nivel, nivel actual y marcador de puntuación más alta (*High Score*).
- **Vidas Limitadas**: Cuentas con 3 naves antes de que el juego termine.
- **Experiencia Sonora**:
  - Música de fondo envolvente.
  - Efectos de sonido para disparos láser.
  - Efectos de sonido para explosiones al ser impactado.
- **Interfaz Fluida**: Pantalla de inicio con botón "Play" y soporte para pantalla completa.

## 🛠️ Requisitos
- **Python 3.x**
- **Pygame**: Puedes instalarlo ejecutando:
  ```bash
  pip install pygame
  ```

## 📦 Instalación y Ejecución
1. Clona o descarga este repositorio.
2. Asegúrate de tener las carpetas `images/` y `sounds/` con los recursos necesarios:
   - `images/`: `ship.bmp`, `alien.bmp`
   - `sounds/`: `background.mp3`, `laser.wav`, `explosion.wav`
3. Ejecuta el archivo principal:
   ```bash
   python alien_invasion.py
   ```

## 🎮 Controles
- **Flecha Derecha / Izquierda**: Mover la nave.
- **Barra Espaciadora**: Disparar láser.
- **Tecla Q**: Salir del juego.
- **Ratón**: Hacer clic en "Play" para iniciar.

## 📂 Estructura del Proyecto
- `alien_invasion.py`: Punto de entrada y gestión del bucle principal.
- `settings.py`: Configuraciones generales del juego.
- `ship.py` / `alien.py` / `bullet.py`: Clases de los objetos del juego.
- `game_stats.py` / `scoreboard.py`: Seguimiento de estadísticas y UI.
- `button.py`: Clase para la creación de botones interactivos.

---
Desarrollado con ❤️ en Python.

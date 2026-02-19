import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def persistent_path(filename):
    """ Returns a path for persistent data (like high scores) 
    next to the executable. """
    if getattr(sys, 'frozen', False):
        # The application is running as a bundle
        base_path = os.path.dirname(sys.executable)
    else:
        # The application is running in a normal Python environment
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, filename)

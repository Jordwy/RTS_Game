from enum import Enum

class ScreenSetting(Enum):
    WIDTH = 1280
    HEIGHT = 720
    FPS = 60

class GameSettings(Enum):
    WORLD_WIDTH = 2000
    WORLD_HEIGHT = 2000
    WORLD_SURFACE_COLOR = (34, 139, 34)  
    '''Forest Green. RGB: 34, 139, 34'''
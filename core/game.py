import pygame
from core.config import ScreenSetting, GameSettings
from entities.buildings import Building
from entities.units import Unit

###########################################################################
# Settings
SCREEN_WIDTH = ScreenSetting.WIDTH
SCREEN_HEIGHT = ScreenSetting.HEIGHT
WORLD_WIDTH = GameSettings.WORLD_WIDTH
WORLD_HEIGHT = GameSettings.WORLD_HEIGHT
WORLD_SURFACE_COLOR = GameSettings.WORLD_SURFACE_COLOR
###########################################################################

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.world_surface = pygame.Surface((WORLD_WIDTH,  WORLD_HEIGHT))
        self.world_surface.fill(WORLD_SURFACE_COLOR)
        
        self.camera_x = 0
        self.camera_y = 0
        self.camera_speed = 5

        self.buildings = [Building(500, 500)]
        self.units = []
        
        self.selecting = False
        self.select_start = (0, 0)
        self.selected_units = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Start selection box
                self.selecting = True
                self.select_start = pygame.mouse.get_pos()

            elif event.button == 3:  # Right mouse button
                # Move selected units to click location
                mouse_x, mouse_y = pygame.mouse.get_pos()
                world_x = mouse_x + self.camera_x
                world_y = mouse_y + self.camera_y
                for u in self.selected_units:
                    u.target_pos = (world_x, world_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # Finish selection
                self.selecting = False
                select_end = pygame.mouse.get_pos()

                x1, y1 = self.select_start
                x2, y2 = select_end
                rect_left = min(x1, x2)
                rect_top = min(y1, y2)
                rect_width = abs(x2 - x1)
                rect_height = abs(y2 - y1)
                selection_rect = pygame.Rect(rect_left, rect_top, rect_width, rect_height)

                self.selected_units = []
                for u in self.units:
                    screen_x = u.x - self.camera_x
                    screen_y = u.y - self.camera_y
                    if selection_rect.collidepoint(screen_x, screen_y):
                        self.selected_units.append(u)

        elif event.type == pygame.KEYDOWN:
            # Press 'U' to spawn a unit at (600,600) for testing
            if event.key == pygame.K_u:
                self.units.append(Unit(600, 600))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.camera_x += self.camera_speed
        if keys[pygame.K_LEFT]:
            self.camera_x -= self.camera_speed
        if keys[pygame.K_DOWN]:
            self.camera_y += self.camera_speed
        if keys[pygame.K_UP]:
            self.camera_y -= self.camera_speed

        self.camera_x = max(0, min(self.camera_x, WORLD_WIDTH - SCREEN_WIDTH))
        self.camera_y = max(0, min(self.camera_y, WORLD_HEIGHT - SCREEN_HEIGHT))

        # Update units
        for u in self.units:
            u.update()

    def draw(self):
        viewport = pygame.Rect(self.camera_x, self.camera_y, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.blit(self.world_surface, (0, 0), viewport)

        # Draw buildings
        for b in self.buildings:
            b.draw(self.screen, self.camera_x, self.camera_y)

        # Draw units and indicate selection
        for u in self.units:
            u.draw(self.screen, self.camera_x, self.camera_y)
            if u in self.selected_units:
                screen_x = int(u.x - self.camera_x)
                screen_y = int(u.y - self.camera_y)
                # Draw a small highlight around the unit
                pygame.draw.circle(self.screen, (255,255,0), (screen_x, screen_y), u.size+2, 1)

        # Draw selection box if currently selecting
        if self.selecting:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x1, y1 = self.select_start
            rect_left = min(x1, mouse_x)
            rect_top = min(y1, mouse_y)
            rect_width = abs(mouse_x - x1)
            rect_height = abs(mouse_y - y1)
            pygame.draw.rect(self.screen, (255,255,255), (rect_left, rect_top, rect_width, rect_height), 1)

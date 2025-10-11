import pygame
from .layout import compute_positions

NODE_RADIUS = 20
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)
LINE_COLOR = (200, 200, 200)

class AVLVisualizer:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont(None, FONT_SIZE)

    def draw(self, root):
        self.surface.fill((0, 0, 0))  
        if root is None:
            return
        positions = {}
        compute_positions(root, 400, 50, 200, positions)
        # draw lines
        for node, (x, y) in positions.items():
            if node.left:
                x2, y2 = positions[node.left]
                pygame.draw.line(self.surface, LINE_COLOR, (x, y), (x2, y2), 2)
            if node.right:
                x2, y2 = positions[node.right]
                pygame.draw.line(self.surface, LINE_COLOR, (x, y), (x2, y2), 2)
        # draw nodes 
        for node, (x, y) in positions.items():
            pygame.draw.circle(self.surface, (50, 150, 200), (int(x), int(y)), NODE_RADIUS)
            text_surf = self.font.render(str(node.key), True, FONT_COLOR)
            text_rect = text_surf.get_rect(center=(x, y))
            self.surface.blit(text_surf, text_rect)

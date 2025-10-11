import pygame

class Controller:
    def __init__(self, tree, visualizer):
        self.tree = tree
        self.visualizer = visualizer
        self.root_node = None
        # You may define rectangles for buttons: Insert, Delete, Clear
        self.buttons = {
            "Insert": pygame.Rect(50, 550, 80, 30),
            "Delete": pygame.Rect(150, 550, 80, 30),
            "Clear": pygame.Rect(250, 550, 80, 30),
        }
        self.user_input = ""  # store string input from keyboard

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                # On Enter, do insert or delete? You might add a mode toggle
                pass
            else:
                if event.unicode.isdigit():
                    self.user_input += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for name, rect in self.buttons.items():
                if rect.collidepoint(pos):
                    val = int(self.user_input) if self.user_input.isdigit() else None
                    if val is not None:
                        if name == "Insert":
                            self.root_node = self.tree.insert(self.root_node, val)
                        elif name == "Delete":
                            self.root_node = self.tree.delete(self.root_node, val)
                    if name == "Clear":
                        self.root_node = None
                    self.user_input = ""

                    


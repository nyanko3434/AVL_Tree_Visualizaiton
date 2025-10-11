import pygame

class Controller:
    def __init__(self, tree, visualizer):
        self.tree = tree
        self.visualizer = visualizer
        self.root_node = None

        self.mode = "insert on enter"
        self.user_input = ""

        self.buttons = {
            "Insert": pygame.Rect(50, 550, 80, 30),
            "Delete": pygame.Rect(150, 550, 80, 30),
            "Clear": pygame.Rect(250, 550, 80, 30),
            "Mode": pygame.Rect(650, 10, 150, 30)
        }

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                if self.user_input.isdigit():
                    num = int(self.user_input)
                    if self.mode == "insert on enter":
                        self.root_node = self.tree.insert(self.root_node, num)
                    else:
                        self.root_node = self.tree.delete(self.root_node, num)
                    self.user_input = ""
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
                        self.user_input = ""
                    if name == "Mode":
                        self.mode = "delete on enter" if self.mode == "insert on enter" else "insert on enter"
                    elif name == "Clear":
                        self.root_node = None
                        self.user_input = ""

                    


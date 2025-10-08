import tk
from .layout import compute_positions

NODE_RADIUS = 20

class AVLVisualizer:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, root):
        self.canvas.delete("all")
        if not root:
            return
        positions = {}
        compute_positions(root, 400, 50, 200, positions)
        for node, (x, y) in positions.items():
            if node.left:
                x_left, y_left = positions[node.left]
                self.canvas.create_line(x, y, x_left, y_left, fill="gray", width=2)
            if node.right:
                x_right, y_right = positions[node.right]
                self.canvas.create_line(x, y, x_right, y_right, fill="gray", width=2)
        for node, (x, y) in positions.items():
            self.canvas.create_oval(x - NODE_RADIUS, y - NODE_RADIUS, x + NODE_RADIUS, y + NODE_RADIUS, fill="#66b3ff")
            self.canvas.create_text(x, y, text=str(node.key), font=("Arial", 12, "bold"))

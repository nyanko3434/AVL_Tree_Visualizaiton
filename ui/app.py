import tk
from avl_tree.tree import AVLTree
from visualization.visualizer import AVLVisualizer

class AVLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AVL Tree Visualization")
        self.tree = AVLTree()
        self.root_node = None

        # Canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Controls
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)
        tk.Label(control_frame, text="Enter value:").pack(side=tk.LEFT)
        self.entry = tk.Entry(control_frame, width=10)
        self.entry.pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Insert", command=self.insert_value).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Delete", command=self.delete_value).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Clear", command=self.clear_canvas).pack(side=tk.LEFT, padx=5)

        self.visualizer = AVLVisualizer(self.canvas)

    def insert_value(self):
        val = self.entry.get()
        if val.isdigit():
            self.root_node = self.tree.insert(self.root_node, int(val))
            self.visualizer.draw(self.root_node)
            self.entry.delete(0, tk.END)

    def delete_value(self):
        val = self.entry.get()
        if val.isdigit():
            self.root_node = self.tree.delete(self.root_node, int(val))
            self.visualizer.draw(self.root_node)
            self.entry.delete(0, tk.END)

    def clear_canvas(self):
        self.root_node = None
        self.visualizer.draw(None)

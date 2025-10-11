# 🌳 AVL Tree Visualization (Python + Pygame)

An interactive visualization tool to demonstrate **AVL Tree insertion and deletion** using **Python** and **Pygame**.  
This project helps users understand how AVL trees maintain balance through rotations after each operation.

---

## 🎯 **Project Overview**

An **AVL Tree** is a self-balancing Binary Search Tree (BST) where the height difference between left and right subtrees of any node is at most 1.  
This project visually shows:
- Node **insertions**
- Node **deletions**
- **Rotations** (Left, Right, Left-Right, Right-Left)
- Real-time **balancing and height updates**

Built using **Python + Pygame**, this tool dynamically animates the structure of the AVL tree as operations are performed.

---



## 🗂️ **Project Structure**
```text
AVL_Tree_Visualization/
│
├── main.py # Entry point
├── requirements.txt # Dependencies (pygame)
├── run_project.sh # Bash script to auto-setup & run
│
├── avl_tree/ # Core AVL logic
│ ├── init.py
│ ├── node.py # Node structure
│ ├── tree.py # AVL insert/delete logic
│ └── utils.py # Helper functions
│
├── visualization/ # Drawing logic
│ ├── init.py
│ ├── visualizer.py # Pygame drawing routines
│ └── layout.py # Node layout (positions)
│
└── ui/ # User interaction layer
├── init.py
└── controller.py # Button click & key handling
```

---

## ⚙️ **Installation and Setup**

### 🧠 Prerequisites
- Python 3.8+
- Pygame library

---

### Run using the Bash script

1. Make the script executable:
   ```bash
   chmod +x run_project.sh
   ```
2. Run the project:
   ```bash
   ./run_project.sh
   ```

## User Interface

| Button                      | Function                                                                  |
| --------------------------- | ------------------------------------------------------------------------- |
| **Insert**                  | Inserts the number entered in the input field into the AVL tree.          |
| **Delete**                  | Deletes the number entered in the input field from the AVL tree.          |
| **Clear**                   | Clears the entire AVL tree.                                               |
| **Mode (top-right toggle)** | Click to switch between **Insert on Enter** and **Delete on Enter** mode. |

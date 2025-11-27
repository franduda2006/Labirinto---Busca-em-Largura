# filepath: maze-solver/src/main.py

import tkinter as tk
from gui import MazeEditorGUI

def main():
    root = tk.Tk()
    root.title("Maze Solver")
    app = MazeEditorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
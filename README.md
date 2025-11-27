# Maze Solver

This project implements an interactive maze solver using the Breadth-First Search (BFS) algorithm. The maze is modeled as a 2D grid, and the application features a graphical user interface (GUI) built with Tkinter.

## Features

- Interactive maze editing: Users can create and modify mazes using a simple interface.
- BFS algorithm: The application uses the BFS algorithm to find the shortest path from the start to the end of the maze.
- Visualization: The maze and the solving process are visually represented, allowing users to see the algorithm in action.

## Project Structure

```
maze-solver
├── src
│   ├── main.py         # Entry point of the application
│   ├── bfs.py          # Implementation of the BFS algorithm
│   ├── gui.py          # GUI management
│   ├── maze.py         # Maze data structure and management
│   └── utils.py        # Utility functions
├── requirements.txt     # Project dependencies
├── .gitignore           # Files to ignore in version control
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd maze-solver
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Once the application is running, you can:

- Draw walls and paths in the maze.
- Set the start and end points.
- Start the BFS algorithm to find the solution.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

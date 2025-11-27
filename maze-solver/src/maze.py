class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.start = None
        self.end = None

    def set_start(self, x, y):
        self.start = (x, y)
        self.grid[y][x] = 1  # Mark start

    def set_end(self, x, y):
        self.end = (x, y)
        self.grid[y][x] = 2  # Mark end

    def toggle_wall(self, x, y):
        if self.grid[y][x] == 0:
            self.grid[y][x] = 3  # Mark wall
        elif self.grid[y][x] == 3:
            self.grid[y][x] = 0  # Remove wall

    def is_valid_move(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] != 3

    def get_neighbors(self, x, y):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if self.is_valid_move(x + dx, y + dy):
                neighbors.append((x + dx, y + dy))
        return neighbors

    def reset(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.start = None
        self.end = None
def get_color(name):
    colors = {
        "wall": "black",
        "path": "white",
        "start": "green",
        "end": "red",
        "visited": "blue",
        "current": "yellow"
    }
    return colors.get(name, "white")

def reset_maze(maze):
    for row in maze:
        for cell in row:
            cell.state = "wall" if cell.is_wall else "path"

def is_valid_move(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and not maze[x][y].is_wall

def draw_grid(canvas, maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            color = get_color(maze[x][y].state)
            canvas.create_rectangle(y * 20, x * 20, (y + 1) * 20, (x + 1) * 20, fill=color, outline="gray")
            
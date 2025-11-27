def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.pop(0)

        if current == end:
            return reconstruct_path(parent, start, end)

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= neighbor[0] < rows and
                    0 <= neighbor[1] < cols and
                    maze[neighbor[0]][neighbor[1]] == 0 and
                    neighbor not in visited):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return None  # No path found


def reconstruct_path(parent, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

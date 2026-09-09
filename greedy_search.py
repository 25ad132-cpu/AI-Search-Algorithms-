
import heapq

grid = [
    ['S', '.', '.', '.'],
    ['.', '#', '#', '.'],
    ['.', '.', '.', '.'],
    ['.', '#', '.', 'G']
]

start = (0, 0)
goal = (3, 3)

def heuristic(node):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def greedy_search():
    queue = [(heuristic(start), start, [start])]
    visited = set()

    while queue:
        h, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        row, col = current

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 4 and 0 <= nc < 4:
                if grid[nr][nc] != '#':
                    if (nr, nc) not in visited:
                        heapq.heappush(
                            queue,
                            (
                                heuristic((nr, nc)),
                                (nr, nc),
                                path + [(nr, nc)]
                            )
                        )

path = greedy_search()

print("Robot Path:")

for position in path:
    print(position)

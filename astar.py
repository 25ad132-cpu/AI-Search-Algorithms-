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

def astar():
    queue = [(heuristic(start), 0, start, [start])]
    visited = set()

    while queue:
        f, cost, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, cost

        row, col = current

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 4 and 0 <= nc < 4:
                if grid[nr][nc] != '#':
                    neighbor = (nr, nc)

                    if neighbor not in visited:
                        new_cost = cost + 1
                        new_f = new_cost + heuristic(neighbor)

                        heapq.heappush(
                            queue,
                            (
                                new_f,
                                new_cost,
                                neighbor,
                                path + [neighbor]
                            )
                        )

path, cost = astar()

print("Game Character Path:")

for position in path:
    print(position)

print("Total Steps:", cost)

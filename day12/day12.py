from itertools import product

def get_pos(height_map, marker):
    return [
        (i, row.index(marker)) 
        for i, row in enumerate(height_map) 
        if marker in row
    ]

def bfs(graph, start, end):
    queue = [[start]]
    visited = set()
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        elif node not in visited:
            for neighbour in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)

if __name__ == "__main__":
    with open("day12.txt", "r") as f:
        height_map = f.read().split("\n")

    s = get_pos(height_map, "S")[0]
    e = get_pos(height_map, "E")[0]
    starts = get_pos(height_map, "a")

    height_map[s[0]] =  height_map[s[0]].replace("S", "a")
    height_map[e[0]] = height_map[e[0]].replace("E", "z")
    height_map = [[ord(char) for char in row] for row in height_map]

    graph = {}
    length = len(height_map)
    width = len(height_map[0])
    for y in range(length):
        for x in range(width):
            x_range = range(max(x-1, 0), min(x+2, width))
            y_range = range(max(y-1, 0), min(y+2, length))
            x_neighbours = set(product([y], x_range))
            y_neighbours = set(product(y_range, [x]))
            
            neighbours = x_neighbours.union(y_neighbours)
            neighbours.remove((y, x))
            neighbours = [
                (j, i)
                for j, i in neighbours 
                if height_map[y][x] + 1 >= height_map[j][i]
            ]
            
            graph[(y ,x)] = neighbours

    print(f"Part 1: {len(bfs(graph, s, e)) - 1}")

    path_lengths = []
    for s in starts:
        path = bfs(graph, s, e)
        if path:
            path_lengths.append(len(path) - 1)
    print(f"Part 2: {min(path_lengths)}")
from itertools import product

def count_connected_nodes_sides(nodes):
    total_sides = 6 * len(nodes)
    for node in nodes:
        for a in ADJACENT:
            if tuple(sum(x) for x in zip(node, a)) in nodes:
                total_sides -= 1
    return total_sides

def bfs(graph, start, end):
    queue = [[start]]
    visited = set()
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end: return path
        elif node not in visited:
            for a in ADJACENT:
                neighbour = tuple(sum(x) for x in zip(node, a))
                if neighbour in graph:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
            visited.add(node)

ADJACENT = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

if __name__ == "__main__":
    with open("day18.txt", "r") as f:
        cubes = set(tuple(int(v) for v in cube.split(",")) for cube in f.read().split("\n"))

    total_sides = count_connected_nodes_sides(cubes)
    print(f"Part 1: {total_sides}")

    max_x, max_y, max_z = [max(cubes, key=lambda x: x[i])[i] + 1 for i in range(3)]
    air = set(product(range(max_x), range(max_y), range(max_z))) - cubes
    trapped_air = [node for node in air if not bfs(air, node, (0, 0, 0))]
    print(f"Part 2: {total_sides - count_connected_nodes_sides(trapped_air)}")
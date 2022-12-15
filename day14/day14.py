import numpy as np
from itertools import product

def check_below(sand_pos):
    down = cave_map.get(tuple(sand_pos + [1, 0]), 0)
    left = cave_map.get(tuple(sand_pos + [1, -1]), 0)
    right = cave_map.get(tuple(sand_pos + [1, 1]), 0)
    
    return down, left, right

if __name__ == "__main__":
    with open("day14.txt", "r") as f:
        cave_scan = []
        max_y = 0
        for rock in f.read().split("\n"):
            coords = []
            for coord in rock.split(" -> "):
                x, y = [int(value) for value in coord.split(",")]
                if y > max_y: max_y = y
                coords.append((x, y))
            cave_scan.append(coords)

    cave_map = {}
    for rock in cave_scan:
        for i in range(len(rock) - 1):
            x1, x2 = rock[i][0], rock[i+1][0]
            y1, y2 = rock[i][1], rock[i+1][1]

            line_x = list(range(min(x1, x2), max(x1, x2) + 1))
            line_y = list(range(min(y1, y2), max(y1, y2) + 1))
            
            for x, y in product(line_x, line_y):
                cave_map[y, x] = 1

    sand_pos = np.array([0, 500])
    sand_at_rest = 0
    part1_complete = False

    while cave_map.get((0,500), 1) != 2:
        sand_pos = np.array([0, 500])
        
        while not all(check_below(sand_pos)):
            down, left, right = check_below(sand_pos)

            if sand_pos[0] > max_y:
                if not part1_complete:
                    print(f"Part 1: {sand_at_rest}")
                    part1_complete = True
                break
            elif down == 0: sand_pos = sand_pos + [1, 0]
            elif left == 0: sand_pos = sand_pos + [1, -1]
            elif right == 0: sand_pos = sand_pos + [1, 1]

        cave_map[tuple(sand_pos)] = 2
        sand_at_rest += 1
        
    print(f"Part 2: {sand_at_rest}")
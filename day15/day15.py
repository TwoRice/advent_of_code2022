import re
from itertools import product

def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == "__main__":
    with open("day15.txt", "r") as f:
        sensor_data = [[int(v) for v in re.findall(r"-*\d+", sensor)] for sensor in f.read().split("\n")]

    sensor_map = {}
    for sensor_x, sensor_y, beacon_x, beacon_y in sensor_data:
        beacon_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensor_map[(sensor_y, sensor_x)] = beacon_dist

    blocked_x = set()
    for (sensor_y, sensor_x), dist in sensor_map.items():
        signal_str = abs(sensor_y - 2000000) - dist
        if signal_str <= 0:
            blocked_x.update(set(range(sensor_x + signal_str, sensor_x - signal_str + 1)))

    print(f"Part 1: {len(blocked_x) - 1}")

    perimiter_points = set()
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for (sensor_y, sensor_x), dist in sensor_map.items():
        sensor_edge = zip(range(dist + 2), range(dist + 1, -1, -1))
        for (y_dist, x_dist), (y_dir, x_dir) in product(sensor_edge, directions):
            y_edge, x_edge = sensor_y + (y_dir * y_dist), sensor_x + (x_dir * x_dist)
            if y_edge <= 4000000 and x_edge <= 4000000 and y_edge >= 0 and x_edge >= 0: perimiter_points.add((y_edge, x_edge))

    for y, x in perimiter_points:
        for (sensor_y, sensor_x), dist in sensor_map.items():
            isolated_point = True
            if manhattan_distance(x, sensor_x, y, sensor_y) <= dist:
                isolated_point = False
                break
                
        if isolated_point:
            break
    
    print(f"Part 2: {4000000 * x + y}")
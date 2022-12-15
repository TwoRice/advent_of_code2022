import re
from itertools import product

def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == "__main__":
    with open("day15.txt", "r") as f:
        sensor_data = [[int(v) for v in re.findall(r"-*\d+", sensor)] for sensor in f.read().split("\n")]

    sensor_map = {}
    for sensor_x, sensor_y, beacon_x, beacon_y in sensor_data:
        beacon_dist = manhattan_distance(sensor_x, beacon_x, sensor_y, beacon_y)
        sensor_map[(sensor_y, sensor_x)] = beacon_dist

    blocked_x = set()
    for (sensor_y, sensor_x), dist in sensor_map.items():
        signal_str = abs(sensor_y - 2000000) - dist
        if signal_str <= 0:
            blocked_x.update(set(range(sensor_x + signal_str, sensor_x - signal_str + 1)))

    print(f"Part 1: {len(blocked_x) - 1}")
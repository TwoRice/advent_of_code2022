import numpy as np

def move_rock(chamber, rock_pos, move):
    new_rock_pos = rock_pos + move
    if 2 not in chamber[new_rock_pos[0], new_rock_pos[1]]:
        chamber[rock_pos[0], rock_pos[1]] = 0
        chamber[new_rock_pos[0], new_rock_pos[1]] = 1
        rock_pos = new_rock_pos
        return True, chamber, rock_pos
    return False, chamber, rock_pos

def drop_rock(chamber, n, i, empty_space):
    # Spawn rock
    chamber = np.concatenate([rocks[n], empty_space, chamber])
    rock_pos = np.array(np.where(rocks[n] == 1))
    
    while True:
        # Move left or right
        move = jet_pattern[i % len(jet_pattern)]
        i += 1
        if move == ">" and 6 not in rock_pos[1]:
            _, chmaber, rock_pos = move_rock(chamber, rock_pos, [[0], [1]])
        elif move == "<" and 0 not in rock_pos[1]:
            _, chmaber, rock_pos = move_rock(chamber, rock_pos, [[0], [-1]])
        
        # move down
        moved, chmaber, rock_pos = move_rock(chamber, rock_pos, [[1], [0]])
        
        # Rock stops
        if not moved:
            chamber[rock_pos[0], rock_pos[1]] += 1
            chamber = chamber[~np.all(chamber == 0, axis=1)]
            return chamber, i

def simulate_rocks(n):
    chamber = np.ones((1, 7)) * 2
    empty_space = np.zeros((3, 7))
    heights = []
    rocks_dropped = 0
    i = 0
    no_pattern = True
    
    for j in range(n):
        n = rocks_dropped % 5
        chamber, i = drop_rock(chamber, n, i, empty_space)
        rocks_dropped += 1
        heights.append(chamber.shape[0] - 1)

    return heights

def find_pattern(values):
    n = len(values)
    longest_pattern = []
    for pattern_length in range(1, n//2 + 1):
        for i in range(n - 2*pattern_length + 1):
            pattern = values[i:i+pattern_length]
            if values[i:i+pattern_length] == values[i+pattern_length:i+2*pattern_length]:
                if len(pattern) > len(longest_pattern):
                    longest_pattern = pattern

    return longest_pattern

def find_sublist(lst, sublist):
    sub_len = len(sublist)
    for i in range(len(lst)):
        if lst[i:i+sub_len] == sublist:
            return i
    return -1

if __name__ == "__main__":
    with open("day17.txt", "r") as f:
        jet_pattern = f.read()

    rocks = [
        np.array([[0, 0, 1, 1, 1, 1, 0]]),
        np.array([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]]),
        np.array([[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0]]),
        np.array([[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]),
        np.array([[0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0]]),
    ]

    print(f"Part 1: {simulate_rocks(2022)[-1]}")

    heights = simulate_rocks(5000)
    height_diffs = np.diff(heights).tolist()
    pattern = find_pattern(height_diffs)
    offset = find_sublist(height_diffs, pattern)
    cycles = (1000000000000 - offset) // len(pattern)
    remainder  = (1000000000000 - offset) % len(pattern)
    print(f"Part 1: {heights[offset] + (sum(pattern) * cycles) + sum(pattern[:remainder-1])}")
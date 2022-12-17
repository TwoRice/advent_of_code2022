import numpy as np

def move_rock(chamber, rock_pos, move):
    new_rock_pos = rock_pos + move
    if 2 not in chamber[new_rock_pos[0], new_rock_pos[1]]:
        chamber[rock_pos[0], rock_pos[1]] = 0
        chamber[new_rock_pos[0], new_rock_pos[1]] = 1
        rock_pos = new_rock_pos
        return True, chamber, rock_pos
    return False, chamber, rock_pos

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

    chamber = np.ones((1, 7)) * 2
    empty_space = np.zeros((3, 7))
    total_height = 0
    i = 0

    for j in range(2022):
        # Check for new floor
        new_floors = np.where(np.all(chamber[:-1] == 2, axis=1))[0]
        if len(new_floors > 0): 
            total_height += chamber.shape[0] - new_floors[0] - 1
            chamber = chamber[:new_floors[0] + 1]
        
        # Spawn rock
        n = j % 5
        chamber = np.concatenate([rocks[n], empty_space, chamber])
        rock_pos = np.array(np.where(rocks[n] == 1))
        
        at_rest = False
        while not at_rest:
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
                at_rest = True
                chamber = chamber[~np.all(chamber == 0, axis=1)]

    print(f"Part 1: {total_height + chamber.shape[0] - 1}")
def update_tail(H, T):
    if abs(T[0] - H[0]) > 1 or abs(T[1] - H[1]) > 1:
        if T[0] < H[0]:
            T[0] += 1
        elif T[0] > H[0]:
            T[0] -= 1
        if T[1] < H[1]:
            T[1] += 1
        elif T[1] > H[1]:
            T[1] -= 1

    return T

def simulate_rope(n):
    knots = [[0, 0] for i in range(n)]
    T_seen = set((0, 0))

    for direction, steps in moveset:
        for _ in range(steps):
            if direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1
            elif direction == "U":
                knots[0][1] += 1
            else:
                knots[0][1] -= 1

            for i in range(1, n):
                knot_pos = update_tail(knots[i-1], knots[i])
                knots[i] = knot_pos
            T_seen.add(tuple(knots[-1]))

    return len(T_seen) - 1

if __name__ == "__main__":
    with open("day9.txt", "r") as f:
        moveset = [(move[0], int(move[2:])) for move in f.read().split("\n")]

    print(f"Part 1: {simulate_rope(2)}")
    print(f"Part 1: {simulate_rope(10)}")

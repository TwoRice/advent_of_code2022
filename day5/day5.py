import re
import numpy as np

def move_crates(crates, n, start, end, reverse=True):
    n, start, end = int(n), int(start)-1, int(end)-1
    crates_to_move = crates[start][:n]
    if reverse: crates_to_move = crates_to_move[::-1]
    crates[end] = crates_to_move + crates[end]
    crates[start] = crates[start][n:]

if __name__ == "__main__":
    with open("day5.txt", "r") as f:
        raw_manifest = f.read().split("\n")

    # Parse crate stacks
    num_stacks = int(raw_manifest[8][-2])
    crates_start = " ".join(raw_manifest[:8]).replace("    ", "-")
    crates_start = list(re.subn("\s|\[|\]", "", crates_start)[0])
    crates_start = np.array(np.array_split(crates_start, len(crates_start) // num_stacks)).T
    crates_start = ["".join(stack).replace("-", "") for stack in crates_start]

    # Parse instructions
    instructions = raw_manifest[10:]
    instructions = [re.findall("\d+", step) for step in instructions]

    # Apply instructions
    part1_crates = crates_start.copy()
    part2_crates = crates_start.copy()
    for step in instructions:
        move_crates(part1_crates, *step)
        move_crates(part2_crates, *step, reverse=False)

    print(f"Part 1: {''.join([stack[0] for stack in part1_crates])}")
    print(f"Part 2: {''.join([stack[0] for stack in part2_crates])}")

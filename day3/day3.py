import numpy as np

def calculate_priority(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38

if __name__ == "__main__":
    with open("day3.txt", "r") as f:
        backpack_data = f.read().split("\n")

    compartment_data = [
        (backpack[:len(backpack)//2], backpack[len(backpack)//2:]) 
        for backpack in backpack_data
    ]
    common_items = [
        list(set(backpack[0]).intersection(backpack[1]))[0] 
        for backpack in compartment_data
    ]
    part1 = sum([calculate_priority(item) for item in common_items])
    print(f"Part 1: {part1}")

    group_packs = np.array_split(backpack_data, len(backpack_data) // 3)
    badges = [
        list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
        for group in group_packs
    ]
    part2 = sum([calculate_priority(item) for item in badges])
    print(f"Part 2: {part2}")
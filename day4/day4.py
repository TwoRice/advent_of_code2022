def elf_to_range(elf):
    return set(range(int(elf[0]), int(elf[1])+1))

if __name__ == "__main__":
    with open("day4.txt", "r") as f:
        cleaning_rota = [row.split(",") for row in f.read().split("\n")]

    part1, part2 = (0, 0)
    for row in cleaning_rota:
        elf1_range = elf_to_range(row[0].split("-"))
        elf2_range = elf_to_range(row[1].split("-"))
        if elf1_range.issubset(elf2_range) or elf1_range.issuperset(elf2_range):
            part1 += 1
        if len(elf1_range.intersection(elf2_range)) > 0:
            part2 += 1
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
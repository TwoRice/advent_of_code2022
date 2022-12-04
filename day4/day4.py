if __name__ == "__main__":
    with open("day4.txt", "r") as f:
        cleaning_rota = [row.split(",") for row in f.read().split("\n")]

    part1, part2 = (0, 0)
    for row in cleaning_rota:
        min1, max1 = [int(x) for x in row[0].split("-")]
        min2, max2 = [int(x) for x in row[1].split("-")]
        if (min1 >= min2 and max1 <= max2) or (min2 >= min1 and max2 <= max1):
            part1 += 1
        if max1 >= min2 and max2 >= min1:
            part2 += 1
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
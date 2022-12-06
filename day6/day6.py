def find(datastream, marker_length):
    for i in range(marker_length, len(datastream)):
        window = datastream[i-marker_length:i]
        if len(set(window)) == marker_length:
            return i

if __name__ == "__main__":
    with open("day6.txt", "r") as f:
        datastream = f.read()

    print(f"Part 1: {find(datastream, 4)}")
    print(f"Part 1: {find(datastream, 14)}")
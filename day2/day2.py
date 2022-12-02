if __name__ == "__main__":
    with open("day2.txt", "r") as f:
        strategy_data = f.read().split("\n")

    score_map = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    }
    print(f"Part 1: {sum(map(score_map.get, strategy_data))}")

    new_score_map = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }
    print(f"Part 2: {sum(map(new_score_map.get, strategy_data))}")
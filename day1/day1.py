import numpy as np

if __name__ == "__main__":
    with open("day1.txt", "r") as f:
        calorie_data = [
            np.array(elf.split("\n"), dtype=int) 
            for elf in f.read().split("\n\n")
        ]
    
    calorie_totals = np.array([sum(elf) for elf in calorie_data])
    print(f"Part 1: {max(calorie_totals)}")
    top_3_totals = sum(calorie_totals[np.argsort(calorie_totals)[-3:]])
    print(f"Part 2: {top_3_totals}")
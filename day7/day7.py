import operator
from functools import reduce

def get_current_dir(file_tree, path):
    return reduce(operator.getitem, path, file_tree)

def add_new_file(file_tree, path, file, details):
    new_file = {**get_current_dir(file_tree, path), **{file: details}}
    reduce(operator.getitem, path[:-1], file_tree)[path[-1]] = new_file

def traverse(filename, file, totals):
    if isinstance(file, dict):
        file_hash = hash(str(file))
        totals[file_hash] = 0
        for f, contents in file.items():
            totals[file_hash] += traverse(f, contents, totals)
        return totals[file_hash]
    else:
        return file

if __name__ == "__main__":
    with open("day7.txt", "r") as f:
        command_history = [
            command.split(" ") for 
            command in f.read().replace("/", "home").split("\n")
        ]

    ## Build file tree
    file_tree = {
        "home": {}
    }
    current_dir = ""

    for cmd in command_history:
        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    current_dir = current_dir[:current_dir.rfind("/")]
                else:
                    current_dir = f"{current_dir}/{cmd[2]}"
        else:
            details = {} if cmd[0] == "dir" else int(cmd[0])
            path = [directory for directory in current_dir.split("/")][1:]
            add_new_file(file_tree, path, cmd[1], details)

    ## Traverse file tree
    dir_totals = {}
    traverse("home", file_tree["home"], dir_totals)
    part1 = sum([total for _, total in dir_totals.items() if total <= 100000])
    print(f"Part 1: {part1}")

    ## Part 2
    home_hash = list(dir_totals.keys())[0]
    required_space = dir_totals[home_hash] - 40000000
    part2 = sorted([total for _, total in dir_totals.items() if total >= required_space])[0]
    print(f"Part 2: {part2}")
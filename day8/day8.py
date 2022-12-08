def get_tree_stats(trees, y, x):
    height = trees[y][x]
    hidden = [False, False, False, False]
    scores = [0, 0, 0, 0]
    for i in range(x + 1, len(trees)):
        scores[0] += 1
        if trees[y][i] >= height:
            hidden[0] = True
            break
    for i in range(x - 1, -1, -1):
        scores[1] += 1
        if trees[y][i] >= height:
            hidden[1] = True
            break
    for i in range(y + 1, len(trees)):
        scores[2] += 1
        if trees[i][x] >= height:
            hidden[2] = True
            break
    for i in range(y - 1, -1, -1):
        scores[3] += 1
        if trees[i][x] >= height:
            hidden[3] = True
            break
            
    return all(hidden), scores[0] * scores[1] * scores[2] * scores[3]

if __name__ == "__main__":
    with open("day8.txt", "r") as f:
        raw_data = f.read()
        trees = [[int(height) for height in row] for row in raw_data.split("\n")]

    hidden_trees = 0
    scenic_scores = []
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees) - 1):
            hidden, score = get_tree_stats(trees, y, x)
            hidden_trees += hidden
            scenic_scores.append(score)
    print(f"Part 1: {len(raw_data) - hidden_trees - len(trees) + 1}")
    print(f"Part 2: {max(scenic_scores)}")
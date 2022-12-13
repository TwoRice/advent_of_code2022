from ast import literal_eval

def inspect(packet1, packet2):    
    done = None
    if type(packet1) != type(packet2):
        if isinstance(packet1, int): packet1 = [packet1]
        if isinstance(packet2, int): packet2 = [packet2]
    
    for value1, value2 in zip(packet1, packet2):    
        if value1 == [] and value2 == []:
            continue
        elif isinstance(value1, int) and isinstance(value2, int):
            if value1 < value2: return True
            elif value1 > value2: return False
        elif isinstance(value1, list) and isinstance(value1, list):
            done = inspect(value1, value2)
        elif isinstance(value1, int):
            done = inspect(value1, value2) 
        elif isinstance(value2, int):
            done = inspect(value1, value2)
 
        if done is not None: return done
    
    return len(packet1) <= len(packet2)

def bubblesort(items):
    n = len(items)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if not inspect(items[j], items[j+1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False
        if already_sorted:
            break
        
    return items

if __name__ == "__main__":
    with open("day13.txt", "r") as f:
        distress_signal = [[literal_eval(packet) for packet in row.split("\n")] for row in f.read().split("\n\n")]

    correct = []
    for i, (packet1, packet2) in enumerate(distress_signal):
        if inspect(packet1, packet2): correct.append(i+1)
    print(f"Part 1: {sum(correct)}")

    distress_signal_flat = [packet for pair in distress_signal for packet in pair] + [[[2]], [[6]]]
    sorted_packets = bubblesort(distress_signal_flat)
    print(f"Part 2: {(sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)}")
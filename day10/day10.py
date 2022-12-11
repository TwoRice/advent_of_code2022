if __name__ == "__main__":
    with open("day10.txt", "r") as f:
        commands = [cmd.split(" ") for cmd in f.read().split("\n")]

    cmds = commands.copy()
    X, cycles = (1, 1)
    value, signal_str = (0, 0)
    process_add = False
    CRT = ""

    while(cmds or process_add):
        if (cycles - 20) % 40 == 0:
            signal_str += cycles * X
        
        if (cycles % 40) == 1: CRT += "\n"
        CRT += "#" if ((cycles - 1) % 40) in [X-1, X, X+1] else "."
        
        if process_add:
            cycles += 1
            X += value
            process_add = False
        else:
            cmd = cmds.pop(0)
            if cmd[0] == "noop":
                cycles += 1
            else:
                value = int(cmd[1])
                cycles += 1
                process_add = True
                
    print(f"Part 1: {signal_str}")
    print(f"Part 2: {CRT}")
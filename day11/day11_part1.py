import operator
from functools import reduce

operators = { "*": operator.mul, "+": operator.add} 

class Monkey():
    def __init__(self, stats):
        self.items = [int(item.replace(",", "")) for item in stats[0].split(" ")[2:]]
        self.op = self._create_op(stats[1].split("= ")[1])
        self.test = self._create_test(*[int(case.split(" ")[-1]) for case in stats[2:]])
        self.inspected = 0
        
    def _create_op(self, operation):
        _, operator, operand = operation.split(" ")
        return lambda x: reduce(
            operators[operator], 
            [x, x if operand == "old" else int(operand)]
        )
        
    def _create_test(self, div_by, if_true, if_false):
        self.div_by = div_by
        return lambda x: if_true if x % div_by == 0 else if_false

def monkey_game(monkeys, rounds, calm=True):        
    for i in range(rounds):
        for monkey in monkeys:
            while(monkey.items):
                monkey.inspected += 1
                item = monkey.items.pop(0)
                worry = monkey.op(item)
                worry = worry // 3
                throw_to = monkey.test(worry)
                monkeys[throw_to].items.append(worry)

    items_inspected = sorted([mon.inspected for mon in monkeys])
    return items_inspected[-1] * items_inspected[-2]

if __name__ == "__main__":
    with open("day11.txt", "r") as f:
        monkey_stats = [
            [stat.strip() for stat in monkey.split("\n")[1:]] 
            for monkey in f.read().split("\n\n")
        ]

    monkeys = [Monkey(stats) for stats in monkey_stats]
    print(monkey_game(monkeys, 20))
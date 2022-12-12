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
        return lambda x, z: reduce(
            operators[operator], 
            [x, x if operand == "old" else int(operand)]
        ) % z
        
    def _create_test(self, div_by, if_true, if_false):
        self.div_by = div_by
        return lambda x: if_true if x % div_by == 0 else if_false

def monkey_game(monkeys, rounds, calm=True):
    for monkey in monkeys:
        new_items = []
        for item in monkey.items:
            new_item = []
            for monkey2 in monkeys:
                new_item.append(item % monkey2.div_by)
            new_items.append(new_item)
        monkey.items = new_items
        
    for i in range(rounds):
        for m, monkey in enumerate(monkeys):
            while(monkey.items):
                monkey.inspected += 1
                item = monkey.items.pop(0)
                for m2, monkey2 in enumerate(monkeys):
                    item[m2] = monkey.op(item[m2], monkey2.div_by)
                throw_to = monkey.test(item[m])
                monkeys[throw_to].items.append(item)

    items_inspected = sorted([mon.inspected for mon in monkeys])
    return items_inspected[-1] * items_inspected[-2]


if __name__ == "__main__":
    with open("day11.txt", "r") as f:
        monkey_stats = [
            [stat.strip() for stat in monkey.split("\n")[1:]] 
            for monkey in f.read().split("\n\n")
        ]

    monkeys = [Monkey(stats) for stats in monkey_stats]
    print(monkey_game(monkeys, 10000))
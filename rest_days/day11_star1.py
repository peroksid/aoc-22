from dataclasses import dataclass, field
from lib import read_lines_from_input


ROUNDS = 20
EXAMPLE_LINES = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


@dataclass
class Monkey:
    index: int
    operation: str
    test_divider: int
    on_zero: int
    on_else: int
    throw_count: int = field(default=0)
    monkey_items: list[list[int]] = field(default_factory=list)

    @staticmethod
    def reduce_worry_level(worry_level: int) -> int:
        return worry_level // 3

    def inspect_items(self):
        while self.monkey_items[self.index]:
            item = self.monkey_items[self.index].pop()
            worry_level = eval(self.operation, {"old": item})
            worry_level = self.reduce_worry_level(worry_level)
            if worry_level % self.test_divider == 0:
                self.monkey_items[self.on_zero].append(worry_level)
            else:
                self.monkey_items[self.on_else].append(worry_level)
            self.throw_count += 1

    @classmethod
    def generate_monkey_world(cls, description_lines: list[str]) -> list["Monkey"]:
        monkey_items = []
        monkey_states = []

        index = None
        operation = None
        test_divider = None
        on_zero = None
        on_else = None
        throw_count = 0
        for i, line in enumerate(description_lines):
            line = line.strip()
            if line.strip().startswith("Monkey"):
                index = int(line.split()[1][:-1])
            elif line.startswith("Starting items: "):
                monkey_items.append(list(map(int, line.split(":")[1].split(","))))
            elif line.startswith("Operation"):
                operation = line.split("new = ")[1].strip()
            elif line.startswith("Test: "):
                test_divider = int(line.split("divisible by ")[1].split()[0])
            elif line.startswith("If true:"):
                on_zero = int(line.split("to monkey ")[1].split()[0])
            elif line.startswith("If false:"):
                on_else = int(line.split("to monkey ")[1].split()[0])
            if line.strip() == "":
                monkey_states.append(
                    cls(
                        index,
                        operation,
                        test_divider,
                        on_zero,
                        on_else,
                        throw_count,
                        monkey_items,
                    )
                )
                index = None
                operation = None
                test_divider = None
                on_zero = None
                on_else = None
                throw_count = 0
        else:
            monkey_states.append(
                cls(
                    index,
                    operation,
                    test_divider,
                    on_zero,
                    on_else,
                    throw_count,
                    monkey_items,
                )
            )
        return monkey_states


def count_monkey_business(rounds: int, lines: list[str], monkey_class: type) -> int:
    """
    >>> count_monkey_business(20, EXAMPLE_LINES.splitlines())
    10605
    """
    monkeys = monkey_class.generate_monkey_world(lines)
    for j in range(rounds):
        for monkey in monkeys:
            monkey.inspect_items()

    monkeys.sort(key=lambda monkey: -monkey.throw_count)
    return monkeys[0].throw_count * monkeys[1].throw_count


def main():
    print(count_monkey_business(20, read_lines_from_input(), Monkey))


if __name__ == "__main__":
    main()
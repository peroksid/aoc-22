from dataclasses import dataclass, field
from day11_star1 import count_monkey_business, Monkey, EXAMPLE_LINES
from gmpy2 import mpz, add, is_divisible, mul
from lib import read_lines_from_input
from functools import cache

ROUNDS = 10000

def main():
    """
    >>> count_monkey_business(ROUNDS, EXAMPLE_LINES.splitlines(), SkeletonMonkey)
    2713310158
    """
    print(count_monkey_business(ROUNDS, read_lines_from_input(), SkeletonMonkey))


@dataclass
class Item:
    #__slots__ = ("value", "monkey_id")
    value: mpz
    monkey_id: int
    reminders_for_dividers: dict[int, int] = field(default_factory=dict)

    def prepare_for_dividers(self, dividers: list[int]) -> None:
        for divider in dividers:
            if divider not in self.reminders_for_dividers:
                self.reminders_for_dividers[divider] = self.value % divider
    
    def update_reminders(self, op) -> None:
        for divider in self.reminders_for_dividers:
            self.reminders_for_dividers[divider] = op(self.reminders_for_dividers[divider]) % divider
    
    def is_divisible_by(self, divider: int) -> bool:
        return self.reminders_for_dividers[divider] == 0
        

@dataclass
class SkeletonMonkey(Monkey):
    #__slots__ = ("operation", "test_divider", "on_zero", "on_else", "callable_op", "throw_count")
    callable_op: callable = None
    
    def get_worry_level(self, item: Item) -> int:
        return self.callable_op(item.value)

    def inspect_items(self):
        for item in self.monkey_items:
            if item.monkey_id == self.index:
                item.update_reminders(self.callable_op)
                new_monkey_id = self.on_zero if item.is_divisible_by(self.test_divider) else self.on_else
                item.monkey_id = new_monkey_id
                self.throw_count += 1

    @classmethod
    def generate_monkey_world(cls, description_lines: list[str]) -> list["SkeletonMonkey"]:
        monkeys = super(SkeletonMonkey, cls).generate_monkey_world(description_lines)
        solid_items = []
        for monkey_id, items in enumerate(monkeys[0].monkey_items):
            for item in items:
                solid_items.append(Item(mpz(item), monkey_id))
        dividers = []
        for monkey in monkeys:
            if monkey.test_divider not in dividers:
                dividers.append(monkey.test_divider)
            monkey.callable_op = eval(f"lambda old: {monkey.operation}")
        for item in solid_items:
            item.prepare_for_dividers(dividers)
        for monkey in monkeys:
            monkey.monkey_items = solid_items
        # for item in solid_items:
        #     item.prepare_for_dividers(dividers)
        #     # if monkey.operation == "old * old":
        #     #     monkey.callable_op = lambda old: mul(old, old)
        #     # elif monkey.operation.startswith("old *"):
        #     #     xxx = mpz(monkey.operation.split("old * ")[1])
        #     #     monkey.callable_op = lambda old: add(old, xxx)
        #     # elif monkey.operation == "old + old":
        #     #     monkey.callable_op = lambda old: add(old, old)
        #     # elif monkey.operation.startswith("old +"):
        #     #     xxx = mpz(monkey.operation.split("old + ")[1])
        #     #     monkey.callable_op = lambda old: add(old, xxx)
        #     # else:
        #     #     raise ValueError(f"Unknown operation: {monkey.operation}")
        #     #monkey.callable_op = cache(monkey.callable_op)
        #     #monkey.callable_op = cache(eval(f"lambda old: {monkey.operation}"))
            
        return monkeys


def profile():
    import cProfile
    cProfile.run("count_monkey_business(1000, EXAMPLE_LINES.splitlines(), SkeletonMonkey)")

if __name__ == "__main__":    
    main()
    #profile()

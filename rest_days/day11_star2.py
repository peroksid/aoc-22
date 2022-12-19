from dataclasses import dataclass, field
from day11_star1 import count_monkey_business, Monkey, EXAMPLE_LINES
from lib import read_lines_from_input

ROUNDS = 10000

def main():
    """
    >>> count_monkey_business(ROUNDS, EXAMPLE_LINES.splitlines(), SkeletonMonkey)
    2713310158
    """
    print(count_monkey_business(ROUNDS, read_lines_from_input(), SkeletonMonkey))


@dataclass
class Item:
    value: int
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
            solid_items.extend(Item(item, monkey_id) for item in items)
        dividers = []
        for monkey in monkeys:
            if monkey.test_divider not in dividers:
                dividers.append(monkey.test_divider)
            monkey.callable_op = eval(f"lambda old: {monkey.operation}")
        for item in solid_items:
            item.prepare_for_dividers(dividers)
        for monkey in monkeys:
            monkey.monkey_items = solid_items            
        return monkeys


def profile():
    import cProfile
    cProfile.run("count_monkey_business(1000, EXAMPLE_LINES.splitlines(), SkeletonMonkey)")

if __name__ == "__main__":    
    main()
    #profile()

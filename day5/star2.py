import sys
from typing import Dict, List
import dataclasses

@dataclasses.dataclass
class Cargo:
  stacks:List[str] = dataclasses.field(default_factory=list)
  stack_labels: Dict[str, int] = dataclasses.field(default_factory=dict)
  
  def stack_index(self, label: str) -> int:
    return self.stack_labels[label]

  def move_crates(self, cargo_count: int, from_stack_label: str, to_stack_label: str):
    from_stack = self.stacks[self.stack_index(from_stack_label)]
    to_stack = self.stacks[self.stack_index(to_stack_label)]
    acc = []
    for _ in range(cargo_count):
      acc.insert(0, from_stack.pop())
    to_stack.extend(acc)

  def prepend_stacks(self, line: str):
    if len(self.stacks) == 0:
      for _ in range(len(line) // 4):
        self.stacks.append([])
    for i in range(1, len(line), 4):
      j = (i - 1) // 4
      x = line[i]
      if x != ' ':
        if x.isdigit():
          self.stack_labels[x] = j
        else:
          self.stacks[j].insert(0, x)

  def move(self, line: str):
    _, cargo_count, _, from_label, _, to_label = line.strip().split(' ')
    self.move_crates(int(cargo_count), from_label, to_label)


def main():
  cargo = Cargo()
  is_map_collected = False
  for line in sys.stdin:
    if is_map_collected:
      cargo.move(line)
    else:
      if line.strip() == "":
        is_map_collected = True
      else:
        cargo.prepend_stacks(line)
  result = "".join([x[-1] for x in cargo.stacks])
  print(result)
    
if __name__ == "__main__":
  main()
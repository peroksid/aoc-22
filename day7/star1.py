import dataclasses
import sys
from typing import Dict, List, Optional



@dataclasses.dataclass
class DirNode:
    parent: Optional["DirNode"]
    name: str
    total_size: int = dataclasses.field(default=0)
    directories: Dict[str, "DirNode"] = dataclasses.field(default_factory=dict)
    files: Dict[str, int] = dataclasses.field(default_factory=dict)

class Directories:
    def __init__(self, root_name):
        self.root = DirNode(None, root_name, 0)
        self.current = self.root

    def cd(self, name):
        if name == "..":
            self.current = self.current.parent
        elif name == "/":
            self.current = self.root
        else:
            self.current = self.current.directories[name]

    def mkdir(self, name):
        self.current.directories[name] = DirNode(self.current, name, 0)

    def touch(self, name, size):
        self.current.files[name] = size
        xxx = self.current
        while True:
            xxx.total_size += size
            if xxx.parent is None:
                break
            xxx = xxx.parent

DOCTEST_EXAMPLE = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

def log_in_test(line):
  if __name__ != "__main__":
    sys.stderr.write(line + "\n")


def fill_fs(lines: List[str]) -> Directories:
    directories = Directories("/")
    for line in lines:
        token = line.split(" ")
        if token[0] == "$":
            if token[1] == "cd":
                directories.cd(token[2])
            elif token[1] == "ls":
                pass
            else:
                raise Exception("Unknown command: " + token[1])
        elif token[0] == "dir":
            directories.mkdir(token[1])
        elif token[0].isdigit():
            directories.touch(token[1], int(token[0]))
    return directories

def sum_all_below_100k(lines: List[str]):
    '''
    >>> sum_all_below_100k(DOCTEST_EXAMPLE.splitlines())
    95437
    '''
    directories = fill_fs(lines)
    nodes = [directories.root]
    acc = 0
    while nodes:
        current = nodes.pop()
        log_in_test(f"name: {current.name}, size: {current.total_size}")
        if current.total_size < 100_000:
            acc += current.total_size
        nodes.extend(current.directories.values())
    return acc

def main(f):
    print(f([x.strip() for x in sys.stdin.readlines()]))


if __name__ == "__main__":
    main(sum_all_below_100k)

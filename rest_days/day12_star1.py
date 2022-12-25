from dataclasses import dataclass, field
from typing import ClassVar
from lib import read_lines_from_input
from functools import partial
from collections import namedtuple


EXAMPLE_MAP = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


Point = namedtuple("Point", ["x", "y"])

START = "S"
END = "E"


@dataclass
class Path:
    tip: Point
    steps: int = field(default=0)
    path: list[Point] = field(default_factory=list)  # debug
    visited: ClassVar[set[Point]] = set()
    
    @classmethod
    def enter(cls, point: Point) -> "Path":
        cls.visited.add(point)
        return Path(point, 1, [point])

    def branch(self, point: Point) -> "Path":
        self.visited.add(point)
        return Path(point, self.steps + 1, self.path.copy() + [point])


def is_passable_by_threshold(
    lines: list[str], threshold: int, a: Point, b: Point
) -> bool:
    """
    >>> is_passable_by_threshold(EXAMPLE_MAP.splitlines(), 1, Point(0, 0), Point(0, 1))
    True
    >>> is_passable_by_threshold(EXAMPLE_MAP.splitlines(), 1, Point(0, 1), Point(1, 1))
    True
    >>> is_passable_by_threshold(EXAMPLE_MAP.splitlines(), 1, Point(2, 0), Point(3, 0))
    False
    >>> is_passable_by_threshold(EXAMPLE_MAP.splitlines(), 1, Point(2, 0), Point(2, 0))
    True
    """
    a_chr = lines[a.y][a.x]
    b_chr = lines[b.y][b.x]
    if a_chr == START:
        a_ord = ord('a')
    else:
        a_ord = ord(a_chr)
    if b_chr == END:
        b_ord = ord('z')
    else:
        b_ord = ord(b_chr)
    return b_ord - threshold <= a_ord


def get_neighbors(n: int, m: int, point: Point) -> list[Point]:
    """
    >>> get_neighbors(3, 3, Point(0, 0))
    [Point(x=1, y=0), Point(x=0, y=1)]
    >>> get_neighbors(1, 100, Point(0, 20))
    [Point(x=0, y=19), Point(x=0, y=21)]
    
    """
    neighbors = []
    if point.x > 0:
        neighbors.append(Point(point.x - 1, point.y))
    if point.x < n - 1:
        neighbors.append(Point(point.x + 1, point.y))
    if point.y > 0:
        neighbors.append(Point(point.x, point.y - 1))
    if point.y < m - 1:
        neighbors.append(Point(point.x, point.y + 1))
    return neighbors


def find_points_in_lines(lines: list[str], targets: list[str]) -> list[Point]:
    results = [None for _ in targets]
    indexes: dict[str, int] = {v: k for (k, v) in enumerate(targets)}
    
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char in indexes:
                results[indexes[char]] = Point(char_index, line_index)

    assert all([x is not None for x in results]), results
    return results

def outchr(lines: list[str], point: Point) -> str:
    return lines[point.y][point.x]

def count_fewest_steps(lines: list[str]) -> int:
    """
    >>> count_fewest_steps(EXAMPLE_MAP.splitlines())
    31
    """
    start, end = find_points_in_lines(lines, [START, END])
    get_next_ones = partial(get_neighbors, len(lines[0]), len(lines))
    is_passable = partial(is_passable_by_threshold, lines, 1)
    out = partial(outchr, lines)

    paths = [Path.enter(start)]
    complete_paths = []
    while paths:
        path = paths.pop()
        neighbors = get_next_ones(path.tip)
        not_visited = [x for x in neighbors if x not in path.visited]
        at_most_one_close = [x for x in not_visited if is_passable(path.tip, x)]
        for n in at_most_one_close:
            if n == end:
                complete_paths.append(path)
            else:
                paths.insert(0, path.branch(n))

    return min([x.steps for x in complete_paths])


def main():
    print(count_fewest_steps(read_lines_from_input()))


if __name__ == "__main__":
    main()

from lib import read_lines_from_input

EXAMPLE_MOVES = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
def parse_str_ints_from_lines(lines: list[str]) -> list[tuple[str, int]]:
    """
    >>> parse_str_ints_from_lines(['1 2', '3 4'])
    [('1', 2), ('3', 4)]
    """
    return [(a, int(b)) for (a, b) in [tuple(line.strip().split()) for line in lines]]

def get_next_step_head_position(head: tuple[int, int], direction: str) -> tuple[int, int]:
    """
    >>> get_next_step_head_position((0, 0), 'R')
    (1, 0)
    >>> get_next_step_head_position((0, 0), 'L')
    (-1, 0)
    >>> get_next_step_head_position((0, 0), 'U')
    (0, 1)
    >>> get_next_step_head_position((0, 0), 'D')
    (0, -1)
    """
    x, y = head
    if direction == 'R':
        return x + 1, y
    elif direction == 'L':
        return x - 1, y
    elif direction == 'U':
        return x, y + 1
    elif direction == 'D':
        return x, y - 1
    else:
        raise ValueError(f"Invalid direction: {direction}")


def get_next_step_tail_position(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    """
    >>> get_next_step_tail_position((0, 0), (0, 0))
    (0, 0)
    >>> get_next_step_tail_position((1, 0), (0, 0))
    (0, 0)
    >>> get_next_step_tail_position((0, 1), (0, 0))
    (0, 0)
    >>> get_next_step_tail_position((0, 0), (1, 0))
    (1, 0)
    >>> get_next_step_tail_position((0, 0), (0, 1))
    (0, 1)
    >>> get_next_step_tail_position((1, 1), (0, 0))
    (0, 0)
    >>> get_next_step_tail_position((1, 1), (1, 0))
    (1, 0)
    >>> get_next_step_tail_position((1, 1), (0, 1))
    (0, 1)
    >>> get_next_step_tail_position((1, 1), (1, 1))
    (1, 1)
    """
    hx, hy = head
    tx, ty = tail
    dx = hx - tx
    dy = hy - ty
    adx = abs(dx)
    ady = abs(dy)
    if adx < 2 and ady < 2:
        return tail

    if adx == 2:
        incx = dx // 2
        newx = tx + incx
        newy = hy
        return newx, newy
    elif ady == 2:
        incy = dy // 2
        newx = hx
        newy = ty + incy
        return newx, newy
    else:
        raise ValueError(f"Invalid head and tail positions: {head}, {tail}")


class Rope:
    head: tuple[int, int]
    tail: tuple[int, int]
    visited_spots: set[tuple[int, int]]
    def __init__(self, head: tuple[int, int], tail: tuple[int, int]):
        self.head = head
        self.tail = tail
        self.visited_spots = set([tail])
    
    def move(self, direction: str, path: int) -> None:
        for _ in range(path):
            self.move_one_step(direction)
        
    def move_one_step(self, direction: str) -> None:
        self.head = get_next_step_head_position(self.head, direction)
        self.tail = get_next_step_tail_position(self.head, self.tail)
        self.visited_spots.add(self.tail)
        
    def report_unique_visited_spots_count(self) -> int:
        return len(self.visited_spots)
    

def count_tail_visited_spots(moves: list[tuple[str, int]]) -> int:
    """
    >>> count_tail_visited_spots(parse_str_ints_from_lines(EXAMPLE_MOVES.splitlines()))
    13
    """
    rope = Rope((0, 0), (0, 0))
    for direction, path in moves:
        rope.move(direction, path)
    return rope.report_unique_visited_spots_count()

def main():
    print(count_tail_visited_spots(parse_str_ints_from_lines(read_lines_from_input())))

if __name__ == "__main__":
    main()
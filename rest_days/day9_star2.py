from day9_star1 import get_next_step_head_position, get_next_step_tail_position
from lib import read_lines_from_input, parse_str_ints_from_lines

EXAMPLE_MOVES = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


class LongRope:
    knots: list[tuple[int, int]] = []
    visited_spots: set[tuple[int, int]]

    def __init__(self, rope_length: int):
        self.knots = [(0, 0)] * rope_length
        self.visited_spots = {(0, 0)}

    def move(self, direction: str, path: int) -> None:
        for _ in range(path):
            self.move_one_step(direction)
    
    def move_one_step(self, direction: str) -> None:
        # import pprint
        # pprint.pprint(self.knots)
        self.knots[0] = get_next_step_head_position(self.knots[0], direction)
        # print("after head:")
        # pprint.pprint(self.knots)
        for i in range(1, len(self.knots)):
            # print(f"on {i}:")
            # pprint.pprint(self.knots)
            self.knots[i] = get_next_step_tail_position(self.knots[i-1], self.knots[i])
            # print(f"after {i}:")
            # pprint.pprint(self.knots)
        self.visited_spots.add(self.knots[-1])
        #raise RuntimeError("")
    
    def report_unique_visited_spots_count(self) -> int:
        return len(self.visited_spots)

def count_tail_visited_spots(moves: list[tuple[str, int]]) -> int:
    """
    >>> count_tail_visited_spots(parse_str_ints_from_lines(EXAMPLE_MOVES.splitlines()))
    36
    """
    rope = LongRope(10)
    for direction, path in moves:
        rope.move(direction, path)
    return rope.report_unique_visited_spots_count()


def main():
    print(count_tail_visited_spots(parse_str_ints_from_lines(read_lines_from_input())))


if __name__ == "__main__":
    main()
import sys


def read_lines_from_input() -> list[str]:
    """
    >>> read_lines_from_input()
    ['1', '2', '3', '4']
    """
    return sys.stdin.readlines()

def parse_2d_ints_from_lines(lines: list[str]) -> list[list[int]]:
    """
    >>> parse_2d_ints_from_lines(['1 2', '3 4'])
    [[1, 2], [3, 4]]
    """
    return [list(map(int, list(line.strip()))) for line in lines]


def parse_str_ints_from_lines(lines: list[str]) -> list[tuple[str, int]]:
    """
    >>> parse_str_ints_from_lines(['1 2', '3 4'])
    [('1', 2), ('3', 4)]
    """
    return [(a, int(b)) for (a, b) in [tuple(line.strip().split()) for line in lines]]

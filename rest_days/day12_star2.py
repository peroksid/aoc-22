from day12_star1 import (
    EXAMPLE_MAP,
    find_points_in_lines,
    START,
    END,
    Point,
    get_neighbors,
    is_passable_by_threshold,
)
from lib import read_lines_from_input
from functools import partial

A = "a"


def find_min_path(lines: list[str]) -> int:
    """
    >>> find_min_path(EXAMPLE_MAP.splitlines())
    29
    """
    (end_point, start_point) = find_points_in_lines(lines, [END, START])
    points = [end_point]

    get_around = partial(get_neighbors, len(lines[0]), len(lines))
    is_passable = partial(is_passable_by_threshold, lines, 1)

    paths = [[float("inf")] * len(lines[0]) for _ in lines]
    paths[end_point.y][end_point.x] = 0

    visited = set([])

    while points:
        point = points.pop()

        for neighbor in get_around(point):
            if neighbor in points:
                continue
            if neighbor in visited:
                continue
            if not is_passable(neighbor, point):
                continue
            points.insert(0, neighbor)
            paths[neighbor.y][neighbor.x] = paths[point.y][point.x] + 1
        visited.add(point)

    min_path = paths[start_point.y][start_point.x]
    for y, line in enumerate(paths):
        for x, val in enumerate(line):
            if lines[y][x] == A:
                min_path = min(min_path, val)
    return min_path


def main():
    print(find_min_path(read_lines_from_input()))


if __name__ == "__main__":
    main()

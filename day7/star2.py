import functools
import sys
from star1 import main, fill_fs, DOCTEST_EXAMPLE

def delete_smallest_to_free(lines: list[str], total_drive_size: int, required_free_space: int) -> int:
    """
    >>> delete_smallest_to_free(DOCTEST_EXAMPLE.splitlines(), 70_000_000, 30_000_000)
    24933642
    """
    fs = fill_fs(lines)
    spare_size = total_drive_size - fs.root.total_size - required_free_space
    if spare_size > 0:
        return 0
    known_sizes = []
    nodes = [fs.root]
    while nodes:
        node = nodes.pop()
        if total_drive_size - fs.root.total_size + node.total_size > required_free_space:
            known_sizes.append(node.total_size)
        nodes.extend(node.directories.values())
    return min(known_sizes)


if __name__ == "__main__":
    f = functools.partial(delete_smallest_to_free, total_drive_size=70_000_000, required_free_space=30_000_000)
    main(f)

import sys


def clock():
    cycle = 1
    while True:
        yield cycle
        cycle += 1


def sum_signal_strength(lines: list[str]) -> int:
    """
    >>> sum_signal_strength(EXAMPLE_OPS.splitlines())
    13140
    """
    x = 1
    signal_strength = 0
    cycle_gen = clock()

    def next_cycle():
        nonlocal x
        nonlocal signal_strength
        nonlocal cycle_gen
        cycle = next(cycle_gen)
        if cycle == 20 or (cycle - 20) % 40 == 0:
            signal_strength += x * cycle

    for line in lines:
        if line.startswith("noop"):
            next_cycle()
        elif line.startswith("addx"):
            next_cycle()
            next_cycle()
            x += int(line.split()[1])
    return signal_strength


def main():
    lines = sys.stdin.readlines()
    print(sum_signal_strength(lines))


if __name__ == "__main__":
    main()

EXAMPLE_OPS = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

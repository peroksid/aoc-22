from lib import read_lines_from_input
from day10_star1 import EXAMPLE_OPS

WIDTH = 40
HEIGHT = 6
SPRITE_WIDTH = 3
INIT = "?"
LIT = "#"
DARK = "."


class Buffer:
    width: int
    height: int
    buffer: list[str]
    def __init__(self, width: int, height: int):
        self.buffer = [INIT] * (width * height)
        self.width = width
        self.height = height

    def __str__(self):
        """
        >>> b = Buffer(3, 2)
        >>> b.buffer = ['a', 'b', 'c', 'd', 'e', 'f']
        >>> print(b)
        abc
        def
        """
        return "\n".join(
            ["".join(self.buffer[i*self.width:i*self.width+self.width]) for i in range(self.height)]
        )


class CPU:
    x: int
    next_x: int
    busy_for: int

    def __init__(self):
        self.x = 0
        self.next_x = 0
        self.busy_for = 0
    
    def tick(self):
        #print("?", self.x, self.next_x, self.busy_for)
        self.busy_for -= 1
        if self.busy_for == 0:
            self.x = self.next_x
        #print("!", self.x, self.next_x, self.busy_for)

    def plan_busy(self, cycles: int):
        self.busy_for = cycles

    def plan_x(self, increment: int):
        self.next_x = self.x + increment


class CRT:
    buffer: Buffer
    cpu: CPU
    clock: int
    def __init__(self, cpu: CPU):
        self.buffer = Buffer(WIDTH, HEIGHT)
        self.cpu = cpu
        self.clock = 0
    
    def render(self):
        sprite_start = self.cpu.x
        sprite_end = self.cpu.x + SPRITE_WIDTH - 1
        char = LIT if sprite_start <= self.clock % 40 <= sprite_end else DARK
        #print(sprite_start, sprite_end, self.clock % 40, self.clock, char)
        self.buffer.buffer[self.clock] = char

    def render_till_cpu_empty(self):
        while self.cpu.busy_for:
            self.render()
            self.cpu.tick()
            self.clock += 1


def render_crt(lines: list[str]) -> None:
    """
    >>> print(render_crt(EXAMPLE_OPS.splitlines()))
    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....
    """
    cpu = CPU()
    crt = CRT(cpu)
    for line in lines:
        #print(f"CMD: {line}")
        if line.startswith("noop"):
            cpu.plan_busy(1)
        elif line.startswith("addx"):
            cpu.plan_busy(2)
            cpu.plan_x(int(line.split()[1]))
        crt.render_till_cpu_empty()
    return str(crt.buffer)


def main():
    print(render_crt(read_lines_from_input()))

if __name__ == "__main__":
    main()
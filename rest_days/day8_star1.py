from lib import read_lines_from_input, parse_2d_ints_from_lines

EXAMPLE_MAP = """30373
25512
65332
33549
35390
"""

def count_visible_trees(map: list[list[int]]) -> int:
    """
    >>> count_visible_trees(parse_2d_ints_from_lines(EXAMPLE_MAP.splitlines()))
    21
    """
    left_right_maximums = [[float("-inf") for _ in range(len(map[0]))] for _ in range(len(map))]
    right_left_maximums = [[float("-inf") for _ in range(len(map[0]))] for _ in range(len(map))]
    top_bottom_maximums = [[float("-inf") for _ in range(len(map[0]))] for _ in range(len(map))]
    bottom_top_maximums = [[float("-inf") for _ in range(len(map[0]))] for _ in range(len(map))]
    for y in range(len(map)):
        for x in range(len(map[0])):
            if x == 0:
                pass
                #left_right_maximums[y][x] = float("-inf")    
            else:
                left_right_maximums[y][x] = max(left_right_maximums[y][x-1] , map[y][x-1])
    for y in range(len(map)):
        for x in range(len(map[0])-1, -1, -1):
            if x == len(map[0])-1:
                pass
                #right_left_maximums[y][x] = float("-inf")
            else:
                right_left_maximums[y][x] = max(right_left_maximums[y][x+1], map[y][x+1])
    for y in range(len(map)):
        for x in range(len(map[0])):
            if y == 0:
                pass
                #top_bottom_maximums[y][x] = float("-inf")
            else:
                top_bottom_maximums[y][x] = max(top_bottom_maximums[y-1][x], map[y-1][x])
    for y in range(len(map)-1, -1, -1):
        for x in range(len(map[0])):
            if y == len(map)-1:
                pass
                #bottom_top_maximums[y][x] = float("-inf")
            else:
                bottom_top_maximums[y][x] = max(bottom_top_maximums[y+1][x], map[y+1][x])
    count = 0
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] > left_right_maximums[y][x] or map[y][x] > right_left_maximums[y][x] or map[y][x] > top_bottom_maximums[y][x] or map[y][x] > bottom_top_maximums[y][x]:
                count += 1
    return count
        

def main():
    map = parse_2d_ints_from_lines(read_lines_from_input())
    print(count_visible_trees(map))

if __name__ == "__main__":
    main()
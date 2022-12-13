from abc import ABC, abstractmethod
import bisect
from lib import read_lines_from_input, parse_2d_ints_from_lines
from day8_star1 import EXAMPLE_MAP


class BaseViewingDistance(ABC):
    dp: list[list[int]]

    def __init__(self, tree_map: list[list[int]]):
        self.dp = [[0 for _ in range(len(tree_map[0]))] for _ in range(len(tree_map))]
        self.fill_dp(tree_map)

    def __call__(self, i: int, j: int) -> int:
        return self.dp[i][j]

    @abstractmethod
    def fill_dp(self, tree_map: list[list[int]]) -> None:
        pass


def viewing_distance_generator(height_iterator):
    known_height: list[int] = []
    height_cache: dict[int, int] = {}
    for i, h in enumerate(height_iterator):
        if i == 0:
            known_height.append(h)
            height_cache[h] = i
            yield 0
        else:
            ip = bisect.bisect_left(known_height, h)
            if ip == len(known_height):
                # h is the tallest
                known_height.append(h)
                height_cache[h] = i
                yield i
            else:
                # h is not the tallest
                # viewing distance will be the closest tallest-even
                all_taller_or_equal = known_height[ip:]
                closest_i = max([height_cache[x] for x in all_taller_or_equal])
                viewing_distance = i - closest_i # i: 7, closest_i: 5, viewing_distance: 2
                # no point in insering the known height if it's already there
                if h not in height_cache:
                    known_height.insert(ip, h)
                height_cache[h] = i
                yield viewing_distance


class LeftViewingDistance(BaseViewingDistance):
    """
    1 2 3 4 5
    0 1 2 3 4

    1 3 1 2 2
    0 1 1
    """

    def fill_dp(self, tree_map: list[list[int]]) -> None:
        for i in range(len(self.dp)):
            for j, viewing_distance in enumerate(viewing_distance_generator(tree_map[i])):
                self.dp[i][j] = viewing_distance

class RightViewingDistance(BaseViewingDistance):
    def fill_dp(self, tree_map: list[list[int]]) -> None:
        for i in range(len(self.dp)):
            for j, viewing_distance in enumerate(viewing_distance_generator(reversed(tree_map[i]))):
                self.dp[i][len(tree_map[i])-j - 1] = viewing_distance


class TopViewingDistance(BaseViewingDistance):
    def fill_dp(self, tree_map: list[list[int]]) -> None:
        for j in range(len(self.dp[0])):
            it = (tree_map[i][j] for i in range(len(tree_map)))
            for i, viewing_distance in enumerate(viewing_distance_generator(it)):
                self.dp[i][j] = viewing_distance


class BottomViewingDistance(BaseViewingDistance):
    def fill_dp(self, tree_map: list[list[int]]) -> None:
        for j in range(len(self.dp[0])):
            it = reversed([tree_map[i][j] for i in range(len(tree_map))])
            for i, viewing_distance in enumerate(viewing_distance_generator(it)):
                self.dp[len(tree_map) - i - 1][j] = viewing_distance


def count_scenic_score(tree_map: list[list[int]]) -> int:
    """
    >>> count_scenic_score(parse_2d_ints_from_lines(EXAMPLE_MAP.splitlines()))
    8
    """
    left_viewing_distance = LeftViewingDistance(tree_map)
    right_viewing_distance = RightViewingDistance(tree_map)
    top_viewing_distance = TopViewingDistance(tree_map)
    bottom_viewing_distance = BottomViewingDistance(tree_map)
    max_scenic_score = 0
    # import pprint
    # pprint.pprint(tree_map)
    # pprint.pprint(left_viewing_distance.dp)
    # pprint.pprint(right_viewing_distance.dp)
    # pprint.pprint(top_viewing_distance.dp)
    # pprint.pprint(bottom_viewing_distance.dp)

    for i in range(len(tree_map)):
        for j in range(len(tree_map[0])):
            scenic_score = (
                left_viewing_distance(i, j)
                * right_viewing_distance(i, j)
                * top_viewing_distance(i, j)
                * bottom_viewing_distance(i, j)
            )
            max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score


def main():
    tree_map = parse_2d_ints_from_lines(read_lines_from_input())
    print(count_scenic_score(tree_map))


if __name__ == "__main__":
    main()
